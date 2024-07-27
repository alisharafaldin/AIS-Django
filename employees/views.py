from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from employees.models import *
from django.views.generic import CreateView
from .forms import EmpForm
from django.contrib.auth.decorators import login_required
from basicinfo.forms import PersonForm
from basicinfo.models import Region, States, Cities, WorkSpecialty, BranchBank
from django.http import JsonResponse

# Create your views here.

# def search(request, item_search):
#     txtsearch = None
#     if 'item_search' in request.GET: # للتحقق من وجود نيم  في الرابط
#         txtsearch = request.GET['search_emp'] # تغذية المتغير بالمدخلات حسب النيم
#         if txtsearch: # للتحقق أن البيانات ليست فارغة
#             all_emp = all_emp.filter(item_search__icontains=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 

def load_region(request):
    country_id = request.GET.get('countryID')
    regions = Region.objects.filter(countryID_id=country_id).order_by('name_ar')
    return JsonResponse(list(regions.values('id', 'name_ar')), safe=False)

def load_state(request):
    regionID_id = request.GET.get('regionID')
    states = States.objects.filter(regionID_id=regionID_id).order_by('name_ar')
    return JsonResponse(list(states.values('id', 'name_ar')), safe=False)

def load_city(request):
    stateID_id = request.GET.get('stateID')
    cities = Cities.objects.filter(stateID_id=stateID_id).order_by('name_ar')
    return JsonResponse(list(cities.values('id', 'name_ar')), safe=False)

def load_workSpecialty(request):
    workTradeID_id = request.GET.get('workTradeID')
    workSpecialty = WorkSpecialty.objects.filter(workTradeID_id=workTradeID_id).order_by('name_ar')
    return JsonResponse(list(workSpecialty.values('id', 'name_ar')), safe=False)

def load_branchBank(request):
    bankID_id = request.GET.get('bankID')
    branchBank = BranchBank.objects.filter(bankID_id=bankID_id).order_by('name_ar')
    return JsonResponse(list(branchBank.values('id', 'name_ar')), safe=False)

def handle_form_errors(head_form, formset, request):
    """وظيفة مساعد لمعالجة الأخطاء وعرض الرسائل المناسبة."""
    for field, errors in head_form.errors.items():
        for error in errors:
            messages.error(request, f"خطأ في نموذج Person في الحقل '{field}': {error}")
    for field, errors in formset.errors.items():
      for error in errors:
          messages.error(request, f"خطأ في نموذج Emp في الحقل '{field}': {error}")
  
@login_required 
def employee_create(request):
    if not request.user.has_perm('employee.add_qayd'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة لإنشاء القيود المحاسبية.")
        return redirect('employees')
    
    if request.method == 'POST':
      person_form = PersonForm(request.POST, request.FILES)
      emp_form = EmpForm(request.POST, request.FILES)
      if person_form.is_valid() and emp_form.is_valid():
        person = person_form.save(commit=False)
        person.created_by = request.user  # تعيين created_by فقط عند إنشاء قيد جديد
        person.save()
        emp = emp_form.save(commit=False)
        emp.companyID = Company.objects.get(id=request.session.get('current_company_id'))
        emp.personID = person
        emp.save()
        messages.success(request, 'تم إضافة موظف جديد بنجاح')
        return redirect('employees')
      else:
        # دالة عرض الأخطاء
        handle_form_errors(person_form, emp_form, request)
        # إعادة عرض النماذج مع الأخطاء
        return render(request, 'employees/employee_create.html', {
            'person_form': person_form,
            'emp_form': emp_form,
        })
    else:
        # إعداد النماذج عند طلب GET
        person_form = PersonForm()
        emp_form = EmpForm()
    context = {
       'person_form': person_form,
       'emp_form': emp_form,
    }
    return render(request, 'employees/employee_create.html', context)

def employee_reade(request, id):
  emp_id = EmployeeInfo.objects.get(id=id)
  context = {
    'employee_reade':emp_id,
  }
  return render(request, 'employees/employee_reade.html', context)

def employee_update(request, id):
  update_emp = EmployeeInfo.objects.get(id=id)
  update_person = Person.objects.get(id=update_emp.personID_id)
  update_emp_form = EmpForm(instance=update_emp)
  update_person_form = PersonForm(request.POST, request.FILES, instance=update_person)
  if request.method == 'POST':
    companyID = None
    workingStatusID = None
    contractSalary = None
    fixedExtra = None
    workStartDate = None
    workEndDate = None
    #Get Values from the form
    if 'companyID' in request.POST: companyID = request.POST['companyID']
    else: messages.error(request, 'Error in companyID')
    if 'workingStatusID' in request.POST: workingStatusID = request.POST['workingStatusID']
    else: messages.error(request, 'Error in workingStatusID')
    if 'contractSalary' in request.POST: contractSalary = request.POST['contractSalary']
    else: messages.error(request, 'Error in contractSalary')
    if 'fixedExtra' in request.POST: fixedExtra = request.POST['fixedExtra']
    else: messages.error(request, 'Error in fixedExtra')
    if 'workStartDate' in request.POST: workStartDate = request.POST['workStartDate']
    else: messages.error(request, 'Error in workStartDate')
    if 'workEndDate' in request.POST: workEndDate = request.POST['workEndDate']
    else: messages.error(request, 'Error in workEndDate')
    if update_person_form.is_valid():
      update_person_form.save()
      update_emp.companyID_id=companyID 
      update_emp.workingStatusID_id=workingStatusID
      update_emp.contractSalary=contractSalary
      update_emp.workStartDate=workStartDate
      update_emp.workEndDate=workEndDate
      update_emp.fixedExtra=fixedExtra
      messages.success(request, 'تم تحديث البيانات بنجاح') 
      return redirect('employees')
    else :      
      messages.error(request, 'خطأ في البيانات') 
      return redirect('employee_update')
  update_person_form = PersonForm(instance=update_person)
  context = {
    'employee_update':update_emp,
    'employee_update_form':update_emp_form,
    'person_update':update_person,
    'person_update_form':update_person_form,
  }
  return render(request, 'employees/employee_update.html', context)    

def employee_delete(request, id):
  if request.user.is_authenticated and not request.user.is_anonymous:
    employee_delete = EmployeeInfo.objects.get(id=id)
    if request.method == 'POST':
      employee_delete.delete()
      messages.info(request, 'تم حذف الموظف بنجاح')
      return redirect('employees')
  else:
      messages.error(request, 'الرجاء تسجيل الدخول أولاً')
  context = {
      'employee_delete':employee_delete,
  }
  return render(request, 'employees/employee_delete.html', context)

def employees(request):
  all_emp = EmployeeInfo.objects.all()
  context = {
    'all_emp': all_emp,
    'emp_form': EmpForm(),
    'person_form': PersonForm(),
    'emp_count': EmployeeInfo.objects.all(),
    'emp_workingStatus': EmployeeInfo.objects.filter(workingStatusID=1).count(),
    'age': EmployeeInfo.objects.filter(),
  }
  return render(request, 'employees/employees.html', context)


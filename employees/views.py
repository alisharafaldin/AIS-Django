from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from employees.models import *
from django.views.generic import CreateView
from .forms import EmpForm
from basicinfo.forms import PersonForm
# Create your views here.

# def search(request, item_search):
#     txtsearch = None
#     if 'item_search' in request.GET: # للتحقق من وجود نيم  في الرابط
#         txtsearch = request.GET['search_emp'] # تغذية المتغير بالمدخلات حسب النيم
#         if txtsearch: # للتحقق أن البيانات ليست فارغة
#             all_emp = all_emp.filter(item_search__icontains=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 

def new_emp(request):
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
    newPerson = PersonForm(request.POST, request.FILES)
    if newPerson.is_valid():
      newPerson.save()
      new_emp = EmpInfo(personID=newPerson.instance, companyID_id=companyID, workingStatusID_id=workingStatusID, contractSalary=contractSalary, workStartDate=workStartDate, workEndDate=workEndDate, fixedExtra=fixedExtra)
      new_emp.save()
      messages.success(request, 'تمت الإضافة بنجاح') 
      return redirect('employees')
    else :      
      messages.error(request, 'خطأ في البيانات') 
      return redirect('new_emp')
  context = {
    'emp_form': EmpForm(),
    'person_form': PersonForm(),
  }
  return render(request, 'employees/new_emp.html', context)

def view_emp(request, id):
  emp_id = EmpInfo.objects.get(id=id)
  context = {
    'view_emp':emp_id,
  }
  return render(request, 'employees/view_emp.html', context)

def update_emp(request, id):
  update_emp = EmpInfo.objects.get(id=id)
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
      return redirect('new_emp')
  update_person_form = PersonForm(instance=update_person)
  context = {
    'update_emp':update_emp,
    'update_emp_form':update_emp_form,
    'update_person':update_person,
    'update_person_form':update_person_form,
  }
  return render(request, 'employees/update_emp.html', context)
    
def delete_emp(request, id):
    if request.user.is_authenticated and not request.user.is_anonymous:
      delete_emp = EmpInfo.objects.get(id=id)
      if request.method == 'POST':
        delete_emp.delete()
        messages.info(request, 'تم حذف الموظف بنجاح')
        return redirect('qayd_all')
    else:
        messages.error(request, 'الرجاء تسجيل الدخول أولاً')
    context = {
        'delete_emp':delete_emp,
    }
    return render(request, 'employees/delete_emp.html', context)

def employees(request):
  all_emp = EmpInfo.objects.all()
  context = {
    'all_emp': all_emp,
    'emp_form': EmpForm(),
    'person_form': PersonForm(),
    'emp_count': EmpInfo.objects.all(),
    'emp_workingStatus': EmpInfo.objects.filter(workingStatusID=1).count(),
    'age': EmpInfo.objects.filter(),
  }
  return render(request, 'employees/employees.html', context)


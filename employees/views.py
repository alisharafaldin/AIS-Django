from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from employees.models import *
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required
from basicinfo.forms import BasicInfoForm, PersonForm
from basicinfo.models import BasicInfo, Persons
# from basicinfo.views import 
  #  التحقق من وجود current_company_id في الجلسة قبل استخدامه.
def is_current_company_id(request):
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'لم يتم تحديد الشركة الحالية.')
        return redirect('employees')
    
def handle_form_errors(request, *forms):
    for form in forms:
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f"{field}: {error}")

@login_required 
def employee_create(request):
    if not request.user.has_perm('employee.add_employee'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة لإضافة موظفين جدد.")
        return redirect('employees')
    
    if request.method == 'POST':
      basicInfo_form = BasicInfoForm(request.POST, request.FILES)
      person_form = PersonForm(request.POST, request.FILES)
      employee_form = EmployeeForm(request.POST, request.FILES)

      if basicInfo_form.is_valid() and person_form.is_valid() and employee_form.is_valid():
        basicInfo = basicInfo_form.save(commit=False)
        basicInfo.created_by = request.user  # تعيين created_by فقط عند إنشاء موظف جديد
        basicInfo.save()

        person = person_form.save(commit=False)
        person.basicInfoID = basicInfo
        person.save()

        #  التحقق من وجود current_company_id في الجلسة قبل استخدامه.
        current_company_id = request.session.get('current_company_id')
        if not current_company_id:
            messages.error(request, 'لم يتم تحديد الشركة الحالية.')
            return redirect('employees')
        
        employee = employee_form.save(commit=False)
        employee.companyID = get_object_or_404(Company, id=current_company_id)
        employee.personID = person
        employee.save()

        messages.success(request, f'تم إضافة موظف جديد بنجاح بإسم : {employee.personID.fullName_ar()} ')
        return redirect('employees')
      else:
        # دالة عرض الأخطاء
            handle_form_errors(request, basicInfo_form, person_form, employee_form)
            # إعادة عرض النماذج مع الأخطاء
            return render(request, 'employees/employee_create.html', {
                'basicInfo_form': basicInfo_form,
                'person_form': person_form,
                'employee_form': employee_form,
            })
    else:
        # إعداد النماذج عند طلب GET
        basicInfo_form = BasicInfoForm()
        person_form = PersonForm()
        employee_form = EmployeeForm()

    context = {
    'basicInfo_form': basicInfo_form,
    'person_form': person_form,
    'employee_form': employee_form,

    'basicInfo_label': basicInfo_form,
    'person_label': person_form,
    'employee_label': employee_form,
    }
    return render(request, 'employees/employee_create.html', context)

@login_required
def employee_reade(request, id):
  employee = Employee.objects.get(id=id)
  person = Persons.objects.get(id=employee.personID_id)
  basicInfo = BasicInfo.objects.get(id=person.basicInfoID_id)

  basicInfo_form = BasicInfoForm(request.POST, request.FILES, instance=basicInfo)
  person_form = PersonForm(request.POST, request.FILES, instance=person)
  employee_form = EmployeeForm(request.POST, request.FILES, instance=employee)

  context = {
    'basicInfo_form': basicInfo,
    'person_form': person,
    'employee_form': employee,

    'basicInfo_label': basicInfo_form,
    'person_label': person_form,
    'employee_label': employee_form,
  }
  return render(request, 'employees/employee_reade.html', context)

@login_required
def employee_update(request, id):
  if not request.user.has_perm('employee.change_employee'):
    messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة لتعديل بيانات الموظفين.")
    return redirect('employees')
  # الحصول على الكائنات المطلوبة من قاعدة البيانات
  employee = get_object_or_404(Employee, id=id)
  person = get_object_or_404(Persons, id=employee.personID_id)
  basicInfo = get_object_or_404(BasicInfo, id=person.basicInfoID_id)

  if request.method == 'POST':
      # إنشاء نماذج بالكائنات المسترجعة
      basicInfo_form = BasicInfoForm(request.POST, request.FILES, instance=basicInfo)
      person_form = PersonForm(request.POST, request.FILES, instance=person)
      employee_form = EmployeeForm(request.POST, request.FILES, instance=employee)

      if basicInfo_form.is_valid() and person_form.is_valid() and employee_form.is_valid():
          basicInfo = basicInfo_form.save(commit=False)
          basicInfo.created_by = request.user 
          basicInfo.save()

          person = person_form.save(commit=False)
          person.basicInfoID = basicInfo
          person.save()

          employee = employee_form.save(commit=False)
          employee.personID = person
          employee.owner = request.user
          employee.companyID = Company.objects.get(id=request.session.get('current_company_id'))
          employee.save()

          messages.success(request, f'تم تحديث بيانات الموظف {employee.personID.fullName_ar()}')
          return redirect('employees')
      else:
          # عرض رسائل الخطأ من النماذج
          handle_form_errors(request, basicInfo_form, person_form, employee_form)
  else:
      # إعداد النماذج عند طلب GET
      basicInfo_form = BasicInfoForm(instance=basicInfo)
      person_form = PersonForm(instance=person)
      employee_form = EmployeeForm(instance=employee)

  context = {
    'employee': employee,

    'basicInfo_form': basicInfo_form,
    'person_form': person_form,
    'employee_form': employee_form,
    
    'basicInfo_label': BasicInfoForm(),
    'person_label': PersonForm(),
    'employee_label': EmployeeForm(),   
  }
  return render(request, 'employees/employee_update.html', context)    

@login_required
def employee_delete(request, id):
  if not request.user.has_perm('employee.delete_employee'):
    messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة لحذف الموظفين.")
    return redirect('employees')
  # الحصول على الكائنات المطلوبة من قاعدة البيانات
  employee = get_object_or_404(Employee, id=id)
  person = get_object_or_404(Persons, id=employee.personID_id)
  basicInfo = get_object_or_404(BasicInfo, id=person.basicInfoID_id)

  if request.method == 'POST':
    # حذف الكائنات بالترتيب المناسب لتجنب القيود المرجعية
    basicInfo.delete()  # حذف BasicInfo أولاً

    messages.info(request, 'تم حذف الموظف وجميع البيانات المرتبطة به بنجاح.')
    return redirect('employees')
  else:
      # إنشاء نماذج بالكائنات المسترجعة
      employee_form =  EmployeeForm(instance=employee)
      person_form = PersonForm(instance=person)
      basicInfo_form = BasicInfoForm(instance=basicInfo)
      handle_form_errors(request, basicInfo_form, person_form, employee_form)
  
  context = {
      'basicInfo_label': basicInfo_form,
      'person_label': person_form,
      'employee_label': employee_form,

      'employee_form': employee,
      'basicInfo_form': basicInfo,
      'person_form': person,
  }
  return render(request, 'employees/employee_delete.html', context)

@login_required
def employees(request):
    # التحقق من الأذونات أولاً
    if not request.user.has_perm('employees.view_employeeinfo'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة للإطلاع على ملفات الموظفين.")
        return redirect('index')
    # الحصول على الشركة الحالية من جلسة المستخدم
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'الرجاء تحديد الشركة للعمل عليها.')
        return redirect('companys')
    # الحصول على القيود الخاصة بالشركة الحالية
    try:
        employees = Employee.objects.filter(companyID_id=current_company_id)
    except Employee.DoesNotExist:
        employees = []  # إذا لم يكن هناك أي كائنات، العودة إلى قائمة فارغة    
    # إعداد السياق
    context = {
        'employees': employees,
    }
    # عرض الصفحة مع البيانات
    return render(request, 'employees/employees.html', context)
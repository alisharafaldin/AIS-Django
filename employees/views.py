from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from employees.models import *
from django.views.generic import CreateView
from .forms import EmpForm
from basicinfo.forms import PersonForm
# Create your views here.


# def new_emp(request, emp_id):
#     # في حال التحقق من وجود مستخدم ولديه أي دي
#     if not request.user.is_anonymous and request.method == 'POST' and 'btnempsave' in request.POST:
#         newPerson = PersonForm(request.POST, request.FILES)
#         if newPerson.is_valid():
#             newPerson.save()

#         newemp = EmpForm(request.POST, request.FILES)
#         if newemp.is_valid():
#             newemp.save()
#             # التحقق من وجود بيانات في الصفحة
#             if request.POST['f_Name_ar'] and request.POST['s_Name_ar'] and request.POST['t_Name_ar'] and request.POST['fo_Name_ar'] and request.POST['dateOfBirth'] and request.POST['genderID'] and request.POST['nationalityID'] and request.POST['socialStatusID']:
          
#                 empprofile.save()
#                 # auth.login(request, request.user)
#                 messages.success(request, 'تم تحديث البيانات بنجاح')
#             else:
#                 messages.error(request, 'تحقق من القيم المدخلة')
#                 return redirect('index')
#             context = {
#                         'emp':EmpInfo.objects.get(id=emp_id),
#                 }
#             return render(request , 'employees/employee.html', context)
#     else:
#         return redirect('/employee/' + str(emp_id))

def search(request, item_search):
    txtsearch = None
    if 'item_search' in request.GET: # للتحقق من وجود نيم  في الرابط
        txtsearch = request.GET['search_emp'] # تغذية المتغير بالمدخلات حسب النيم
        if txtsearch: # للتحقق أن البيانات ليست فارغة
            all_emp = all_emp.filter(item_search__icontains=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 

def employees(request):
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
            # new_emp = EmpInfo( personID_id=1, companyID_id=companyID, workingStatusID_id=workingStatusID, contractSalary=contractSalary, fixedExtra=fixedExtra, workStartDate=workStartDate, workEndDate=workEndDate)
            # new_emp.save()
            messages.success(request, 'تمت الإضافة بنجاح') 
        else :      
            messages.error(request, 'خطأ في البيانات') 
    all_emp = Person.objects.all()
    context = {
        'all_emp': all_emp,
        'emp_form': EmpForm(),
        'person_form': PersonForm(),
        'emp_count': EmpInfo.objects.all(),
        'emp_workingStatus': EmpInfo.objects.filter(workingStatusID=1).count(),
        'age': EmpInfo.objects.filter(),
    }
    return render(request , 'employees/employees.html', context)

def employee(request, emp_id):
    if request.user.is_authenticated:
        context = {
            'emp':EmpInfo.objects.get(id=emp_id),
            'all_gender':Gender.objects.all(),
            'all_company':Company.objects.all(),
            'all_sponser':Sponser.objects.all(),
            'all_countrie':Countries.objects.all(),
            'all_socialstatus':SocialStatus.objects.all(),
            'all_worktrade':WorkTrade.objects.all(),
            'all_workspecialty':WorkSpecialty.objects.all(),
            'all_workingstatus':WorkingStatus.objects.all(),
            'all_bank':Bank.objects.all(),
        }
        return render(request , 'employees/employee.html', context)
    else:
        messages.error(request, 'الرجاء تسجيل الدخول لعرض بيانات الموظف')
    return redirect('employees')

def update(request, id):
    emp_id = EmpInfo.objects.get(id=id)
    if request.method == 'POST':
        emp_save = EmpForm(request.POST, request.FILES, instance=emp_id)
        if emp_save.is_valid():
            emp_save.save()
            messages.success(request, 'تمت تحديث البيانات بنجاح')
            return redirect('employees')
    else:
        emp_save = EmpForm(instance=emp_id)
    context = {
        'emp_form':emp_save,
        'emp':emp_id,
    }
    return render(request, 'employees/update_emp.html', context)

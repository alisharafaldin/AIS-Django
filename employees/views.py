from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from employees.models import *
from django.views.generic import CreateView
from .forms import EmpForm
# Create your views here.

def generalsettings(request):
    return render(request , 'employees/generalsettings.html')

def countrie(request):
    if request.method == 'POST' and 'btnsave' in request.POST:
        new_countrie = Countries()
        new_countrie.countryName_en = request.POST['countryName_en']
        new_countrie.countryName_ar = request.POST['countryName_ar']
        new_countrie.code = request.POST['code']
        new_countrie.callKey = request.POST['callKey']
        new_countrie.nationality = request.POST['nationality']
        new_countrie.save()# يجب حفظ الطلب أولاً ليتم إضافة التفاصيل
        messages.success(request, 'تمت إضافة دولة جديد بنجاح')
    context = {'all_countrie':Countries.objects.all()}
    return render(request, 'employees/countries.html', context)

def delete_countrie(request, countrie_id):
    if request.user.is_authenticated and not request.user.is_anonymous and countrie_id:
        countrie = Countries.objects.get(id=countrie_id)
        countrie.delete()
        messages.error(request, 'تم حذف بيانات الدولة')
    else:
        messages.error(request, 'الرجاء تسجيل الدخول')
    return redirect('countrie')

def edit_countrie(request, countrie_id):
    if request.user.is_authenticated and not request.user.is_anonymous and countrie_id:
        countrie = Countries.objects.get(id=countrie_id)
        context = {
            'countryName_ar':countrie.countryName_ar,
            'countryName_en':countrie.countryName_en,
        }
        messages.success(request, 'تمت تحديث البيانات بنجاح')
        return render(request , 'employees/countries.html', context) 

def gender(request): 
    context = {
        'all_gender':Gender.objects.all()
    }
    return render(request , 'employees/gender.html',context) 

def add_gender(request): 
    if request.method == 'POST' and request.POST['gender_ar'] and request.POST['gender_en']:
        if 'btnsave' in request.POST:
            new_gender = Gender()
            new_gender.gender_ar = request.POST['gender_ar']
            new_gender.gender_en = request.POST['gender_en']
            new_gender.save()
            messages.success(request, 'تمت الإضافة بنجاح')
    return redirect('gender') 

def edit_gender(request, gender_id):
    if  request.user.is_authenticated and not request.user.is_anonymous and gender_id:
        gender = Gender.objects.get(id=gender_id)
        if request.method == 'POST' and 'btneditsave' in request.POST :
            if request.POST['gender_ar'] and request.POST['gender_en']:
                gender.gender_ar = request.POST['gender_ar']
                gender.gender_en = request.POST['gender_en']
                gender.save()
                messages.success(request, 'تمت تحديث البيانات بنجاح')
        else:
            context = {
                'gender_ar':gender.gender_ar,
                'gender_en':gender.gender_en,
                'all_gender':Gender.objects.all(),
            }
            return render(request , 'employees/gender.html', context) 
    messages.error(request, 'الرجاء تسجيل الدخول')

def delete_gender(request, gender_id):
    if request.user.is_authenticated and not request.user.is_anonymous and gender_id:
        gender = Gender.objects.get(id=gender_id)
        gender.delete()
    else:
        messages.error(request, 'الرجاء تسجيل الدخول')
    return redirect('gender') 

def employees(request):
    if request.method == 'POST':
        add_emp = EmpForm(request.POST, request.FILES)
        if add_emp.is_valid():
            add_emp.save()
        messages.success(request, 'تمت الإضافة بنجاح')       
    all_emp = EmpInfo.objects.all()
    # Start Search
    txtsearch = None
    if 'search_emp' in request.GET: # للتحقق من وجود نيم  في الرابط
        txtsearch = request.GET['search_emp'] # تغذية المتغير بالمدخلات حسب النيم
        if txtsearch: # للتحقق أن البيانات ليست فارغة
            all_emp = all_emp.filter(f_Name_ar__icontains=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 
    if 'search_iqama' in request.GET: # للتحقق من وجود نيم  في الرابط
        txtsearch = request.GET['search_iqama'] # تغذية المتغير بالمدخلات حسب النيم
        if txtsearch: # للتحقق أن البيانات ليست فارغة
            all_emp = all_emp.filter(iqamaNumber__icontains=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 
    if 'search_border' in request.GET: # للتحقق من وجود نيم  في الرابط
        txtsearch = request.GET['search_border'] # تغذية المتغير بالمدخلات حسب النيم
        if txtsearch: # للتحقق أن البيانات ليست فارغة
            all_emp = all_emp.filter(borderNumber__icontains=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 
    # if 'search_company' in request.GET: # للتحقق من وجود نيم  في الرابط
    #     txtsearch = request.GET['search_company'] # تغذية المتغير بالمدخلات حسب النيم
    #     if txtsearch: # للتحقق أن البيانات ليست فارغة
    #         all_emp = all_emp.filter(companyID__icontains=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 
    context = {
        'all_emp': all_emp,
        'emp_form': EmpForm(),
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
    else:
        emp_save = EmpForm(instance=emp_id)
    context = {
        'emp_form':emp_save,
        'emp':emp_id,
    }
    return render(request, 'employees/update_emp.html', context)

def emp_profile(request, emp_id):
    # في حال التحقق من وجود مستخدم ولديه أي دي
    if not request.user.is_anonymous and request.method == 'POST' and 'btnempsave' in request.POST:
            empprofile = EmpInfo.objects.get(id=request.id)
            # التحقق من وجود بيانات في الصفحة
            if request.POST['f_Name_ar'] and request.POST['s_Name_ar'] and request.POST['t_Name_ar'] and request.POST['fo_Name_ar'] and request.POST['f_Name_en'] and request.POST['s_Name_en'] and request.POST['t_Name_en'] and request.POST['fo_Name_en'] and request.POST['dateOfBirth'] and request.POST['genderID'] and request.POST['nationalityID'] and request.POST['socialStatusID'] and request.POST['passportNumber'] and request.POST['passportExpiryDate'] and request.POST['enteryDate'] and request.POST['borderNumber'] and request.POST['businessOfficeNumber'] and request.POST['visaNumber'] and request.POST['sponserID'] and request.POST['companyID'] and request.POST['iqamaNumber'] and request.POST['iqamaReleaseDate'] and request.POST['iqamaExpiredDate'] and request.POST['medicalInsuranceExpirDate'] and request.POST['workStartingDate'] and request.POST['workTradeID'] and request.POST['workSpecialtyID'] and request.POST['workingStatusID'] and request.POST['salaryInsurance'] and request.POST['contractSalary'] and request.POST['fixedExtra'] and request.POST['endDateOfService'] and request.POST['bankID'] and request.POST['accountNumber'] and request.POST['mobileNumber'] and request.POST['medicalInsurance'] and request.POST['muqeemCopy'] and request.POST['coronaCheck'] and request.POST['tawaklna'] and request.POST['sahaty'] and request.POST['emp_Photo'] and request.POST['documentLink'] and request.POST['notes']:
                empprofile.f_Name_ar = request.POST['f_Name_ar']
                empprofile.s_Name_ar = request.POST['s_Name_ar']
                empprofile.t_Name_ar = request.POST['t_Name_ar']
                empprofile.fo_Name_ar = request.POST['fo_Name_ar']
                empprofile.f_Name_en = request.POST['f_Name_en']
                empprofile.s_Name_en = request.POST['s_Name_en']
                empprofile.t_Name_en = request.POST['t_Name_en']
                empprofile.fo_Name_en = request.POST['fo_Name_en']
                empprofile.dateOfBirth = request.POST['dateOfBirth']
                empprofile.genderID = request.POST['genderID']
                empprofile.nationalityID = request.POST['nationalityID']
                empprofile.socialStatusID = request.POST['socialStatusID']
                empprofile.passportNumber = request.POST['passportNumber']
                empprofile.passportExpiryDate = request.POST['passportExpiryDate']
                empprofile.enteryDate = request.POST['enteryDate']
                empprofile.borderNumber = request.POST['borderNumber']
                empprofile.businessOfficeNumber = request.POST['businessOfficeNumber']
                empprofile.visaNumber = request.POST['visaNumber']
                empprofile.sponserID = request.POST['sponserID']
                empprofile.companyID = request.POST['companyID']
                empprofile.iqamaNumber = request.POST['iqamaNumber']
                empprofile.iqamaReleaseDate = request.POST['iqamaReleaseDate']
                empprofile.iqamaExpiredDate = request.POST['iqamaExpiredDate']
                empprofile.medicalInsuranceExpirDate = request.POST['medicalInsuranceExpirDate']
                empprofile.workStartingDate = request.POST['workStartingDate']
                empprofile.workTradeID = request.POST['workTradeID']
                empprofile.workSpecialtyID = request.POST['workSpecialtyID']
                empprofile.workingStatusID = request.POST['workingStatusID']
                empprofile.salaryInsurance = request.POST['salaryInsurance']
                empprofile.contractSalary = request.POST['contractSalary']
                empprofile.fixedExtra = request.POST['fixedExtra']
                empprofile.endDateOfService = request.POST['endDateOfService']
                empprofile.bankID = request.POST['bankID']
                empprofile.accountNumber = request.POST['accountNumber']
                empprofile.mobileNumber = request.POST['mobileNumber']
                empprofile.medicalInsurance = request.POST['medicalInsurance']
                empprofile.muqeemCopy = request.POST['muqeemCopy']
                empprofile.coronaCheck = request.POST['coronaCheck']
                empprofile.tawaklna = request.POST['tawaklna']
                empprofile.sahaty = request.POST['sahaty']
                empprofile.emp_Photo = request.POST['emp_Photo']
                empprofile.documentLink = request.POST['documentLink']
                empprofile.notes = request.POST['notes']
                empprofile.save()
                # auth.login(request, request.user)
                messages.success(request, 'تم تحديث البيانات بنجاح')
            else:
                messages.error(request, 'تحقق من القيم المدخلة')
                return redirect('index')
            context = {
                        'emp':EmpInfo.objects.get(id=emp_id),
                       
                }
            return render(request , 'employees/employee.html', context)
    else:
        return redirect('/employee/' + str(emp_id))

def sponser(request): 
    context = {
        'all_sponser':Sponser.objects.all(),
        'all_company':Company.objects.all(),
    }
    return render(request, 'employees/sponser.html', context) 

def add_sponser(request): 
    new_sponser = Sponser()
    new_sponser.sponsName = request.POST['sponsName']
    new_sponser.companyID = request.POST['companyID']
    new_sponser.save()
    messages.success(request, 'تمت الإضافة بنجاح')
    return redirect('sponser') 


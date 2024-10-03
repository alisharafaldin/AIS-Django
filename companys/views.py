from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from basicinfo.models import BasicInfo, LegalPersons
from .models import Company, CompanyUser, JobTitle
from basicinfo.forms import BasicInfoForm, LegalPersonsForm
from .forms import CompanyForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# دوال لإنشاء وتحديث وقراءة وحذف القيود المحاسبية
def handle_form_errors(head_form, request):
    """وظيفة مساعد لمعالجة الأخطاء وعرض الرسائل المناسبة."""
    for field, errors in head_form.errors.items():
        for error in errors:
            messages.error(request, f"خطأ في النموذج في الحقل '{field}': {error}")

@login_required
def company_create(request):
  if request.method == 'POST':
    basicInfo_Form = BasicInfoForm(request.POST, request.FILES)
    legalPerson_Form = LegalPersonsForm(request.POST, request.FILES)
    company_form = CompanyForm(request.POST, request.FILES)

    try:
        job_title_admin = JobTitle.objects.get(id=1)
    except JobTitle.DoesNotExist:
        messages.error(request, 'JobTitle with ID does not exist.')
        return redirect('company_create')
        
    if basicInfo_Form.is_valid() and legalPerson_Form.is_valid() and company_form.is_valid():
      basicInfo = basicInfo_Form.save(commit=False)
      basicInfo.created_by = request.user 
      basicInfo.save()

      legalPerson = legalPerson_Form.save(commit=False)
      legalPerson.basicInfoID = basicInfo
      legalPerson.save()
      
      company = company_form.save(commit=False)
      company.legalPersonID = legalPerson
      company.owner = request.user
      company.save()
      # إنشاء اشتراك للمستخدم الحالي كمدير للشركة
      CompanyUser.objects.create(userID=request.user, companyID=company, jobTitleID=job_title_admin)     
      messages.success(request, 'تم إنشاء شركة بنجاح') 
      return redirect('companys')
    else :      
      handle_form_errors(basicInfo_Form, request)
      handle_form_errors(legalPerson_Form, request)
      handle_form_errors(company_form, request)
      return redirect('company_create')
  context = {
    'basicInfo_form': BasicInfoForm(),
    'legalPerson_form': LegalPersonsForm(),
    'company_form': CompanyForm(),

    'basicInfo_label': BasicInfoForm(),
    'legalPerson_label': LegalPersonsForm(),
    'company_label': CompanyForm(),
    
  }
  return render(request, 'companys/company_create.html', context)

@login_required
def company_reade(request, id):
    company = get_object_or_404(Company, id=id)
    legalPerson = get_object_or_404(LegalPersons, id=company.legalPersonID_id)
    basicInfo = get_object_or_404(BasicInfo, id=legalPerson.basicInfoID_id)

    company_form = CompanyForm(instance=company)
    legalPerson_form = LegalPersonsForm(instance=legalPerson)
    basicInfo_form = BasicInfoForm(instance=basicInfo)

    context = {
        'basicInfo_label': basicInfo_form,
        'legalPerson_label': legalPerson_form,
        'company_label': company_form,

        'company_form': company,
        'basicInfo_form': basicInfo,
        'legalPerson_form': legalPerson,
    }
    return render(request, 'companys/company_reade.html', context)

@login_required
def company_update(request, id):
  # الحصول على الكائنات المطلوبة من قاعدة البيانات
  company_id = get_object_or_404(Company, id=id)
  legalPerson_id = get_object_or_404(LegalPersons, id=company_id.legalPersonID_id)
  basicInfo_id = get_object_or_404(BasicInfo, id=legalPerson_id.basicInfoID_id)

  if request.method == 'POST':
    # إنشاء نماذج بالكائنات المسترجعة
    basicInfo_form = BasicInfoForm(request.POST, request.FILES, instance=basicInfo_id)
    legalPerson_form = LegalPersonsForm(request.POST, request.FILES, instance=legalPerson_id)
    company_form = CompanyForm(request.POST, request.FILES, instance=company_id)
    
      # تحديث البيانات وعرض رسالة تأكيد
    if basicInfo_form.is_valid() and legalPerson_form.is_valid() and company_form.is_valid():
      basicInfo = basicInfo_form.save(commit=False)
      basicInfo.created_by = request.user 
      basicInfo.save()

      legalPerson = legalPerson_form.save(commit=False)
      legalPerson.basicInfoID = basicInfo
      legalPerson.save()
      
      company = company_form.save(commit=False)
      company.legalPersonID = legalPerson
      company.owner = request.user
      company.save()

      messages.success(request, 'تم إنشاء شركة بنجاح') 
      return redirect('companys')
    else :      
      # عرض رسائل الخطأ من النماذج
      handle_form_errors(basicInfo_form, request)
      handle_form_errors(legalPerson_form, request)
      handle_form_errors(company_form, request)
      return redirect('company_update')
  # إنشاء نماذج بالكائنات المسترجعة
  basicInfo_form = BasicInfoForm(instance=basicInfo_id)
  legalPerson_form = LegalPersonsForm(instance=legalPerson_id)
  company_form = CompanyForm(instance=company_id)

  context = {
    'company_id': company_id,

    'basicInfo_form': basicInfo_form,
    'legalPerson_form': legalPerson_form,
    'company_form': company_form,
    
    'basicInfo_label': BasicInfoForm(),
    'legalPerson_label': LegalPersonsForm(),
    'company_label': CompanyForm(),   
  }
  return render(request, 'companys/company_update.html', context)    

@login_required
def company_delete(request, id):
  # الحصول على الكائنات المطلوبة من قاعدة البيانات
  company = get_object_or_404(Company, id=id)
  legalPerson = get_object_or_404(LegalPersons, id=company.legalPersonID_id)
  basicInfo = get_object_or_404(BasicInfo, id=legalPerson.basicInfoID_id)

  # إنشاء نماذج بالكائنات المسترجعة
  company_form = CompanyForm(instance=company)
  legalPerson_form = LegalPersonsForm(instance=legalPerson)
  basicInfo_form = BasicInfoForm(instance=basicInfo)

  if request.method == 'POST':
    # حذف الكائن وإضافة رسالة نجاح
    basicInfo.delete()
    messages.info(request, 'تم حذف الشركة بنجاح')
    return redirect('companys')
  else:
      handle_form_errors(basicInfo_form, request)
      handle_form_errors(legalPerson_form, request)
      handle_form_errors(company_form, request)
  
  context = {
      'basicInfo_label': basicInfo_form,
      'legalPerson_label': legalPerson_form,
      'company_label': company_form,

      'company_form': company,
      'basicInfo_form': basicInfo,
      'legalPerson_form': legalPerson,
  }
  return render(request, 'companys/company_delete.html', context)

@login_required
def companys(request):
  user_companys = CompanyUser.objects.filter(userID=request.user).values_list('companyID', flat=True)
  companys = Company.objects.filter(id__in=user_companys, includeInInAccountingRecords=True)
  context = {
    'companys': companys,
  }
  return render(request, 'companys/companys.html', context)

#إعداد عرض لتبديل الشركة
@login_required
def switch_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    # تحقق إذا كان المستخدم ينتمي للشركة
    if CompanyUser.objects.filter(userID=request.user, companyID=company).exists():
        request.session['current_company_id'] = company.id
        request.session['current_company_name'] = company.legalPersonID.name_ar
        messages.success(request, f'تم بدء العمل في : {company.legalPersonID.name_ar}')
        return redirect('index')  # 
    else:
        messages.error(request, 'الشركة غير موجودة أو ليس لديك صلاحيات الوصول إليها.')
    return redirect('companys')

#إضافة معلومات الشركة الحالية إلى الجلسة
class CompanyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            company_id = request.session.get('current_company_id')
            if company_id:
                try:
                    request.current_company = CompanyUser.objects.get(id=company_id, userID=request.user)
                except Company.DoesNotExist:
                    request.current_company = None
            else:
                request.current_company = None
        response = self.get_response(request)
        return response
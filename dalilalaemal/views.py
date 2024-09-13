from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from basicinfo.models import BusinessScope, Cities, BasicInfo, LegalPersons
from basicinfo.forms import InvoiceSearchForm, BasicInfoForm, BasicInfoForm, LegalPersonsForm
from django.contrib.auth.decorators import login_required
from companys.models import Company, CompanyUser, JobTitle
from django.contrib import messages
from companys.forms import CompanyForm

def handle_form_errors(head_form, request):
    """وظيفة مساعد لمعالجة الأخطاء وعرض الرسائل المناسبة."""
    for field, errors in head_form.errors.items():
        for error in errors:
            messages.error(request, f"خطأ في النموذج في الحقل '{field}': {error}")

@login_required
def create(request):
  if request.method == 'POST':
    basicInfo_Form = BasicInfoForm(request.POST, request.FILES)
    legalPerson_Form = LegalPersonsForm(request.POST, request.FILES)
    company_form = CompanyForm(request.POST, request.FILES)
    try:
        job_title_admin = JobTitle.objects.get(id=1)
    except JobTitle.DoesNotExist:
        messages.error(request, 'JobTitle with ID does not exist.')
        return redirect('create')

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
      return redirect('dalils')
    else :      
      handle_form_errors(basicInfo_Form, request)
      handle_form_errors(legalPerson_Form, request)
      handle_form_errors(company_form, request)
      return redirect('create')
  context = {
    'basicInfo_form': BasicInfoForm(),
    'legalPerson_form': LegalPersonsForm(),
    'company_form': CompanyForm(),

    'basicInfo_label': BasicInfoForm(),
    'legalPerson_label': LegalPersonsForm(),
    'company_label': CompanyForm(),
    
  }
  return render(request, 'dalilalaemal/dalil_create.html', context)

@login_required
def update(request, id):
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
      return redirect('dalils')
    else :      
      # عرض رسائل الخطأ من النماذج
      handle_form_errors(basicInfo_form, request)
      handle_form_errors(legalPerson_form, request)
      handle_form_errors(company_form, request)
      return redirect('update')
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
  return render(request, 'dalilalaemal/dalil_update.html', context)    

# -------------------- دليل الأعمال --------------------

# @login_required
def dalil_home(request):
    company = Company.objects.filter(includeInDalilAlaemal=True).count()-1
    businessScope = BusinessScope.objects.filter(legalpersons__company__isnull=False).distinct().count()
    cities = Cities.objects.filter(basicInfo__legalpersons__company__isnull=False).distinct().count()

    context = {
        'company': company,
        'businessScope': businessScope,
        'cities': cities
    }
    return render(request, 'dalilalaemal/dalil_home.html', context)

# @login_required
def dalilalaemal_single(request, id):
    company = Company.objects.get(id=id)
    context = {
        'company': company,
    }
    return render(request, 'dalilalaemal/dalilalaemal_single.html', context)

# @login_required
def dalils_business_Scope(request):
    business_scopes = BusinessScope.objects.filter(legalpersons__company__isnull=False).distinct()
    scope_data = [
        (scope.id, scope.logo, scope.name_ar, scope.legalpersons.filter(company__isnull=False).count())
        for scope in business_scopes
    ]
    # قم بترتيب القائمة تنازلياً حسب العدد
    sorted_scope_data = sorted(scope_data, key=lambda x: x[3], reverse=True)
    context = {
        'scope_data': sorted_scope_data
    }
    return render(request, 'dalilalaemal/dalils_business_Scope.html', context)

# @login_required
def dalilalaemal_search(request):
    # الحصول على معايير البحث من الطلب
    search_cityID = request.GET.get('cityID', None)
    search_companyID = request.GET.get('companyID', '')
    search_businessScopeID = request.GET.get('businessScopeID', '')
    company_query = Company.objects.filter(includeInDalilAlaemal=True).order_by('-id')
    # استعلام الفواتير بين تاريخين
    if search_cityID:
        company_query = company_query.filter(legalPersonID__basicInfoID__cityID=search_cityID)
    if search_businessScopeID:
        company_query = company_query.filter(legalPersonID__businessScopeID=search_businessScopeID)
    if search_companyID:
        company_query = company_query.filter(id=search_companyID)
    # تحويل search_cityID إلى عدد صحيح إذا كانت القيمة ليست فارغة
    try:
        if search_cityID and search_cityID != 'None':        
            search_cityID = int(search_cityID)
        else:
            search_cityID = ""
    except ValueError:
        search_cityID = None

    # الحصول على جميع المدن
    cities = Cities.objects.all()

    # البحث عن المدينة المحددة
    selected_city_name = None
    if search_cityID:
        selected_city = Cities.objects.filter(id=search_cityID).first()
        if selected_city:
            selected_city_name = selected_city.name_ar
    
    # إعداد السياق
    context = {
        'companys': company_query,
        'search_form': InvoiceSearchForm(request.GET),
        'search_cityID':search_cityID,
        'selected_city_name': selected_city_name,
        'search_businessScopeID':search_businessScopeID,
        'businessScope':BusinessScope.objects.filter(legalpersons__company__isnull=False).distinct(),
        'cities': Cities.objects.filter(basicInfo__legalpersons__company__isnull=False).distinct(),
    }

    # عرض الصفحة مع البيانات
    return render(request, 'dalilalaemal/dalilalaemal_search.html', context)

# @login_required
def dalils(request):
    company_query = Company.objects.filter(includeInDalilAlaemal=True).order_by('-id')
    context = {
        'companys': company_query,
        'search_form': InvoiceSearchForm(request.GET),
        'businessScope':BusinessScope.objects.filter(legalpersons__company__isnull=False).distinct(),
        'cities': Cities.objects.filter(basicInfo__legalpersons__company__isnull=False).distinct(),
    }
    # عرض الصفحة مع البيانات
    return render(request, 'dalilalaemal/dalils.html', context)

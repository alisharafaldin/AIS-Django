from django.contrib import messages
from companys.forms import CompanyForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from companys.models import Company, CompanyUser, JobTitle
from django.shortcuts import render, redirect, get_object_or_404
from basicinfo.models import BusinessScope, Cities, BasicInfo, LegalPersons
from basicinfo.forms import SetComboBox, BasicInfoForm, BasicInfoForm, LegalPersonsForm

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
      return redirect('dalil_home')
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
        # 'search_cityID' = request.GET.get('cityID', None),

    context = {
        'company': company,
        'businessScope': businessScope,
        'cities': cities,
        'search_cityID': request.GET.get('cityID', None),
        'cities2': Cities.objects.filter(basicInfo__legalpersons__company__isnull=False).distinct(),
    }
    return render(request, 'dalilalaemal/dalil_home.html', context)

# @login_required
def dalil_single(request, id):
    company = Company.objects.get(id=id)
    context = {
        'company': company,
    }
    return render(request, 'dalilalaemal/dalil_single.html', context)

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
def dalil_cities(request):
    company_query = Company.objects.filter(includeInDalilAlaemal=True)
    cities = Cities.objects.filter(basicInfo__legalpersons__company__in=company_query).distinct()
    scope_data = [
        (scope.id, scope.logo, scope.name_ar, scope.basicInfo.filter(legalpersons__company__isnull=False).count())
        for scope in cities
    ]

    # قم بترتيب القائمة تنازلياً حسب العدد
    sorted_scope_data = sorted(scope_data, key=lambda x: x[3], reverse=True)
    context = {
        'scope_data': sorted_scope_data
    }
    return render(request, 'dalilalaemal/dalil_cities.html', context)

# @login_required
def dalil_search(request):
    # الحصول على معايير البحث من الطلب
    search_cityID = request.GET.get('cityID', None)
    search_companyID = request.GET.get('companyID', '')
    search_businessScopeID = request.GET.get('businessScopeID', '')
    # الحصول على المدخل النصي من المستخدم وتجاهل المسافات
    search_name = request.GET.get('search_name', '')  # القيمة الافتراضية سلسلة فارغة إذا لم يتم إدخال شيء
    # إعداد التعبير النمطي لاستبدال "ا" و"أ" وكذلك "ة" و"ه"
    search_regex = search_name.replace('أ', '[ا|أ]').replace('ا', '[أ|ا]').replace('ة', '[ة|ه]').replace('ه', '[ة|ه]')
    # إزالة المسافات في نهاية النص إذا كانت موجودة
    search_regex = search_regex.strip()

    # استعلام الشركات
    company_query = Company.objects.filter(includeInDalilAlaemal=True).order_by('-id')
    
    if search_name:
        # تنفيذ البحث باستخدام iregex لتجاهل حالة الحروف
        company_query = company_query.filter(legalPersonID__name_ar__iregex=search_regex)
    
    # تصفية الشركات بناءً على المدينة
    if search_cityID:
        company_query = company_query.filter(legalPersonID__basicInfoID__cityID=search_cityID)
    
    # تصفية الشركات بناءً على المجال
    if search_businessScopeID:
        company_query = company_query.filter(legalPersonID__businessScopeID=search_businessScopeID)
    
    # تصفية الشركات بناءً على معرف الشركة
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

    # البحث عن المدينة المحددة
    selected_city_name = None
    if search_cityID:
        selected_city = Cities.objects.filter(id=search_cityID).first()
        if selected_city:
            selected_city_name = selected_city.name_ar

    # البحث عن المجال المحدد
    selected_businessScope_name = None
    if search_businessScopeID:
        selected_businessScope = BusinessScope.objects.filter(id=search_businessScopeID).first()
        if selected_businessScope:
            selected_businessScope_name = selected_businessScope.name_ar

    # تصفية المجالات بناءً على المدينة المختارة
    if search_cityID:
        business_scopes = BusinessScope.objects.filter(
            legalpersons__basicInfoID__cityID=search_cityID, legalpersons__company__isnull=False).distinct()
    else:
        business_scopes = BusinessScope.objects.filter(legalpersons__company__isnull=False).distinct()

    # إعداد بيانات المجالات
    if search_cityID:
        scope_business = [
            (scope.id, scope.logo, scope.name_ar, scope.legalpersons.filter(company__isnull=False,basicInfoID__cityID=search_cityID).count())
            for scope in business_scopes
        ]
    else:
        scope_business = [
            (scope.id, scope.logo, scope.name_ar, scope.legalpersons.filter(company__isnull=False).count())
            for scope in business_scopes
        ]
    
    # ترتيب القائمة تنازلياً حسب العدد
    sorted_scope_business = sorted(scope_business, key=lambda x: x[3], reverse=True)

    # إذا كان الطلب AJAX، أعد فقط المحتوى المطلوب
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'dalilalaemal/dalil_search_ajax.html', {'companys': company_query})
    
    # إعداد السياق
    context = {
        'companys': company_query,
        'search_form': SetComboBox(request.GET),
        'search_cityID': search_cityID,
        'search_name': search_name,
        'selected_city_name': selected_city_name,
        'selected_businessScope_name':selected_businessScope_name,
        'search_businessScopeID': search_businessScopeID,
        'businessScope': sorted_scope_business,
        'cities': Cities.objects.filter(basicInfo__legalpersons__company__isnull=False).distinct(),
    }
    return render(request, 'dalilalaemal/dalil_search.html', context)

# @login_required
def dalils(request):
   # الحصول على قائمة معرفات الشركات التي تم تحميلها سابقًا
    loaded_ids = request.GET.getlist('loaded_ids[]', [])
    company_query = Company.objects.filter(includeInDalilAlaemal=True).exclude(id__in=loaded_ids).order_by('?')
    
    # إعداد عرض المزيد البادئة وعدد العناصر
    paginator = Paginator(company_query, 3)  # تقسيم النتائج لـ 3 عناصر في الصفحة الواحدة
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # إذا كان الطلب AJAX، قم بإرجاع HTML القالب الفرعي مع الحالة
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('dalilalaemal/dalil_dalils_card.html', {'companys': page_obj})
        results_list = [company.id for company in page_obj.object_list]  # احصل على معرفات النتائج الجديدة
        return JsonResponse({
            'html': html,
            'has_next': page_obj.has_next(),
            'loaded_ids': results_list  # أضف المعرفات إلى البيانات المستجيبة
        })
    
    context = {
        'companys': page_obj,
        'search_form': SetComboBox(request.GET),
        'businessScope':BusinessScope.objects.filter(legalpersons__company__isnull=False).distinct(),
        'cities': Cities.objects.filter(basicInfo__legalpersons__company__isnull=False).distinct(),
        'page_obj': page_obj
    }
    # عرض الصفحة مع البيانات
    return render(request, 'dalilalaemal/dalil_dalils.html', context)

def the_four_freedoms_view(request):
    return render(request, 'dalilalaemal/TheFourFreedoms.html')
 
def add_dalil(request):
    if not request.user.is_authenticated:
        # عرض رسالة خطأ في حال لم يكن المستخدم مسجلاً للدخول
        messages.error(request, 'الرجاء تسجيل الدخول لإضافة عمل جديد إلى الدليل.')
        return redirect('signin')  # إعادة توجيه المستخدم إلى صفحة تسجيل الدخول
    return redirect('https://docs.google.com/forms/d/e/1FAIpQLSdIJcsZD9iOsvD9QLYo4mSN-hWxQkZTqhJd1OzPl49qQ4XTzA/viewform')

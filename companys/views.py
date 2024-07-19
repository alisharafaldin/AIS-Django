from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Company, CompanyUser, JobTitle
from .forms import CompanyForm
from profiles.models import UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.

# دوال لإنشاء وتحديث وقراءة وحذف القيود المحاسبية
def handle_form_errors(head_form, request):
    """وظيفة مساعد لمعالجة الأخطاء وعرض الرسائل المناسبة."""
    for field, errors in head_form.errors.items():
        for error in errors:
            messages.error(request, f"خطأ في نموذج الرأس في الحقل '{field}': {error}")

def company_create(request):
  if request.method == 'POST':
    company_form = CompanyForm(request.POST, request.FILES)

    try:
        job_title_admin = JobTitle.objects.get(id=1)
    except JobTitle.DoesNotExist:
        messages.error(request, 'JobTitle with ID 1 does not exist.')
        return redirect('company_create')
        
    if company_form.is_valid():
      company = company_form.save(commit=False)
      company.owner = request.user
      company.save()
      # إنشاء اشتراك للمستخدم الحالي كمدير للشركة
      CompanyUser.objects.create(userID=request.user, companyID=company, jobTitleID=job_title_admin)     
      messages.success(request, 'تم إنشاء شركة بنجاح') 
      return redirect('companys')
    else :      
      handle_form_errors(company_form, request)
      return redirect('company_create')
  context = {
    'company_form': CompanyForm(),
  }
  return render(request, 'companys/company_create.html', context)

def company_reade(request, id):
  company_id = Company.objects.get(id=id)
  company_form = CompanyForm(instance=company_id)
  context = {
    'company_reade':company_id,
    'company_form':company_form,
  }
  return render(request, 'companys/company_reade.html', context)

def company_update(request, id):
  company_id= Company.objects.get(id=id)
  company_form = CompanyForm(request.POST, request.FILES, instance=company_id)
  if request.method == 'POST':
      if company_form.is_valid():
        company_form.save()
        messages.success(request, 'تم تحديث البيانات بنجاح') 
        return redirect('companys')
      else :      
        handle_form_errors(company_form, request)
  company_form = CompanyForm(instance=company_id)
  context = {
    'company_id':company_id,
    'company_form':company_form,
  }
  return render(request, 'companys/company_update.html', context)    

def company_delete(request, id):
  if request.user.is_authenticated and not request.user.is_anonymous:
    company_delete = Company.objects.get(id=id)
    if request.method == 'POST':
      company_delete.delete()
      messages.info(request, 'تم حذف الشركة بنجاح')
      return redirect('companys')
  else:
      messages.error(request, 'يوجد خطأ في البيانات')
  context = {
      'company_delete':company_delete,
  }
  return render(request, 'companys/company_delete.html', context)

def companys(request):
  user_companys = CompanyUser.objects.filter(userID=request.user).values_list('companyID', flat=True)
  companys = Company.objects.filter(id__in=user_companys)
  context = {
    'companys': companys,
  }
  return render(request, 'companys/companys.html', context)

#  إعداد عرض لتبديل الشركة
@login_required
def switch_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    # تحقق إذا كان المستخدم ينتمي للشركة
    if CompanyUser.objects.filter(userID=request.user, companyID=company).exists():
        request.session['current_company_id'] = company.id
        request.session['current_company_name'] = company.name_ar
        messages.success(request, f'تم بدء العمل في : {company.name_ar}')
        return redirect('qayds')  # 
    else:
        messages.error(request, 'الشركة غير موجودة أو ليس لديك صلاحيات الوصول إليها.')
    return redirect('companys')

# إضافة معلومات الشركة الحالية إلى الجلسة
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
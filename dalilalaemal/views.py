import re
import requests
from django.shortcuts import render, redirect
from companys.models import Company, CompanyUser
from django.contrib.auth.decorators import login_required
from basicinfo.forms import InvoiceSearchForm, BasicInfoForm
from basicinfo.models import BusinessScope, Cities

@login_required
def dalilalaemal_main(request):
    user_companys = CompanyUser.objects.filter(userID=request.user).values_list('companyID', flat=True)
    companys = Company.objects.filter(id__in=user_companys, includeInDalilAlaemal=True).order_by('-id')
    context = {
        'companys': companys,
        'search_form': InvoiceSearchForm(request.GET),
        'businessScope':BusinessScope.objects.all()
    }
    return render(request, 'dalilalaemal/dalilalaemal_main.html', context)

@login_required
def dalilalaemal(request):
    user_companys = CompanyUser.objects.filter(userID=request.user).values_list('companyID', flat=True)
    companys = Company.objects.filter(id__in=user_companys, includeInDalilAlaemal=True).order_by('-id')
    context = {
        'companys': companys,
        'company_form': BasicInfoForm,
        'search_form': InvoiceSearchForm(request.GET),
        'businessScope':BusinessScope.objects.all(),
        'city': Cities.objects.all()
    }
    return render(request, 'dalilalaemal/dalilalaemal.html', context)


@login_required
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

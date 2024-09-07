import re
from django.shortcuts import render, redirect
from companys.models import Company, CompanyUser
from django.contrib.auth.decorators import login_required
from basicinfo.forms import InvoiceSearchForm
# from django.contrib import messages
# from employees.models import *
# from .forms import EmpForm
# from basicinfo.forms import PersonForm
# from basicinfo.models import Person
# # Create your views here.



@login_required
def dalilalaemal(request):
    user_companys = CompanyUser.objects.filter(userID=request.user).values_list('companyID', flat=True)
    companys = Company.objects.filter(id__in=user_companys, includeInDalilAlaemal=True).order_by('-id')
    context = {
        'companys': companys,
        'search_form': InvoiceSearchForm(request.GET),
    }
    return render(request, 'dalilalaemal/dalilalaemal.html', context)

# def google_maps_location(request):
#     # استخدام تعبير عادي لاستخراج الإحداثيات
#     match = re.search(r'@(-?\d+\.\d+),(-?\d+\.\d+)', request)
#     if match:
#         latitude = float(match.group(1))
#         longitude = float(match.group(2))
#         print(latitude)
#         print(longitude)
#         return latitude, longitude

#     return None, None

@login_required
def dalilalaemal_search(request):
    # الحصول على معايير البحث من الطلب
    search_countryID = request.GET.get('countryID', '')
    search_regionID = request.GET.get('regionID', '')
    search_stateID = request.GET.get('stateID', '')
    search_cityID = request.GET.get('cityID', '')
    search_companyID = request.GET.get('companyID', '')
    search_businessScopeID = request.GET.get('businessScopeID', '')
    search_google_maps_location = request.GET.get('google_maps_location', '')

    company_query = Company.objects.filter(includeInDalilAlaemal=True).order_by('-id')

    # استعلام الفواتير بين تاريخين
    if search_countryID:
        company_query = company_query.filter(legalPersonID__basicInfoID__countryID=search_countryID)
    if search_regionID:
        company_query = company_query.filter(legalPersonID__basicInfoID__regionID=search_regionID)
    if search_stateID:
        company_query = company_query.filter(legalPersonID__basicInfoID__stateID=search_stateID)
    if search_cityID:
        company_query = company_query.filter(legalPersonID__basicInfoID__cityID=search_cityID)
    if search_businessScopeID:
        company_query = company_query.filter(legalPersonID__businessScopeID=search_businessScopeID)
    if search_companyID:
        company_query = company_query.filter(id=search_companyID)

    # إعداد السياق
    context = {
        'companys': company_query,
        'search_form': InvoiceSearchForm(request.GET),
        'businessScopeID':search_businessScopeID,
    }

    # عرض الصفحة مع البيانات
    return render(request, 'dalilalaemal/dalilalaemal_search.html', context)

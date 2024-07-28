from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from basicinfo.models import *
from django.http import JsonResponse
from basicinfo.models import Region, States, Cities, WorkSpecialty, BranchBank

# Create your views here.

def basicinfo(request):
    return render(request , 'basicinfo/basicinfo.html')

def load_region(request):
    country_id = request.GET.get('countryID')
    regions = Region.objects.filter(countryID_id=country_id).order_by('name_ar')
    return JsonResponse(list(regions.values('id', 'name_ar')), safe=False)

def load_state(request):
    regionID_id = request.GET.get('regionID')
    states = States.objects.filter(regionID_id=regionID_id).order_by('name_ar')
    return JsonResponse(list(states.values('id', 'name_ar')), safe=False)

def load_city(request):
    stateID_id = request.GET.get('stateID')
    cities = Cities.objects.filter(stateID_id=stateID_id).order_by('name_ar')
    return JsonResponse(list(cities.values('id', 'name_ar')), safe=False)

def load_workSpecialty(request):
    workTradeID_id = request.GET.get('workTradeID')
    workSpecialty = WorkSpecialty.objects.filter(workTradeID_id=workTradeID_id).order_by('name_ar')
    return JsonResponse(list(workSpecialty.values('id', 'name_ar')), safe=False)

def load_branchBank(request):
    bankID_id = request.GET.get('bankID')
    branchBank = BranchBank.objects.filter(bankID_id=bankID_id).order_by('name_ar')
    return JsonResponse(list(branchBank.values('id', 'name_ar')), safe=False)

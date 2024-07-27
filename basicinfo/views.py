from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from basicinfo.models import *
# Create your views here.

def basicinfo(request):
    return render(request , 'basicinfo/basicinfo.html')
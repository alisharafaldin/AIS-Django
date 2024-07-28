from django.shortcuts import render, redirect
from products.models import ItemDetails
from employees.models import EmployeeInfo
from shrfntod.models import Posts
from accounts.models import Qayd
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
    # الحصول على الشركة الحالية من جلسة المستخدم
    current_company_id = request.session.get('current_company_id')
    emp_list = EmployeeInfo.objects.filter(companyID_id=current_company_id)
    qayd_list = Qayd.objects.filter(companyID_id=current_company_id)

    context = {
        'emp_count': emp_list,
        'qayds' : qayd_list,
    }
    return render(request , 'pages/index.html' , context)

def about(request):
    return render(request , 'pages/about.html')
    # return HttpResponse('<h1>About Page</h1>')

def coffee(request):
    return render(request, 'pages/coffee.html')

def blog(r):
    all_postes = Posts.objects.all()
    return render(r,'pages/blog.html',{'all_postes':all_postes})
from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from employees.models import EmployeeInfo
from shrfntod.models import Posts
from accounts.models import Qayd
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
    context = {
        'products': Product.objects.all(),
        'emp_count': EmployeeInfo.objects.all(),
        'qayds' : Qayd.objects.all(),
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
from django.shortcuts import render, redirect
from employees.models import Employee
from sales.models import InvoicesSalesHead, Customers, Inventory
from purchases.models import InvoicesPurchasesHead, Suppliers
# from accounts.models import Qayd
# from cashreceipt.models import CashReceiptHead
from products.models import Items
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
    # الحصول على الشركة الحالية من جلسة المستخدم
    current_company_id = request.session.get('current_company_id')
    emp_list = Employee.objects.filter(companyID_id=current_company_id)
    # qayd_list = Qayd.objects.filter(companyID_id=current_company_id)
    customers_list = Customers.objects.filter(companyID_id=current_company_id)
    invoicesSales_list = InvoicesSalesHead.objects.filter(companyID_id=current_company_id)
    suppliers_list = Suppliers.objects.filter(companyID_id=current_company_id)
    invoicesPurchases_list = InvoicesPurchasesHead.objects.filter(companyID_id=current_company_id)
    inventory_list = Inventory.objects.filter(companyID_id=current_company_id)
    items_list = Items.objects.filter(companyID_id=current_company_id)
    # cashReceipt_list = CashReceiptHead.objects.filter(companyID_id=current_company_id)

    context = {
        'emp_count': emp_list,
        # 'qayds' : qayd_list,
        
        'customers_list':customers_list,
        'invoicesSales_list':invoicesSales_list,

        'suppliers_list':suppliers_list,
        'invoicesPurchases_list':invoicesPurchases_list,

        'inventory_list':inventory_list,
        'items_list':items_list,

        # 'cashReceipt_list':cashReceipt_list,
    }
    return render(request , 'pages/index.html' , context)

def about(request):
    return render(request , 'pages/about.html')
    # return HttpResponse('<h1>About Page</h1>')

def coffee(request):
    return render(request, 'pages/coffee.html')

# def blog(r):
#     all_postes = Posts.objects.all()
#     return render(r,'pages/blog.html',{'all_postes':all_postes})
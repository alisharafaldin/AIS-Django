# from django.shortcuts import render, redirect
# from django.contrib import messages
# from employees.models import *
# from .forms import EmpForm
# from django.contrib.auth.decorators import login_required
# from basicinfo.forms import PersonForm
# from basicinfo.models import Person
# # Create your views here.


def dalilalaemal():
    pass

# def employees(request):
#     # التحقق من الأذونات أولاً
#     if not request.user.has_perm('emplyees.view_qayd'):
#         messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة للإطلاع على ملفات الموظفين.")
#         return redirect('index')
#     # الحصول على الشركة الحالية من جلسة المستخدم
#     current_company_id = request.session.get('current_company_id')
#     if not current_company_id:
#         messages.error(request, 'الرجاء تحديد الشركة للعمل عليها.')
#         return redirect('companys')
#     # الحصول على القيود الخاصة بالشركة الحالية
#     try:
#         emp_list = EmployeeInfo.objects.filter(companyID_id=current_company_id)
#     except EmployeeInfo.DoesNotExist:
#         emp_list = []  # إذا لم يكن هناك أي كائنات، العودة إلى قائمة فارغة    
#     # إعداد السياق
#     context = {
#         'all_emغ ثp': emp_list,
#     }
#     # عرض الصفحة مع البيانات
#     return render(request, 'employees/employees.html', context)

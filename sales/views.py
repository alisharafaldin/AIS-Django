import io
from typing import Any
from django.shortcuts import render , redirect, get_object_or_404
from basicinfo.forms import BasicInfoForm, LegalPersonsForm
from basicinfo.models import BasicInfo, LegalPersons
from django.contrib import messages
from . models import Customers, InvoicesSalesHead, InvoicesSalesBody
from companys.models import Company
from . forms import CustomerForm, InvoiceHeadForm, InvoiceBodyForm, InvoiceBodyFormSet
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required

# Create your views here.

# دوال لإنشاء وتحديث وقراءة وحذف القيود المحاسبية

def handle_form_errors(head_form, request):
    """وظيفة مساعد لمعالجة الأخطاء وعرض الرسائل المناسبة."""
    for field, errors in head_form.errors.items():
        for error in errors:
            messages.error(request, f"خطأ في النموذج في الحقل '{field}': {error}")

def handle_invoice_form_errors(head_form, formset, request):
    """وظيفة مساعد لمعالجة الأخطاء وعرض الرسائل المناسبة."""
    for field, errors in head_form.errors.items():
        for error in errors:
            messages.error(request, f"خطأ في نموذج الرأس في الحقل '{field}': {error}")
    for form_index, form in enumerate(formset.forms):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f"خطأ في نموذج التفاصيل {form_index + 1} في الحقل '{field}': {error}")
    for error in formset.non_form_errors():
        messages.error(request, f"خطأ في الـ FormSet: {error}")

def calculate_totals(details_queryset):
    """ وظيفة مساعدة لعمل مجاميع القيود """
    total_d = sum(item.debit for item in details_queryset)
    total_c = sum(item.credit for item in details_queryset)
    return total_d, total_c, total_d - total_c

@login_required 
def customer_create(request):
    if not request.user.has_perm('customer.add_qayd'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة لإضافة عملاء.")
        return redirect('customers')
    
    if request.method == 'POST':
      basicInfo_form = BasicInfoForm(request.POST, request.FILES)
      legalPerson_form = LegalPersonsForm(request.POST, request.FILES)
      customer_form = CustomerForm(request.POST, request.FILES)

      if basicInfo_form.is_valid() and legalPerson_form.is_valid() and customer_form.is_valid():

        basicInfo = basicInfo_form.save(commit=False)
        basicInfo.created_by = request.user  # تعيين created_by فقط عند إنشاء قيد جديد
        basicInfo.save()

        legalPerson = legalPerson_form.save(commit=False)
        legalPerson.basicInfoID = basicInfo
        legalPerson.save()

        # التحقق من وجود current_company_id في الجلسة قبل استخدامه.
        current_company_id = request.session.get('current_company_id')
        if not current_company_id:
            messages.error(request, 'لم يتم تحديد الشركة الحالية.')
            return redirect('sales')
        
        customer = customer_form.save(commit=False)
        customer.companyID = get_object_or_404(Company, id=current_company_id)
        customer.legalPersonID = legalPerson
        customer.save()
        messages.success(request, f'تم إضافة عميل جديد بإسم : {customer.legalPersonID.name_ar}')
        return redirect('customers')
      else:
        # دالة عرض الأخطاء
        handle_form_errors(legalPerson_form, customer_form, request)
        # إعادة عرض النماذج مع الأخطاء
        return render(request, 'sales/customer_create.html', {
            'basicInfo_form': basicInfo_form,
            'legalPerson_form': legalPerson_form,
            'customer_form': customer_form,
        })
    else:
        # إعداد النماذج عند طلب GET
        basicInfo_form = BasicInfoForm()
        legalPerson_form = LegalPersonsForm()
        customer_form = CustomerForm()
    context = {
       'basicInfo_form': basicInfo_form,
       'legalPerson_form': legalPerson_form,
       'customer_form': customer_form,

       'basicInfo_label': basicInfo_form,
       'legalPerson_label': legalPerson_form,
       'customer_label': customer_form,
    }
    return render(request, 'sales/customer_create.html', context)

@login_required
def customer_reade(request, id):
    customer = get_object_or_404(Customers, id=id)
    legalPerson = get_object_or_404(LegalPersons, id=customer.legalPersonID_id)
    basicInfo = get_object_or_404(BasicInfo, id=legalPerson.basicInfoID_id)

    customer_form = CustomerForm(instance=customer)
    legalPerson_form = LegalPersonsForm(instance=legalPerson)
    basicInfo_form = BasicInfoForm(instance=basicInfo)

    context = {
        'basicInfo_label': basicInfo_form,
        'legalPerson_label': legalPerson_form,
        'customer_label': customer_form,

        'customer_form': customer,
        'basicInfo_form': basicInfo,
        'legalPerson_form': legalPerson,
    }
    return render(request, 'sales/customer_reade.html', context)

@login_required
def customer_update(request, id):
  # الحصول على الكائنات المطلوبة من قاعدة البيانات
  customer_id = get_object_or_404(Customers, id=id)
  legalPerson_id = get_object_or_404(LegalPersons, id=customer_id.legalPersonID_id)
  basicInfo_id = get_object_or_404(BasicInfo, id=legalPerson_id.basicInfoID_id)

  if request.method == 'POST':
    # إنشاء نماذج بالكائنات المسترجعة
    basicInfo_form = BasicInfoForm(request.POST, request.FILES, instance=basicInfo_id)
    legalPerson_form = LegalPersonsForm(request.POST, request.FILES, instance=legalPerson_id)
    customer_form = CustomerForm(request.POST, request.FILES, instance=customer_id)
    
      # تحديث البيانات وعرض رسالة تأكيد
    if basicInfo_form.is_valid() and legalPerson_form.is_valid() and customer_form.is_valid():
      basicInfo = basicInfo_form.save(commit=False)
      basicInfo.created_by = request.user 
      basicInfo.save()

      legalPerson = legalPerson_form.save(commit=False)
      legalPerson.basicInfoID = basicInfo
      legalPerson.save()
      
      customer = customer_form.save(commit=False)
      customer.legalPersonID = legalPerson
      customer.companyID = Company.objects.get(id=request.session.get('current_company_id'))
      customer.save()

      messages.success(request, f' تم تعديل بيانات العميل : {customer.legalPersonID.name_ar} ') 
      return redirect('customers')
    else :      
      # عرض رسائل الخطأ من النماذج
      handle_form_errors(basicInfo_form, request)
      handle_form_errors(legalPerson_form, request)
      handle_form_errors(customer_form, request)
      return redirect('customer_update')
  # إنشاء نماذج بالكائنات المسترجعة
  basicInfo_form = BasicInfoForm(instance=basicInfo_id)
  legalPerson_form = LegalPersonsForm(instance=legalPerson_id)
  customer_form = CustomerForm(instance=customer_id)

  context = {
    'customer_id': customer_id,

    'basicInfo_form': basicInfo_form,
    'legalPerson_form': legalPerson_form,
    'customer_form': customer_form,
    
    'basicInfo_label': BasicInfoForm(),
    'legalPerson_label': LegalPersonsForm(),
    'customer_label': CustomerForm(),   
  }
  return render(request, 'sales/customer_update.html', context)    

@login_required
def customer_delete(request, id):
  # الحصول على الكائنات المطلوبة من قاعدة البيانات
  customer = get_object_or_404(Customers, id=id)
  legalPerson = get_object_or_404(LegalPersons, id=customer.legalPersonID_id)
  basicInfo = get_object_or_404(BasicInfo, id=legalPerson.basicInfoID_id)

  # إنشاء نماذج بالكائنات المسترجعة
  customer_form = CustomerForm(instance=customer)
  legalPerson_form = LegalPersonsForm(instance=legalPerson)
  basicInfo_form = BasicInfoForm(instance=basicInfo)

  if request.method == 'POST':
    # حذف الكائن وإضافة رسالة نجاح
    customer.delete()
    messages.info(request, f'تم حذف العميل {customer.legalPersonID.name_ar}')
    return redirect('customers')
  else:
      handle_form_errors(basicInfo_form, request)
      handle_form_errors(legalPerson_form, request)
      handle_form_errors(customer_form, request)
  
  context = {
      'basicInfo_label': basicInfo_form,
      'legalPerson_label': legalPerson_form,
      'customer_label': customer_form,

      'customer_form': customer,
      'basicInfo_form': basicInfo,
      'legalPerson_form': legalPerson,
  }
  return render(request, 'sales/customer_delete.html', context)

def customers(request):
    # التحقق من الأذونات أولاً
    if not request.user.has_perm('emplyees.view_qayd'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة للإطلاع على ملفات الموظفين.")
        return redirect('index')
    # الحصول على الشركة الحالية من جلسة المستخدم
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'الرجاء تحديد الشركة للعمل عليها.')
        return redirect('companys')
    # الحصول على القيود الخاصة بالشركة الحالية
    try:
        customers = Customers.objects.filter(companyID_id=current_company_id)
    except Customers.DoesNotExist:
        customers = []  # إذا لم يكن هناك أي كائنات، العودة إلى قائمة فارغة    
    # إعداد السياق
    context = {
        'customers': customers,
    }
    # عرض الصفحة مع البيانات
    return render(request, 'sales/customers.html', context)

# # دالة عرض جميع القيود
@login_required
def invoices_sales(request):
    """
    عرض جميع الكائنات من نموذج invoice في صفحة invoices.html.
    يجب أن يكون المستخدم مسجلاً للدخول للوصول إلى هذه الصفحة.
    """
    # التحقق من الأذونات أولاً
    if not request.user.has_perm('accounts.view_invoice'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة للإطلاع على فواتير المبيعات.")
        return redirect('index')
    
    # الحصول على الشركة الحالية من جلسة المستخدم
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'الرجاء تحديد الشركة للعمل عليها.')
        return redirect('companys')

    # الحصول على القيود الخاصة بالشركة الحالية
    try:
        invoices_list = InvoicesSalesHead.objects.filter(companyID_id=current_company_id)
    except InvoicesSalesHead.DoesNotExist:
        invoices_list = []  # إذا لم يكن هناك أي كائنات، العودة إلى قائمة فارغة
    
    # إعداد السياق
    context = {
        'invoices': invoices_list,
    }
    
    # عرض الصفحة مع البيانات
    return render(request, 'sales/invoices.html', context)

# دالة إنشاء فاتورة جديدة
@login_required 
def create_invoice_sales(request):
    """
    وظيفة هذه الدالة هي إنشاء فاتورة مبيعات جديدة خاصة بالشركة التي قام المستخدم بتسجيل الدخول إليها
    """
    if not request.user.has_perm('accounts.add_qayd'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة لإنشاء القيود المحاسبية.")
        return redirect('invoices_salse')
    
    if request.method == 'POST':
      head_form = InvoiceHeadForm(request.POST, request.FILES)
      formset = InvoiceBodyFormSet(request.POST)

      # التحقق من وجود current_company_id في الجلسة قبل استخدامه.
      current_company_id = request.session.get('current_company_id')
      if not current_company_id:
        messages.error(request, 'لم يتم تحديد الشركة الحالية.')
        return redirect('invoices_sales')
    
      if head_form.is_valid() and formset.is_valid():
        head = head_form.save(commit=False)
        head.created_by = request.user  # تعيين created_by فقط عند إنشاء فاتورة جديد
        head.companyID = get_object_or_404(Company, id=current_company_id)
        head.save()

        for form in formset:
          if form.cleaned_data:  # تأكد من أن النموذج يحتوي على بيانات صالحة
            body = form.save(commit=False)
            body.invoiceHeadID = head  # استخدام head مباشرة بدلاً من head.instance
            body.save()
        messages.success(request, 'تم إضافة فاتورة مبيعات جديدة')
        return redirect('invoices_sales')
      else:
        # دالة عرض الأخطاء
        handle_invoice_form_errors(head_form, formset, request)
        # إعادة عرض النماذج مع الأخطاء
        return render(request, 'sales/invoice_create.html', {
            'head_form': head_form,
            'formset': formset,
            # 'customer':Customers.objects.get(all)
        })
    else:
        # إعداد النماذج عند طلب GET
        head_form = InvoiceHeadForm()
        formset = InvoiceBodyFormSet(queryset=InvoicesSalesBody.objects.none())
    context = {
       'head_form': head_form,
       'formset': formset,
    }
    return render(request, 'sales/invoice_create.html', context)

@login_required 
def reade_invoice_sales(request):
    pass

@login_required 
def update_invoice_sales(request):
    pass

@login_required 
def delete_invoice_sales(request):
    pass
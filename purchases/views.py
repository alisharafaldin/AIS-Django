
from django.shortcuts import render , redirect, get_object_or_404
from . models import Suppliers, InvoicesPurchasesHead, InvoicesPurchasesBody
from basicinfo.forms import BasicInfoForm, LegalPersonsForm, InvoiceSearchForm
from django.db.models import Sum, Count
from basicinfo.models import BasicInfo, LegalPersons
from django.contrib import messages
from . models import Suppliers, InvoicesPurchasesHead, InvoicesPurchasesBody
from companys.models import Company
from accounts.models import Qayd, QaydDetails
from . forms import SupplierForm, InvoiceHeadForm, InvoiceBodyForm, InvoiceBodyFormSet
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
from rest_framework import viewsets, generics
# from .serializers import suppliersSerializer

# Create your views here.
def handle_form_errors(head_form, request):
    """وظيفة مساعد لمعالجة الأخطاء وعرض الرسائل المناسبة."""
    for field, errors in head_form.errors.items():
        for error in errors:
            messages.error(request, f"خطأ في النموذج في الحقل '{field}': {error}")

def handle_formset_errors(head_form, formset, request):
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
def supplier_create(request):
    if not request.user.has_perm('suppliers.add_suppliers'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة لإضافة عملاء.")
        return redirect('suppliers')
    
    if request.method == 'POST':
      basicInfo_form = BasicInfoForm(request.POST, request.FILES)
      legalPerson_form = LegalPersonsForm(request.POST, request.FILES)
      supplier_form = SupplierForm(request.POST, request.FILES)

      if basicInfo_form.is_valid() and legalPerson_form.is_valid() and supplier_form.is_valid():

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
            return redirect('purchases')
        
        supplier = supplier_form.save(commit=False)
        supplier.companyID = get_object_or_404(Company, id=current_company_id)
        supplier.legalPersonID = legalPerson
        supplier.save()
        messages.success(request, f'تم إضافة عميل جديد بإسم : {supplier.legalPersonID.name_ar}')
        return redirect('suppliers')
      else:
        # دالة عرض الأخطاء
        handle_form_errors(legalPerson_form, supplier_form, request)
        # إعادة عرض النماذج مع الأخطاء
        return render(request, 'purchases/supplier_create.html', {
            'basicInfo_form': basicInfo_form,
            'legalPerson_form': legalPerson_form,
            'supplier_form': supplier_form,
        })
    else:
        # إعداد النماذج عند طلب GET
        basicInfo_form = BasicInfoForm()
        legalPerson_form = LegalPersonsForm()
        supplier_form = SupplierForm()
    context = {
       'basicInfo_form': basicInfo_form,
       'legalPerson_form': legalPerson_form,
       'supplier_form': supplier_form,

       'basicInfo_label': basicInfo_form,
       'legalPerson_label': legalPerson_form,
       'supplier_label': supplier_form,
    }
    return render(request, 'purchases/supplier_create.html', context)

@login_required
def supplier_reade(request, id):
    supplier = get_object_or_404(Suppliers, id=id)
    legalPerson = get_object_or_404(LegalPersons, id=supplier.legalPersonID_id)
    basicInfo = get_object_or_404(BasicInfo, id=legalPerson.basicInfoID_id)

    supplier_form = SupplierForm(instance=supplier)
    legalPerson_form = LegalPersonsForm(instance=legalPerson)
    basicInfo_form = BasicInfoForm(instance=basicInfo)

    context = {
        'basicInfo_label': basicInfo_form,
        'legalPerson_label': legalPerson_form,
        'supplier_label': supplier_form,

        'supplier_form': supplier,
        'basicInfo_form': basicInfo,
        'legalPerson_form': legalPerson,
    }
    return render(request, 'purchases/supplier_reade.html', context)

@login_required
def supplier_update(request, id):
  # الحصول على الكائنات المطلوبة من قاعدة البيانات
  supplier_id = get_object_or_404(Suppliers, id=id)
  legalPerson_id = get_object_or_404(LegalPersons, id=supplier_id.legalPersonID_id)
  basicInfo_id = get_object_or_404(BasicInfo, id=legalPerson_id.basicInfoID_id)

  if request.method == 'POST':
    # إنشاء نماذج بالكائنات المسترجعة
    basicInfo_form = BasicInfoForm(request.POST, request.FILES, instance=basicInfo_id)
    legalPerson_form = LegalPersonsForm(request.POST, request.FILES, instance=legalPerson_id)
    supplier_form = SupplierForm(request.POST, request.FILES, instance=supplier_id)
    
      # تحديث البيانات وعرض رسالة تأكيد
    if basicInfo_form.is_valid() and legalPerson_form.is_valid() and supplier_form.is_valid():
      basicInfo = basicInfo_form.save(commit=False)
      basicInfo.created_by = request.user 
      basicInfo.save()

      legalPerson = legalPerson_form.save(commit=False)
      legalPerson.basicInfoID = basicInfo
      legalPerson.save()
      
      supplier = supplier_form.save(commit=False)
      supplier.legalPersonID = legalPerson
      supplier.companyID = Company.objects.get(id=request.session.get('current_company_id'))
      supplier.save()

      messages.success(request, f' تم تعديل بيانات المورد : {supplier.legalPersonID.name_ar} ') 
      return redirect('suppliers')
    else :      
      # عرض رسائل الخطأ من النماذج
      handle_form_errors(basicInfo_form, request)
      handle_form_errors(legalPerson_form, request)
      handle_form_errors(supplier_form, request)
      return redirect('supplier_update')
  # إنشاء نماذج بالكائنات المسترجعة
  basicInfo_form = BasicInfoForm(instance=basicInfo_id)
  legalPerson_form = LegalPersonsForm(instance=legalPerson_id)
  supplier_form = SupplierForm(instance=supplier_id)

  context = {
    'supplier_id': supplier_id,

    'basicInfo_form': basicInfo_form,
    'legalPerson_form': legalPerson_form,
    'supplier_form': supplier_form,
    
    'basicInfo_label': BasicInfoForm(),
    'legalPerson_label': LegalPersonsForm(),
    'supplier_label': SupplierForm(),   
  }
  return render(request, 'purchases/supplier_update.html', context)    

@login_required
def supplier_delete(request, id):
  # الحصول على الكائنات المطلوبة من قاعدة البيانات
  supplier = get_object_or_404(Suppliers, id=id)
  legalPerson = get_object_or_404(LegalPersons, id=supplier.legalPersonID_id)
  basicInfo = get_object_or_404(BasicInfo, id=legalPerson.basicInfoID_id)

  # إنشاء نماذج بالكائنات المسترجعة
  supplier_form = SupplierForm(instance=supplier)
  legalPerson_form = LegalPersonsForm(instance=legalPerson)
  basicInfo_form = BasicInfoForm(instance=basicInfo)

  if request.method == 'POST':
    # حذف الكائن وإضافة رسالة نجاح
    supplier.delete()
    messages.info(request, f'تم حذف المورد {supplier.legalPersonID.name_ar}')
    return redirect('suppliers')
  else:
      handle_form_errors(basicInfo_form, request)
      handle_form_errors(legalPerson_form, request)
      handle_form_errors(supplier_form, request)
  
  context = {
      'basicInfo_label': basicInfo_form,
      'legalPerson_label': legalPerson_form,
      'supplier_label': supplier_form,

      'supplier_form': supplier,
      'basicInfo_form': basicInfo,
      'legalPerson_form': legalPerson,
  }
  return render(request, 'purchases/supplier_delete.html', context)

@login_required
def suppliers(request):
    # التحقق من الأذونات أولاً
    if not request.user.has_perm('suppliers.view_suppliers'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة للإطلاع على ملفات الموردين.")
        return redirect('index')
    # الحصول على الشركة الحالية من جلسة المستخدم
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'الرجاء تحديد الشركة للعمل عليها.')
        return redirect('companys')
    # الحصول على القيود الخاصة بالشركة الحالية
    try:
        suppliers = Suppliers.objects.filter(companyID_id=current_company_id).annotate(
        total_Count=Count('purchases_supplier__sequence')).order_by("-total_Count")
        # حساب الإجمالي الكلي لجميع الفواتير
        total_invoice_Count = suppliers.aggregate(total_Count=Count('purchases_supplier__sequence'))['total_Count'] or 0
    except suppliers.DoesNotExist:
        suppliers = []  # إذا لم يكن هناك أي كائنات، العودة إلى قائمة فارغة    
    # إعداد السياق
    context = {
        'suppliers': suppliers,
        'total_invoice_Count': total_invoice_Count,
    }
    # عرض الصفحة مع البيانات
    return render(request, 'purchases/suppliers.html', context)

@login_required
def supplier_purchases_invoices(request, supplier_id):
    # الحصول على الشركة الحالية من جلسة المستخدم
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'الرجاء تحديد الشركة للعمل عليها.')
        return redirect('companys')
    # الحصول على المورد المحدد
    supplier = get_object_or_404(suppliers, id=supplier_id)
    try:
        # الحصول على فواتير المبيعات الخاصة بالمورد في الشركة الحالية
        invoices = InvoicesPurchasesHead.objects.filter(companyID_id=current_company_id, supplierID=supplier).annotate(
        total_sum=Sum('purchases_invoice__total_price_after_tax')).order_by("-id")
        # حساب الإجمالي الكلي لجميع الفواتير
        total_invoices_sum = invoices.aggregate(total_sum=Sum('purchases_invoice__total_price_after_tax'))['total_sum'] or 0
    except InvoicesPurchasesHead.DoesNotExist:
        invoices = []  # إذا لم يكن هناك أي كائنات، العودة إلى قائمة فارغة
    context = {
        'invoices': invoices,
        'invoice_search_form':InvoiceSearchForm(request.GET),
        'total_invoices_sum':total_invoices_sum,
    }
    return render(request, 'purchases/invoices.html', context)

# # دالة عرض جميع القيود
def calculate_totals(details_queryset):
    """ وظيفة مساعدة لعمل مجاميع القيود """
    total_d = sum(item.debit for item in details_queryset)
    total_c = sum(item.credit for item in details_queryset)
    return total_d, total_c, total_d - total_c

@login_required
def invoices_purchases_search(request):
    # الحصول على معايير البحث من الطلب
    search_name = request.GET.get('search_name', '')
    search_invoice_number = request.GET.get('search_invoice_number', '')
    search_date = request.GET.get('search_date', '')
    search_currencyID = request.GET.get('currencyID', '')
    search_inventoryID = request.GET.get('inventoryID', '')
    search_supplierID = request.GET.get('supplierID', '')
    start_date = request.GET.get('start_date','')
    end_date = request.GET.get('end_date','')
    
    invoices_query = InvoicesPurchasesHead.objects.all()
    # استعلام الفواتير بين تاريخين
    if start_date and end_date:
        invoices_query = invoices_query.filter(date__range=[start_date, end_date])
    if search_date:
        invoices_query = invoices_query.filter(date=search_date)
    if search_name:
        invoices_query = invoices_query.filter(supplierID__legalPersonID__name_ar__icontains=search_name)
    if search_invoice_number:
        invoices_query = invoices_query.filter(sequence=search_invoice_number)
    if search_currencyID:
        invoices_query = invoices_query.filter(currencyID=search_currencyID)
    if search_inventoryID:
        invoices_query = invoices_query.filter(inventoryID=search_inventoryID)
    if search_supplierID:
        invoices_query = invoices_query.filter(supplierID=search_supplierID)
    
    # الحصول على الشركة الحالية من الجلسة
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'الرجاء تحديد الشركة للعمل عليها.')
        return redirect('companys')

    # تصفية الفواتير بناءً على الشركة الحالية
    invoices_query = invoices_query.filter(companyID_id=current_company_id).annotate(
        total_sum=Sum('purchases_invoice__total_price_after_tax')).order_by("-id")

      # حساب الإجمالي الكلي لجميع الفواتير
    total_invoices_sum = invoices_query.aggregate(total_sum=Sum('purchases_invoice__total_price_after_tax'))['total_sum'] or 0

    # إعداد السياق
    context = {
        'invoices': invoices_query,
        'invoice_search_form': InvoiceSearchForm(request.GET),
        'total_invoices_sum':total_invoices_sum,
    }

    # عرض الصفحة مع البيانات
    return render(request, 'purchases/invoices.html', context)

@login_required
def invoice_purchases_create(request):
    if not request.user.has_perm('purchases.add_InvoicesPurchasesHead'):
        messages.info(request, f"عذراً {request.user}، ليس لديك الأذونات اللازمة لإنشاء قيود فاتورة مشتريات.")
        return redirect('invoices_purchases')

    # التحقق من وجود current_company_id في الجلسة قبل استخدامه.
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'لم يتم تحديد الشركة الحالية.')
        return redirect('invoices_purchases')
    
    if request.method == 'POST':
        # تمرير companyID إلى النموذج عند تقديم البيانات
        head_form = InvoiceHeadForm(request.POST, request.FILES, companyID=current_company_id)
        formset = InvoiceBodyFormSet(request.POST)

        if head_form.is_valid() and formset.is_valid():
            head = head_form.save(commit=False)
            head.created_by = request.user  # تعيين created_by فقط عند إنشاء فاتورة جديد
            head.companyID = get_object_or_404(Company, id=current_company_id)
            head.save()

            for form in formset:
                if form.cleaned_data:  # تأكد من أن النموذج يحتوي على بيانات صالحة
                    body = form.save(commit=False)
                    body.invoiceHeadID = head
                    body.save()
            messages.success(request, 'تم إضافة فاتورة مبيعات جديدة')
            return redirect('invoices_purchases')
        else:
            # دالة عرض الأخطاء
            handle_formset_errors(head_form, formset, request)
            # إعادة عرض النماذج مع الأخطاء
            return render(request, 'purchases/invoice_create.html', {
                'head_form': head_form,
                'formset': formset,
            })
    else:
        # إعداد النماذج عند طلب GET
        head_form = InvoiceHeadForm(companyID=current_company_id)
        formset = InvoiceBodyFormSet(queryset=InvoicesPurchasesBody.objects.none())
        is_edit_mode = True  # حدد إذا كنت في وضع إنشاء أو تعديل

        context = {
            'is_edit_mode': is_edit_mode,
            'invoice_head_form': head_form,
            'invoice_body_form': formset,
            'invoice_head_label': InvoiceHeadForm(),
            'invoice_body_label': InvoiceBodyForm(),
        }
        return render(request, 'purchases/invoice_create.html', context)
    
@login_required
def invoice_purchases_reade(request, id):
    if not request.user.has_perm('purchases.view_InvoicesPurchasesHead'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة للإطلاع على فواتير المبيعات.")
        return redirect('invoices_purchases')
    
    invoice_head =  get_object_or_404(InvoicesPurchasesHead, id=id)
    invoice_body = InvoicesPurchasesBody.objects.filter(invoiceHeadID=id)

    # تجميع الكميات والأسعار
    total_quantity = invoice_body.aggregate(Sum('quantity'))['quantity__sum'] or 0
    total_price_after_tax = invoice_body.aggregate(Sum('total_price_after_tax'))['total_price_after_tax__sum'] or 0.0
   
    supplier = Suppliers.objects.get(id=invoice_head.supplierID_id)
    is_edit_mode = False  # أو True بناءً على وضع النموذج
    context = {
       'is_edit_mode':is_edit_mode,
       'supplier':supplier,
        'invoice_body_label': invoice_body,
        'invoice_head_label': invoice_head,

        'invoice_head_form': invoice_head,
        'invoice_body_form': invoice_body,

        'total_quantity':total_quantity,
        'total_price_after_tax':total_price_after_tax,
    }
    return render(request, 'purchases/invoice_reade.html', context)

@login_required 
def invoice_purchases_update(request, id):
    if not request.user.has_perm('purchases.change_InvoicesPurchasesHead'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة لتعديل فواتير المبيعات.")
        return redirect('invoices_purchases')
    invoice_head = get_object_or_404(InvoicesPurchasesHead, id=id)

    # استخدام formset للحصول على جميع نماذج QaydDetails المرتبطة بـ Qayd المحدد
    InvoiceBodyFormSet = modelformset_factory(InvoicesPurchasesBody, form=InvoiceBodyForm, extra=1)
    queryset = InvoicesPurchasesBody.objects.filter(invoiceHeadID=invoice_head)

    if request.method == 'POST':
        head_form = InvoiceHeadForm(request.POST, request.FILES, instance=invoice_head)
        formset = InvoiceBodyFormSet(request.POST, queryset=queryset)
        if head_form.is_valid() and formset.is_valid():
          head = head_form.save(commit=False)
          head.updated_by = request.user
          head.companyID = Company.objects.get(id=request.session.get('current_company_id'))
          head.save()
          for form in formset:
            if form.cleaned_data.get('DELETE', False):
                if form.instance.pk:
                    form.instance.delete()  # حذف النموذج من قاعدة البيانات
            else:
                body = form.save(commit=False)
                body.invoiceHeadID = head
                body.save()
          messages.success(request, f'تم تحديث بيانات فاتورة مبيعات {id} بنجاح')
          return redirect('invoices_purchases')
        else:
            # دالة عرض الأخطاء
            handle_formset_errors(head_form, formset, request)
    else:
        head_form = InvoiceHeadForm(instance=invoice_head)
        formset = InvoiceBodyFormSet(queryset=queryset)

    supplier = Suppliers.objects.get(id=invoice_head.supplierID_id)
    is_edit_mode = True  # أو True بناءً على وضع النموذج

    context = {
        'supplier':supplier,
        'is_edit_mode':is_edit_mode,
        'invoice_head': invoice_head,
        'invoice_head_form': head_form,
        'invoice_body_form': formset,
        'invoice_head_label': InvoiceHeadForm(),
        'invoice_body_label': InvoiceBodyForm(),  
    }
    return render(request, 'purchases/invoice_update.html', context)

@login_required 
def invoice_purchases_delete(request, id):
    if not request.user.has_perm('purchases.delete_InvoicesPurchasesHead'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة لحذف فواتير المبيعات.")
        return redirect('invoices_purchases')
    if request.user.is_authenticated and not request.user.is_anonymous:
        qayd_id = InvoicesPurchasesHead.objects.get(id=id)
        if 'btndelete' in request.POST:
            qayd_id.delete()
            messages.success(request, f'تم حذف القيد {id} بنجاح')
            return redirect('invoices_purchases')
    else:
        messages.error(request, 'الرجاء تسجيل الدخول أولاً')
    invoice_body = InvoicesPurchasesBody.objects.filter(invoiceHeadID=id)
    # تجميع الكميات والأسعار
    total_quantity = invoice_body.aggregate(Sum('quantity'))['quantity__sum'] or 0
    total_price_after_tax = invoice_body.aggregate(Sum('total_price_after_tax'))['total_price_after_tax__sum'] or 0.0

    is_edit_mode = False  # أو True بناءً على وضع النموذج
    context = {
       'is_edit_mode':is_edit_mode,
        'invoice_head_form': qayd_id,
        'invoice_body_form': invoice_body,

         'total_quantity':total_quantity,
        'total_price_after_tax':total_price_after_tax,
    }
    return render(request, 'purchases/invoice_delete.html', context)

@login_required
def invoices_purchases(request):
    # التحقق من الأذونات أولاً
    if not request.user.has_perm('purchases.view_InvoicesPurchasesHead'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة للإطلاع على فواتير المبيعات.")
        return redirect('index')
    # الحصول على الشركة الحالية من جلسة المستخدم
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'الرجاء تحديد الشركة للعمل عليها.')
        return redirect('companys')
    # الحصول على فواتير المبيعات الخاصة بالشركة الحالية
    try:
        # الحصول على فواتير المبيعات الخاصة بالشركة الحالية
        invoices = InvoicesPurchasesHead.objects.filter(companyID_id=current_company_id).annotate(
        total_sum=Sum('purchases_invoice__total_price_after_tax')).order_by("-id")
        # حساب الإجمالي الكلي لجميع الفواتير
        total_invoices_sum = invoices.aggregate(total_sum=Sum('purchases_invoice__total_price_after_tax'))['total_sum'] or 0
    except InvoicesPurchasesHead.DoesNotExist:
        invoices = []  # إذا لم يكن هناك أي كائنات، العودة إلى قائمة فارغة
    context = {
        'invoices': invoices,
        'invoice_search_form':InvoiceSearchForm(request.GET),
        'total_invoices_sum':total_invoices_sum,
    }
    # عرض الصفحة مع البيانات
    return render(request, 'purchases/invoices.html', context)


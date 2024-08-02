import io
from typing import Any
from django.shortcuts import render , redirect
from django.contrib import messages
from . models import Suppliers, InvoiceHead, InvoiceBody
from companys.models import Company
from . forms import Suppliers, InvoiceHeadForm, InvoiceBodyForm, InvoiceBodyFormSet
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

# Create your views here.

# دوال لإنشاء وتحديث وقراءة وحذف القيود المحاسبية

def handle_form_errors(head_form, formset, request):
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

# # دالة عرض جميع القيود
@login_required
def invoices(request):
    """
    عرض جميع الكائنات من نموذج invoice في صفحة invoices.html.
    يجب أن يكون المستخدم مسجلاً للدخول للوصول إلى هذه الصفحة.
    """
    # التحقق من الأذونات أولاً
    if not request.user.has_perm('accounts.view_invoice'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة للإطلاع على القيود المحاسبية.")
        return redirect('index')
    
    # الحصول على الشركة الحالية من جلسة المستخدم
    current_company_id = request.session.get('current_company_id')
    
    if not current_company_id:
        messages.error(request, 'الرجاء تحديد الشركة للعمل عليها.')
        return redirect('companys')

    # الحصول على القيود الخاصة بالشركة الحالية
    try:
        invoices_list = InvoiceHead.objects.filter(companyID_id=current_company_id)
    except InvoiceHead.DoesNotExist:
        invoices_list = []  # إذا لم يكن هناك أي كائنات، العودة إلى قائمة فارغة
    
    # إعداد السياق
    context = {
        'invoices': invoices_list,
    }
    
    # عرض الصفحة مع البيانات
    return render(request, 'purchases/invoices.html', context)


# دالة إنشاء فاتورة جديدة
@login_required 
def invoice_create(request):
    """
    وظيفة هذه الدالة هي إنشاء قيد محاسبي جديد خاص بالشركة التي قام المستخدم بتسجيل الدخول إليها
    """
    if not request.user.has_perm('accounts.add_invoice'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة لإنشاء القيود المحاسبية.")
        return redirect('invoices')
    
    if request.method == 'POST':
      head_form = InvoiceHead(request.POST, request.FILES)
      formset = InvoiceBodyFormSet(request.POST)

      if head_form.is_valid() and formset.is_valid():
        head = head_form.save(commit=False)
        head.created_by = request.user  # تعيين created_by فقط عند إنشاء قيد جديد
        head.companyID = Company.objects.get(id=request.session.get('current_company_id'))
     
        head.save()

        for form in formset:
          if form.cleaned_data:  # تأكد من أن النموذج يحتوي على بيانات صالحة
            body = form.save(commit=False)
            body.invoiceHeadID = head  # استخدام head مباشرة بدلاً من head.instance
            body.save()
        messages.success(request, 'تم إضافة قيد جديد بنجاح')
        return redirect('invoices')
      else:
        # دالة عرض الأخطاء
        handle_form_errors(head_form, formset, request)
        # إعادة عرض النماذج مع الأخطاء
        return render(request, 'purchases/invoice_create.html', {
            'head_form': head_form,
            'formset': formset,
        })
    else:
        # إعداد النماذج عند طلب GET
        head_form = InvoiceHeadForm()
        formset = InvoiceBodyFormSet(queryset=InvoiceBody.objects.none())
    context = {
       'head_form': head_form,
       'formset': formset,
    }
    return render(request, 'purchases/invoice_create.html', context)

# @login_required 
# def invoice_reade(request, id):
#     """ دالة عرض وقراءة قيد موجود مسبقاَ """
#     if not request.user.has_perm('accounts.view_invoice'):
#         messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة للإطلاع القيود المحاسبية.")
#         return redirect('invoices')
#     if request.user.is_authenticated and not request.user.is_anonymous:
#         invoice_reade = invoice.objects.get(id=id)
#         invoice_reade_details = invoiceDetails.objects.filter(invoiceID=id)
#         total_d, total_c, difference = calculate_totals(invoice_reade_details)
#         context = {
#             'invoice_reade': invoice_reade,
#             'invoice_reade_details': invoice_reade_details,
#             'total_d': total_d,
#             'total_c': total_c,
#             'difference': difference,
#         }
#         return render(request, 'accounts/invoice_reade.html', context)

# @login_required 
# def invoice_delete(request, id):
#     """ د دالة حذف قيد """
#     if not request.user.has_perm('accounts.delete_invoice'):
#         messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة لحذف القيود المحاسبية.")
#         return redirect('invoices')
#     if request.user.is_authenticated and not request.user.is_anonymous:
#         invoice_id = invoice.objects.get(id=id)
#         if 'btndelete' in request.POST:
#             invoice_id.delete()
#             messages.success(request, f'تم حذف القيد {id} بنجاح')
#             return redirect('invoices')
#     else:
#         messages.error(request, 'الرجاء تسجيل الدخول أولاً')
    
#     invoice_id_details = invoiceDetails.objects.filter(invoiceID=id)
#     total_d, total_c, difference = calculate_totals(invoice_id_details)

#     context = {
#         'invoice_id': invoice_id,
#         'invoice_id_details': invoice_id_details,
#         'total_d': total_d,
#         'total_c': total_c,
#         'difference': difference,
#     }
#     return render(request, 'accounts/invoice_delete.html', context)

# # دالة تحديث بيانات قيد موجود
# @login_required 
# def invoice_update(request, id):
#     if not request.user.has_perm('accounts.change_invoice'):
#         messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة لتعديل القيود المحاسبية.")
#         return redirect('invoices')
#     invoice_update = get_object_or_404(invoice, id=id)
#     # استخدام formset للحصول على جميع نماذج invoiceDetails المرتبطة بـ invoice المحدد
#     invoiceDetailsFormSet = modelformset_factory(invoiceDetails, form=invoiceDetailsForm, extra=1)
#     queryset = invoiceDetails.objects.filter(invoiceID=invoice_update)

#     if request.method == 'POST':
#         head_form = invoiceForm(request.POST, request.FILES, instance=invoice_update)
#         formset = invoiceDetailsFormSet(request.POST, queryset=queryset)
    
#         if head_form.is_valid() and formset.is_valid():
#           head = head_form.save(commit=False)
#           head.updated_by = request.user
#           head.companyID = Company.objects.get(id=request.session.get('current_company_id'))
#           head.save()
        
#           for form in formset:
#             if form.cleaned_data.get('DELETE', False):
#                 if form.instance.pk:
#                     form.instance.delete()  # حذف النموذج من قاعدة البيانات
#             else:
#                 body = form.save(commit=False)
#                 body.invoiceID = head
#                 body.save()

#           messages.success(request, f'تم تحديث بيانات القيد {id} بنجاح')
#           return redirect('invoices')
#         else:
#             # دالة عرض الأخطاء
#             handle_form_errors(head_form, formset, request)
#     else:
#         head_form = invoiceForm(instance=invoice_update)
#         formset = invoiceDetailsFormSet(queryset=queryset)
#     total_d, total_c, difference = calculate_totals(queryset)
#     context = {
#         'invoice_update': invoice_update,
#         'head_form': head_form,
#         'formset':formset,
#         'total_d': total_d,
#         'total_c': total_c,
#         'difference': difference,
#     }
#     return render(request, 'accounts/invoice_update.html', context)


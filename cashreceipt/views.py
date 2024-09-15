from django.shortcuts import render , redirect, get_object_or_404
from django.db.models import Sum, Count
from django.contrib import messages
from . models import  CashReceiptHead, CashReceiptBody
from companys.models import Company
from . forms import CashReceiptHeadForm, CashReceiptBodyForm, CashReceiptFormSet
from django.contrib.auth.decorators import login_required

# دوال لإنشاء وتحديث وقراءة وحذف القيود المحاسبية

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
def create(request):
    if not request.user.has_perm('cashreceipt.add_CashReceiptHead'):
        messages.info(request, f"عذراً {request.user}، ليس لديك الأذونات اللازمة لإنشاء سند قبض.")
        return redirect('cashreceipts')

    # التحقق من وجود current_company_id في الجلسة قبل استخدامه.
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'لم يتم تحديد الشركة الحالية.')
        return redirect('index')
    
    if request.method == 'POST':
        # تمرير companyID إلى النموذج عند تقديم البيانات
        head_form = CashReceiptHeadForm(request.POST, request.FILES, companyID=current_company_id)
        formset = CashReceiptFormSet(request.POST)

        if head_form.is_valid() and formset.is_valid():
            head = head_form.save(commit=False)
            head.created_by = request.user  # تعيين created_by فقط عند إنشاء فاتورة جديد
            head.companyID = get_object_or_404(Company, id=current_company_id)
            head.save()

            for form in formset:
                if form.cleaned_data:  # تأكد من أن النموذج يحتوي على بيانات صالحة
                    body = form.save(commit=False)
                    body.cashReceiptHeadID = head
                    # إذا لم يقم المستخدم بتعيين inventoryID، استخدم القيمة من رأس الفاتورة
                    if not form.cleaned_data.get('inventoryID'):
                        body.inventoryID = head.inventoryID
                    body.save()
            messages.success(request, 'تم إضافة فاتورة مبيعات جديدة')
            return redirect('cashreceipts')
        else:
            # دالة عرض الأخطاء
            handle_formset_errors(head_form, formset, request)
            # إعادة عرض النماذج مع الأخطاء
            return render(request, 'cash_receipt/cashReceipt_create.html', {
                'head_form': head_form,
                'formset': formset,
            })
    else:
        # إعداد النماذج عند طلب GET
        head_form = CashReceiptHeadForm(companyID=current_company_id)
        formset = CashReceiptFormSet(queryset=CashReceiptBody.objects.none())
        is_edit_mode = True  # حدد إذا كنت في وضع إنشاء أو تعديل

        context = {
            'is_edit_mode': is_edit_mode,
            'cash_receipt_head_form': head_form,
            'cash_receipt_body_form': formset,
            'cash_receipt_head_label': CashReceiptHeadForm(),
            'cash_receipt_body_label': CashReceiptBodyForm(),
        }
        return render(request, 'cashreceipt/create.html', context)

# @login_required
# def reade(request, id):
#     if not request.user.has_perm('cash_receipt.view_CashReceiptHead'):
#         messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة للإطلاع على فواتير المبيعات.")
#         return redirect('cashReceipts_cash_receipt')
    
#     cashReceipt_head =  get_object_or_404(CashReceiptHead, id=id)
#     cashReceipt_body = CashReceiptBody.objects.filter(cashReceiptHeadID=id)

#     # تجميع الكميات والأسعار
#     total_quantity = cashReceipt_body.aggregate(Sum('quantity'))['quantity__sum'] or 0
#     total_price_after_tax = cashReceipt_body.aggregate(Sum('total_price_after_tax'))['total_price_after_tax__sum'] or 0.0
   
#     customer = Customers.objects.get(id=cashReceipt_head.customerID_id)
#     is_edit_mode = False  # أو True بناءً على وضع النموذج
#     context = {
#        'is_edit_mode':is_edit_mode,
#        'customer':customer,
#         'cashReceipt_body_label': cashReceipt_body,
#         'cashReceipt_head_label': cashReceipt_head,

#         'cashReceipt_head_form': cashReceipt_head,
#         'cashReceipt_body_form': cashReceipt_body,

#         'total_quantity':total_quantity,
#         'total_price_after_tax':total_price_after_tax,
#     }
#     return render(request, 'cash_receipt/cashReceipt_reade.html', context)

# @login_required 
# def update(request, id):
#     if not request.user.has_perm('cash_receipt.change_CashReceiptHead'):
#         messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة لتعديل فواتير المبيعات.")
#         return redirect('cashReceipts_cash_receipt')
#     cashReceipt_head = get_object_or_404(CashReceiptHead, id=id)

#     # استخدام formset للحصول على جميع نماذج QaydDetails المرتبطة بـ Qayd المحدد
#     CashReceiptBodyFormSet = modelformset_factory(CashReceiptBody, form=CashReceiptBodyForm, extra=1)
#     queryset = CashReceiptBody.objects.filter(cashReceiptHeadID=cashReceipt_head)

#     if request.method == 'POST':
#         head_form = CashReceiptHeadForm(request.POST, request.FILES, instance=cashReceipt_head)
#         formset = CashReceiptBodyFormSet(request.POST, queryset=queryset)
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
#                 body.cashReceiptHeadID = head
#                 # إذا لم يقم المستخدم بتعيين inventoryID، استخدم القيمة من رأس الفاتورة
#                 if not form.cleaned_data.get('inventoryID'):
#                     body.inventoryID = head.inventoryID
#                 body.save()
#           messages.success(request, f'تم تحديث بيانات فاتورة مبيعات {id} بنجاح')
#           return redirect('cashReceipts_cash_receipt')
#         else:
#             # دالة عرض الأخطاء
#             handle_formset_errors(head_form, formset, request)
#     else:
#         head_form = CashReceiptHeadForm(instance=cashReceipt_head)
#         formset = CashReceiptBodyFormSet(queryset=queryset)

#     customer = Customers.objects.get(id=cashReceipt_head.customerID_id)
#     is_edit_mode = True  # أو True بناءً على وضع النموذج

#     context = {
#         'customer':customer,
#         'is_edit_mode':is_edit_mode,
#         'cashReceipt_head': cashReceipt_head,
#         'cashReceipt_head_form': head_form,
#         'cashReceipt_body_form': formset,
#         'cashReceipt_head_label': CashReceiptHeadForm(),
#         'cashReceipt_body_label': CashReceiptBodyForm(),  
#     }
#     return render(request, 'cash_receipt/cashReceipt_update.html', context)

# @login_required 
# def delete(request, id):
#     if not request.user.has_perm('cash_receipt.delete_CashReceiptHead'):
#         messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة لحذف فواتير المبيعات.")
#         return redirect('cashReceipts_cash_receipt')
#     if request.user.is_authenticated and not request.user.is_anonymous:
#         qayd_id = CashReceiptHead.objects.get(id=id)
#         if 'btndelete' in request.POST:
#             qayd_id.delete()
#             messages.success(request, f'تم حذف القيد {id} بنجاح')
#             return redirect('cashReceipts_cash_receipt')
#     else:
#         messages.error(request, 'الرجاء تسجيل الدخول أولاً')
#     cashReceipt_body = CashReceiptBody.objects.filter(cashReceiptHeadID=id)
#     # تجميع الكميات والأسعار
#     total_quantity = cashReceipt_body.aggregate(Sum('quantity'))['quantity__sum'] or 0
#     total_price_after_tax = cashReceipt_body.aggregate(Sum('total_price_after_tax'))['total_price_after_tax__sum'] or 0.0

#     is_edit_mode = False  # أو True بناءً على وضع النموذج
#     context = {
#        'is_edit_mode':is_edit_mode,
#         'cashReceipt_head_form': qayd_id,
#         'cashReceipt_body_form': cashReceipt_body,

#          'total_quantity':total_quantity,
#         'total_price_after_tax':total_price_after_tax,
#     }
#     return render(request, 'cash_receipt/cashReceipt_delete.html', context)

@login_required
def cashreceipts(request):
    # التحقق من الأذونات أولاً
    if not request.user.has_perm('cash_receipt.view_CashReceiptHead'):
        messages.info(request, f"عذراً {request.user}، ليس لديك الأذونات اللازمة للإطلاع على سندات القبض.")
        return redirect('index')

    # الحصول على الشركة الحالية من جلسة المستخدم
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'الرجاء تحديد الشركة للعمل عليها.')
        return redirect('companys')

    # try:
    #     # الحصول على سندات القبض الخاصة بالشركة الحالية
    #     cashReceipts = CashReceiptHead.objects.filter(companyID_id=current_company_id).annotate(
    #         total_sum=Sum('cash_receipt__amountDebit'),
    #         total_local_sum=Sum('cash_receipt__amountDebit_local_currency')
    #     ).order_by("-id")

    #     # حساب الإجمالي الكلي لجميع سندات القبض (بالعملة الأساسية والمحلية)
    #     total_amounts = cashReceipts.aggregate(
    #         total_sum=Sum('total_sum'),
    #         total_local_sum=Sum('total_local_sum')
    #     )

    #     # إجمالي سندات القبض بالعملة الأساسية والمحلية
    #     total_sum = total_amounts.get('total_sum', 0) or 0
    #     total_local_sum = total_amounts.get('total_local_sum', 0) or 0

    # except CashReceiptHead.DoesNotExist:
    #     cashReceipts = []  # إذا لم يكن هناك أي كائنات، العودة إلى قائمة فارغة
    #     total_sum = 0
    #     total_local_sum = 0
    #     messages.warning(request, 'لا توجد سندات قبض مسجلة لهذه الشركة.')

    context = {
        # 'cashReceipts': cashReceipts,
        # 'total_sum': total_sum,
        # 'total_local_sum': total_local_sum,
    }
    # عرض الصفحة مع البيانات
    return render(request, 'cashreceipt/cashReceipts.html', context)
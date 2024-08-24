import io
from django.shortcuts import render , redirect
from django.contrib import messages
from . models import AccountsTree, Qayd, QaydDetails
from companys.models import Company
from django.db.models import Sum
from . forms import AccountsTreeForm, QaydForm, QaydDetailsForm, QaydDetailsFormSet
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q #لعمل أكثر من تصفية
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

@login_required 
def account_create(request):
     # التحقق من وجود current_company_id في الجلسة قبل استخدامه.
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'لم يتم تحديد الشركة الحالية.')
        return redirect('invoices_sales')
    
    if request.method == 'POST':
        accountTree_form = AccountsTreeForm(request.POST, request.FILES)
        if accountTree_form.is_valid():
            account = accountTree_form.save(commit=False)
            # account.created_by = request.user  # تعيين created_by فقط عند إنشاء قيد جديد
            account.companyID = get_object_or_404(Company, id=current_company_id)
            account.save()
            messages.success(request, 'تمت الإضافة بنجاح') 
            return redirect('accounts')
    else:
        form = AccountsTreeForm(companyID=current_company_id)
    context = {
        'acc_form': AccountsTreeForm(),
        'form':form,
    }    
    return render(request,'accounts/account_create.html', context)

@login_required
def account_reade(request, id):
    if request.user.is_authenticated and not request.user.is_anonymous:
      account_id = AccountsTree.objects.get(id=id)
    context = {
        'account':account_id,
    }
    return render(request, 'accounts/account_reade.html', context)

@login_required 
def account_update(request, id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        account_id = AccountsTree.objects.get(id=id)
        if request.method == 'POST':
            account_save = AccountsTreeForm(request.POST, request.FILES, instance=account_id)
            if account_save.is_valid():
                account_save.save()
                messages.success(request, 'تم التحديث بنجاح')       
                return redirect('accounts')
        else:
            account_save = AccountsTreeForm(instance=account_id)
        context = {
            'account_form':account_save,
            'account':account_id,
        }
        return render(request, 'accounts/account_update.html', context)
    else:
        messages.info(request, 'الرجاء تسجيل الدخول' )
        return redirect('accounts')

@login_required 
def account_delete(request, id):
    if request.user.is_authenticated and not request.user.is_anonymous:
      account_id = AccountsTree.objects.get(id=id)
      if 'btndelete' in request.POST:
        account_id.delete()
        messages.info(request, 'تم الحذف بنجاح')
        return redirect('accounts')
    else:
        messages.error(request, 'الرجاء تسجيل الدخول أولاً')
    context = {
        'account':account_id,
    }
    return render(request, 'accounts/account_delete.html', context)

@login_required
def accounts(request):
      # التحقق من وجود current_company_id في الجلسة قبل استخدامه.
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'لم يتم تحديد الشركة الحالية.')
        return redirect('invoices_sales')
        
        # تصفية القيود الخاصة بالشركة أو العامة
    accounts = AccountsTree.objects.filter(
        Q(companyID=current_company_id) | Q(companyID__isnull=True)
    ).order_by("categoryID", "code")
    context = {
        'accounts': accounts,
    }
    return render(request,'accounts/accounts.html', context)

@login_required
def accounts_tree(request):
    accounts = AccountsTree.objects.filter(parent__isnull=True)
    accounts2 = accounts.order_by("code")
    context = {
        'accounts':accounts2,
    }    
    return render(request,'accounts/accounts_tree.html', context)

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

# دالة إنشاء قيد جديد

@login_required 
def qayd_create(request):
    """
    وظيفة هذه الدالة هي إنشاء قيد محاسبي جديد خاص بالشركة التي قام المستخدم بتسجيل الدخول إليها
    """
    if not request.user.has_perm('accounts.add_qayd'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة لإنشاء القيود المحاسبية.")
        return redirect('qayds')
    
    # التحقق من وجود current_company_id في الجلسة قبل استخدامه.
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'لم يتم تحديد الشركة الحالية.')
        return redirect('invoices_sales')
    
    if request.method == 'POST':
        head_form = QaydForm(request.POST, request.FILES)
        formset = QaydDetailsFormSet(
            request.POST, 
            request.FILES, 
            form_kwargs={'companyID': current_company_id}  # تمرير companyID للنموذج
        )

        if head_form.is_valid() and formset.is_valid():
            head = head_form.save(commit=False)
            head.created_by = request.user  # تعيين created_by فقط عند إنشاء قيد جديد
            head.companyID = get_object_or_404(Company, id=current_company_id)
            head.save()

            for form in formset:
                if form.cleaned_data:  # تأكد من أن النموذج يحتوي على بيانات صالحة
                    body = form.save(commit=False)
                    body.qaydID = head  # استخدام head مباشرة بدلاً من head.instance
                    body.save()
            messages.success(request, 'تم إضافة قيد جديد بنجاح')
            return redirect('qayds')
        else:
            # دالة عرض الأخطاء
            handle_form_errors(head_form, formset, request)
            # إعادة عرض النماذج مع الأخطاء
            return render(request, 'accounts/qayd_create.html', {
                'head_form': head_form,
                'formset': formset,
            })
    else:
        # إعداد النماذج عند طلب GET
        head_form = QaydForm() 
        formset = QaydDetailsFormSet(
            queryset=QaydDetails.objects.none(),  # لا توجد بيانات افتراضية
            form_kwargs={'companyID': current_company_id}  # تمرير companyID للنموذج
        )
    context = {
        'head_form': head_form,
        'formset': formset,
    }
    return render(request, 'accounts/qayd_create.html', context)

@login_required 
def qayd_reade(request, id):
    """ دالة عرض وقراءة قيد موجود مسبقاَ """
    if not request.user.has_perm('accounts.view_qayd'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة للإطلاع القيود المحاسبية.")
        return redirect('qayds')
    if request.user.is_authenticated and not request.user.is_anonymous:
        qayd_reade = Qayd.objects.get(id=id)
        qayd_reade_details = QaydDetails.objects.filter(qaydID=id)
        total_d, total_c, difference = calculate_totals(qayd_reade_details)
        context = {
            'qayd_reade': qayd_reade,
            'qayd_reade_details': qayd_reade_details,
            'total_d': total_d,
            'total_c': total_c,
            'difference': difference,
        }
        return render(request, 'accounts/qayd_reade.html', context)

@login_required 
def qayd_delete(request, id):
    """ د دالة حذف قيد """
    if not request.user.has_perm('accounts.delete_qayd'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة لحذف القيود المحاسبية.")
        return redirect('qayds')
    if request.user.is_authenticated and not request.user.is_anonymous:
        qayd_id = Qayd.objects.get(id=id)
        if 'btndelete' in request.POST:
            qayd_id.delete()
            messages.success(request, f'تم حذف القيد {id} بنجاح')
            return redirect('qayds')
    else:
        messages.error(request, 'الرجاء تسجيل الدخول أولاً')
    
    qayd_id_details = QaydDetails.objects.filter(qaydID=id)
    total_d, total_c, difference = calculate_totals(qayd_id_details)

    context = {
        'qayd_id': qayd_id,
        'qayd_id_details': qayd_id_details,
        'total_d': total_d,
        'total_c': total_c,
        'difference': difference,
    }
    return render(request, 'accounts/qayd_delete.html', context)

# دالة تحديث بيانات قيد موجود
@login_required 
def qayd_update(request, id):
    if not request.user.has_perm('accounts.change_qayd'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة لتعديل القيود المحاسبية.")
        return redirect('qayds')
    
    # التحقق من وجود current_company_id في الجلسة قبل استخدامه.
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'لم يتم تحديد الشركة الحالية.')
        return redirect('invoices_sales')
    
    qayd_update = get_object_or_404(Qayd, id=id)
    # استخدام formset للحصول على جميع نماذج QaydDetails المرتبطة بـ Qayd المحدد
    QaydDetailsFormSet = modelformset_factory(QaydDetails, form=QaydDetailsForm, extra=1)
    queryset = QaydDetails.objects.filter(qaydID=qayd_update)

    if request.method == 'POST':
        head_form = QaydForm(request.POST, request.FILES, instance=qayd_update)
        formset = QaydDetailsFormSet(
            request.POST, 
            queryset=queryset, 
            form_kwargs={'companyID': current_company_id}  # تمرير companyID للنموذج
        )

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
                body.qaydID = head
                body.save()

          messages.success(request, f'تم تحديث بيانات القيد {id} بنجاح')
          return redirect('qayds')
        else:
            # دالة عرض الأخطاء
            handle_form_errors(head_form, formset, request)
    else:
        head_form = QaydForm(instance=qayd_update)
        formset = QaydDetailsFormSet(
            queryset=queryset,  # لا توجد بيانات افتراضية
            form_kwargs={'companyID': current_company_id}  # تمرير companyID للنموذج
        )
    total_d, total_c, difference = calculate_totals(queryset)
    context = {
        'qayd_update': qayd_update,
        'head_form': head_form,
        'formset':formset,
        'total_d': total_d,
        'total_c': total_c,
        'difference': difference,
    }
    return render(request, 'accounts/qayd_update.html', context)

# دالة عرض جميع القيود
@login_required
def qayds(request):
    """
    عرض جميع الكائنات من نموذج Qayd في صفحة qayds.html.
    يجب أن يكون المستخدم مسجلاً للدخول للوصول إلى هذه الصفحة.
    """
    # التحقق من الأذونات أولاً
    if not request.user.has_perm('accounts.view_qayd'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة للإطلاع على القيود المحاسبية.")
        return redirect('index')
    
    # الحصول على الشركة الحالية من جلسة المستخدم
    current_company_id = request.session.get('current_company_id')
    
    if not current_company_id:
        messages.error(request, 'الرجاء تحديد الشركة للعمل عليها.')
        return redirect('companys')

    # الحصول على القيود الخاصة بالشركة الحالية
    try:
        qayds_list = Qayd.objects.filter(companyID_id=current_company_id)
    except Qayd.DoesNotExist:
        qayds_list = []  # إذا لم يكن هناك أي كائنات، العودة إلى قائمة فارغة
    
    # إعداد السياق
    context = {
        'qayds': qayds_list,
    }
    
    # عرض الصفحة مع البيانات
    return render(request, 'accounts/qayds.html', context)

@login_required
def generate_qayd_pdf(request, id):
    # احصل على القيد والتفاصيل الخاصة به من قاعدة البيانات
    qayd = Qayd.objects.get(id=id)  # تأكد من أنك تحصل على Qayd وليس QaydDetails
    qayd_details = qayd.details.all()  # استخدام 'details' بدلاً من 'qayddetails_set'
    # إنشاء مستند PDF
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    # إعداد الأنماط
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    heading_style = styles['Heading2']
    normal_style = styles['Normal']
    # إضافة ترويسة
    elements.append(Paragraph("تفاصيل القيد", title_style))
    elements.append(Paragraph(f"رقم القيد: {qayd.id}", heading_style))
    elements.append(Paragraph(f"date القيد: {qayd.date}", normal_style))
    elements.append(Paragraph(f"أنشأه: {qayd.created_by}", normal_style))
    elements.append(Paragraph("<br/><br/>", normal_style))  # إضافة مسافة
    # إعداد جدول التفاصيل
    data = [['العملة', 'المدين', 'الدائن']]
    for detail in qayd_details:
        data.append([
            f"{detail.debit:.2f}",
            f"{detail.credit:.2f}"
        ])
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    # بناء ملف PDF
    doc.build(elements)
    buffer.seek(0)
    # إرجاع استجابة PDF
    return FileResponse(buffer, as_attachment=True, filename='qayd.pdf')


#------------------- التقارير ---------------------


@login_required
def account_statement_search(request):
    # الحصول على معايير البحث من الطلب
    search_name = request.GET.get('search_name', '')
    search_invoice_number = request.GET.get('search_invoice_number', '')
    search_date = request.GET.get('search_date', '')
    search_currencyID = request.GET.get('currencyID', '')
    search_inventoryID = request.GET.get('inventoryID', '')
    search_customerID = request.GET.get('customerID', '')
    start_date = request.GET.get('start_date','')
    end_date = request.GET.get('end_date','')
    
    invoices_query = QaydDetailsForm.objects.all()
    # استعلام الفواتير بين تاريخين
    if start_date and end_date:
        invoices_query = invoices_query.filter(date__range=[start_date, end_date])
    if search_date:
        invoices_query = invoices_query.filter(date=search_date)
    if search_name:
        invoices_query = invoices_query.filter(customerID__legalPersonID__name_ar__icontains=search_name)
    if search_invoice_number:
        invoices_query = invoices_query.filter(sequence=search_invoice_number)
    if search_currencyID:
        invoices_query = invoices_query.filter(currencyID=search_currencyID)
    if search_inventoryID:
        invoices_query = invoices_query.filter(inventoryID=search_inventoryID)
    if search_customerID:
        invoices_query = invoices_query.filter(customerID=search_customerID)
    
    # الحصول على الشركة الحالية من الجلسة
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'الرجاء تحديد الشركة للعمل عليها.')
        return redirect('companys')

    # تصفية الفواتير بناءً على الشركة الحالية
    invoices_query = invoices_query.filter(companyID_id=current_company_id).annotate(
        total_sum=Sum('sales_invoice__total_price_after_tax')).order_by("-id")

      # حساب الإجمالي الكلي لجميع الفواتير
    total_invoices_sum = invoices_query.aggregate(total_sum=Sum('sales_invoice__total_price_after_tax'))['total_sum'] or 0

    # إعداد السياق
    context = {
        'invoices': invoices_query,
        'invoice_search_form': QaydDetailsForm(request.GET),
        'total_invoices_sum':total_invoices_sum,
    }

    # عرض الصفحة مع البيانات
    return render(request, 'accounts/account_statement.html', context)

@login_required 
def account_statement(request):
    if not request.user.has_perm('accounts.view_qayd'):
        messages.info(request, f" عذراً {request.user} ، ليس لديك الأذونات اللازمة للإطلاع على كشوفات الحساب.")
        return redirect('qayds')
    
    if request.user.is_authenticated and not request.user.is_anonymous:
        # الحصول على كافة التفاصيل مرتبة حسب التاريخ أو أي معيار آخر
        qayds_details = QaydDetails.objects.all().order_by('date_details')

        # إعداد قائمة لحفظ تفاصيل القيد مع الرصيد
        detailed_with_balance = []
        balance = 0

        for detail in qayds_details:
            balance += detail.debit - detail.credit
            detailed_with_balance.append({
                'detail': detail,
                'balance': balance
            })

        total_debit, total_credit, difference = calculate_totals(qayds_details)
        
        context = {
            'qayds_details': detailed_with_balance,
            'qayd_details_form': QaydDetailsForm(),
            'total_debit': total_debit,
            'total_credit': total_credit,
            'difference': difference,
        }
        return render(request, 'accounts/account_statement.html', context)




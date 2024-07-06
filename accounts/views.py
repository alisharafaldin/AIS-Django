
from typing import Any
from django.shortcuts import render , redirect, HttpResponse
from django.contrib import messages
from django.views.generic import CreateView
from . models import AccountsTree, Qayd, QaydDetails
from employees.models import EmpInfo
from . forms import AccountsTreeForm, QaydForm, QaydDetailsForm, QaydDetailsFormSet
from django.utils import timezone
from django.forms import modelformset_factory
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# class qaydCreate(CreateView):
#    model = Qayd
#    fields = "__all__" #تعبئة كل الحقول
#   #  fields = ['date','description'] #تعبئة جزء من الحقول
#    success_url = reverse_lazy({'qayd_list'}) #لإعادة توجيه إلى صفحة أخرى
#    form_class = QaydForm
#   #  success_url = reverse_lazy('qayds')
#   #  template_name = 'qayd_create' #لتحديد صفحة القالب 
#    pass
   
# class qaydDetail(DetailView):
#    model = Qayd
#   #  context_object_name = 'qayd' #المتغير الذي يستخدم في القالب

# class qaydUpdate(UpdateView):
#    model = Qayd
#    form_class = QaydForm
#   #  fields = ['description'] #تعبئة كل الحقول
#    template_name = 'accounts/qayd_update.html'
#    success_url = reverse_lazy({'qayd_list'}) #لإعادة توجيه إلى صفحة أخرى
#    def get_context_data(self, **kwargs):
#       context = super().get_context_data(**kwargs)
#       context['qayd_update_form'] = QaydForm()
#       context['qayd_update_details_form'] = QaydDetailsForm()
#       return context

# class qaydDelete(DeleteView):
#    model = Qayd
#    success_url = reverse_lazy({'qayd_list'}) #لإعادة توجيه إلى صفحة أخرى
   
# class qaydList(ListView):
#    model = Qayd
#   # queryset = Qayd.objects.order_by('date') #لترتيب البيانات
#   # ordering = ["-date"] #لترتيب البيانات
#   # context_object_name = 'qayds' #المتغير الذي يستخدم في القالب
#   # paginate_by = 

def account_create(request):
    if request.method == 'POST':
        add_acc = AccountsTreeForm(request.POST, request.FILES)
        if add_acc.is_valid():
            add_acc.save()
            messages.success(request, 'تمت الإضافة بنجاح') 
    context = {
        'acc_form': AccountsTreeForm(),
    }    
    return render(request,'accounts/account_create.html', context)

def account_reade(request, id):
    if request.user.is_authenticated and not request.user.is_anonymous:
      account_id = AccountsTree.objects.get(id=id)
    context = {
        'account':account_id,
    }
    return render(request, 'accounts/account_reade.html', context)

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

def accounts(request):
    accounts = AccountsTree.objects.all().order_by("typeID")
    accounts2 = accounts.order_by("code")
    context = {
        'accounts':accounts2,
    }    
    return render(request,'accounts/accounts.html', context)

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
    total_d = sum(item.debit for item in details_queryset)
    total_c = sum(item.credit for item in details_queryset)
    return total_d, total_c, total_d - total_c

# دالة إنشاء قيد جديد
def qayd_create(request):
    if request.method == 'POST':
      head_form = QaydForm(request.POST, request.FILES)
      formset = QaydDetailsFormSet(request.POST)

      if head_form.is_valid() and formset.is_valid():
        head = head_form.save(commit=False)
        head.created_by = request.user  # تعيين created_by فقط عند إنشاء قيد جديد
        head.save()

        for form in formset:
          if form.cleaned_data:  # تأكد من أن النموذج يحتوي على بيانات صالحة
            body = form.save(commit=False)
            body.qaydID = head  # استخدام head مباشرة بدلاً من head.instance
            body.save()
        messages.success(request, 'تمت الإضافة بنجاح')
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
        formset = QaydDetailsFormSet(queryset=QaydDetails.objects.none())
    context = {
       'head_form': head_form,
       'formset': formset,
    }
    return render(request, 'accounts/qayd_create.html', context)

# دالة عرض وقراءة قيد موجود مسبقاَ
def qayd_reade(request, id):
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

# دالة حذف قيد
def qayd_delete(request, id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        qayd_id = Qayd.objects.get(id=id)
        if 'btndelete' in request.POST:
            qayd_id.delete()
            messages.info(request, 'تم الحذف بنجاح')
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
    qayd_update = get_object_or_404(Qayd, id=id)
    # استخدام formset للحصول على جميع نماذج QaydDetails المرتبطة بـ Qayd المحدد
    QaydDetailsFormSet = modelformset_factory(QaydDetails, form=QaydDetailsForm, extra=1)
    queryset = QaydDetails.objects.filter(qaydID=qayd_update)

    if request.method == 'POST':
        head_form = QaydForm(request.POST, request.FILES, instance=qayd_update)
        formset = QaydDetailsFormSet(request.POST, queryset=queryset)

        if head_form.is_valid() and formset.is_valid():
          head = head_form.save(commit=False)
          head.updated_by = request.user
          head.save()

          for form in formset:
            if form.cleaned_data.get('DELETE', False):
                if form.instance.pk:
                    form.instance.delete()  # حذف النموذج من قاعدة البيانات
            else:
                body = form.save(commit=False)
                body.qaydID = head
                body.save()

          messages.success(request, 'تم التحديث بنجاح')
          return redirect('qayds')
        else:
            # دالة عرض الأخطاء
            handle_form_errors(head_form, formset, request)
    else:
        head_form = QaydForm(instance=qayd_update)
        formset = QaydDetailsFormSet(queryset=queryset)
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
    try:
        qayds_list = Qayd.objects.all()  # استعلام عن جميع الكائنات من نموذج Qayd

    except Qayd.DoesNotExist:
        qayds_list = []  # إذا لم يكن هناك أي كائنات، العودة إلى قائمة فارغة
    context = {
        'qayds': qayds_list,
    }
    return render(request, 'accounts/qayds.html', context)


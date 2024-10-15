from datetime import datetime
from django.contrib import messages
from .models import ItemType, ItemGrop, Items
from .forms import ItemTypeForm, ItemGropForm, ItemsForm
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect, get_object_or_404

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

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from django.contrib import messages

@login_required
@permission_required('items.add_items', raise_exception=True)
def product_create(request):
    # التحقق من وجود current_company_id مباشرة بعد الأذونات
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'لم يتم تحديد الشركة الحالية.')
        return redirect('sales')
    
    if request.method == 'POST':
        item_form = ItemsForm(request.POST, request.FILES)
        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.created_by = request.user
            item.save()
            messages.success(request, f'تم إضافة صنف جديد بإسم: {item.name_ar}')
            return redirect('customers')
        else:
            # دالة عرض الأخطاء (موجودة لديك لتجميع الأخطاء)
            handle_form_errors(item_form, request)
    else:
        item_form = ItemsForm()

    context = {
       'item_form': item_form,
       'item_label': item_form,
    }
    return render(request, 'products/product_create.html', context)

def items(request):
    pro = Items.objects.all()
    name = None
    desc = None
    pricefrom = None
    priceto = None
    cs = None
    if 'cs' in request.GET:
        cs = request.GET['cs']
        if not cs:
            cs = 'off'
    if 'searchname' in request.GET: # للتحقق من وجود نيم  في الرابط
        name = request.GET['searchname'] # تغذية المتغير بالمدخلات حسب النيم
        if name: # للتحقق أن البيانات ليست فارغة
            if cs=='on':
                pro = pro.filter(name__contains=name) #فلتر البيانات بالإسم مع مراعاة حساسية للأحرف
            else:
                pro = pro.filter(name__icontains=name) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 
    if 'searchdesc' in request.GET: # للتحقق من وجود نيم  في الرابط
        desc = request.GET['searchdesc'] # تغذية المتغير بالمدخلات حسب النيم
        if desc: # للتحقق أن البيانات ليست فارغة
            if cs =='on':
                pro = pro.filter(description__contains=desc) 
            else:
                pro = pro.filter(description__icontains=desc) 
    if 'searchpricefrom' in request.GET and 'searchpriceto' in request.GET: # للتحقق من وجود نيم  في الرابط
        pricefrom = request.GET['searchpricefrom'] # تغذية المتغير بالمدخلات حسب النيم
        priceto = request.GET['searchpriceto']# تغذية المتغير بالمدخلات حسب النيم
        if pricefrom and priceto: # للتحقق أن البيانات ليست فارغة
            if pricefrom.isdigit() and priceto.isdigit(): #للتأكد أن المدخلات رقم
                pro = pro.filter(price__gte=pricefrom , price__lte=priceto) # الإختصار gte يعني أكبر من أو يساوي
    context = {
        'products':pro
    }
    return render(request, 'products/products.html', context)

def Items(request, pro_id):
    context = {
        'pro':get_object_or_404(Items, pk=pro_id)
    }
    return render(request, 'products/product.html', context)

def search(request):
    return render(request, 'products/search.html')
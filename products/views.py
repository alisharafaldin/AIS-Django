from datetime import datetime
from django.contrib import messages
from .models import ItemType, ItemGrop, Items
from .forms import ItemTypeForm, ItemGropForm, ItemsForm
from django.shortcuts import get_object_or_404, render
from basicinfo.forms import SetComboBox
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from companys.models import Company
# Create your views here.
def handle_form_errors(Item_form, request):
    """وظيفة مساعد لمعالجة الأخطاء وعرض الرسائل المناسبة."""
    for field, errors in Item_form.errors.items():
        for error in errors:
            messages.error(request, f"خطأ في النموذج في الحقل '{field}': {error}")

def handle_formset_errors(Item_form, formset, request):
    """وظيفة مساعد لمعالجة الأخطاء وعرض الرسائل المناسبة."""
    for field, errors in Item_form.errors.items():
        for error in errors:
            messages.error(request, f"خطأ في نموذج الرأس في الحقل '{field}': {error}")
    for form_index, form in enumerate(formset.forms):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f"خطأ في نموذج التفاصيل {form_index + 1} في الحقل '{field}': {error}")
    for error in formset.non_form_errors():
        messages.error(request, f"خطأ في الـ FormSet: {error}")

@login_required
@permission_required('items.add_items', raise_exception=True)
def item_create(request):
    # التحقق من وجود current_company_id مباشرة بعد الأذونات
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'لم يتم تحديد الشركة الحالية.')
        return redirect('companys')
    
    if request.method == 'POST':
        item_form = ItemsForm(request.POST, request.FILES)
        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.created_by = request.user
            item.companyID = get_object_or_404(Company, id=current_company_id)
            item.save()
            messages.success(request, f'تم إضافة صنف جديد بإسم: {item.name_ar}')
            return redirect('items')
        else:
            # دالة عرض الأخطاء (موجودة لديك لتجميع الأخطاء)
            handle_form_errors(item_form, request)
    else:
        item_form = ItemsForm()

    context = {
       'item_form': item_form,
       'item_label': item_form,
    }
    return render(request, 'products/item_create.html', context)

@login_required 
@permission_required('items.update_items', raise_exception=True)
def item_update(request, id):
    item = get_object_or_404(Items, id=id)
    if request.method == 'POST':
        item_form = ItemsForm(request.POST, request.FILES, instance=item)
        if item_form.is_valid():
          item = item_form.save(commit=False)
          item.updated_by = request.user
          item.companyID = Company.objects.get(id=request.session.get('current_company_id'))
          item.save()
          messages.success(request, f'تم تحديث بيانات الصنف {item.name_ar} بنجاح')
          return redirect('items')

    context = {
        'item_form': item,
        'item_label': item,
    }
    return render(request, 'products/item_update.html', context)

@login_required
@permission_required('items.reade_items', raise_exception=True)
def item_reade(request, id):
    item_form =  get_object_or_404(Items, id=id)
    context = {
        'item_form': item_form,
       'item_label': item_form,  
    }
    return render(request, 'products/item_reade.html', context)

@login_required 
@permission_required('items.delete_items', raise_exception=True)
def item_delete(request, id):
    item = Items.objects.get(id=id)
    if 'btndelete' in request.POST:
        item.delete()
        messages.success(request, f'تم حذف الصنف {item.name_ar} بنجاح')
        return redirect('invoices_sales')
    context = {
        'item_form': item,
       'item_label': item,
    }
    return render(request, 'products/item_delete.html', context)

@login_required
@permission_required('items.delete_items', raise_exception=True)
def items(request):
    items = Items.objects.all().order_by("id")
    context = {
        'items':items,
        'SetComboBox': SetComboBox()
    }
    return render(request, 'products/items.html', context)

@login_required
def items_search(request):
    # الحصول على معايير البحث من الطلب
    search_name = request.GET.get('search_name', '')
    search_itemID = request.GET.get('itemID', '')
    search_itemGropID = request.GET.get('itemGropID', '')

    items_query = Items.objects.all()
    # استعلام الفواتير بين تاريخين
    if search_name:
        items_query = items_query.filter(name_ar=search_name)
    if search_itemID:
        items_query = items_query.filter(id=search_itemID)
    if search_itemGropID:
        items_query = items_query.filter(itemGropID=search_itemGropID) 
    
    # الحصول على الشركة الحالية من الجلسة
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'الرجاء تحديد الشركة للعمل عليها.')
        return redirect('companys')

   # الحصول على الأصناف الخاصة بالشركة الحالية
    items = items_query.filter(companyID_id=current_company_id).order_by("-id")
    
    # إعداد السياق
    context = {
        'items': items,
        'SetComboBox': SetComboBox(request.GET),
        'search_name': search_name,  # تمرير معايير البحث إلى القالب
        'search_itemID': search_itemID,  # تمرير معايير البحث إلى القالب
        'search_itemGropID': search_itemGropID,  # تمرير معايير البحث إلى القالب
    }
    return render(request, 'products/items.html', context)



from datetime import datetime
from django.contrib import messages
from .models import Inventory
from .forms import InventoryForm
from django.shortcuts import get_object_or_404, render
from basicinfo.forms import SetComboBox
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from companys.models import Company
# Create your views here.
def handle_form_errors(inventory_form, request):
    """وظيفة مساعد لمعالجة الأخطاء وعرض الرسائل المناسبة."""
    for field, errors in inventory_form.errors.inventorys():
        for error in errors:
            messages.error(request, f"خطأ في النموذج في الحقل '{field}': {error}")

def handle_formset_errors(inventory_form, formset, request):
    """وظيفة مساعد لمعالجة الأخطاء وعرض الرسائل المناسبة."""
    for field, errors in inventory_form.errors.inventorys():
        for error in errors:
            messages.error(request, f"خطأ في نموذج الرأس في الحقل '{field}': {error}")
    for form_index, form in enumerate(formset.forms):
        for field, errors in form.errors.inventorys():
            for error in errors:
                messages.error(request, f"خطأ في نموذج التفاصيل {form_index + 1} في الحقل '{field}': {error}")
    for error in formset.non_form_errors():
        messages.error(request, f"خطأ في الـ FormSet: {error}")

@login_required
@permission_required('inventorys.add_inventorys', raise_exception=True)
def inventory_create(request):
    # التحقق من وجود current_company_id مباشرة بعد الأذونات
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'لم يتم تحديد الشركة الحالية.')
        return redirect('companys')
    
    if request.method == 'POST':
        inventory_form = InventoryForm(request.POST, request.FILES)
        if inventory_form.is_valid():
            inventory = inventory_form.save(commit=False)
            inventory.created_by = request.user
            inventory.companyID = get_object_or_404(Company, id=current_company_id)
            inventory.save()
            messages.success(request, f'تم إضافة مخزن جديد بإسم: {inventory.name_ar}')
            return redirect('inventorys')
        else:
            # دالة عرض الأخطاء (موجودة لديك لتجميع الأخطاء)
            handle_form_errors(inventory_form, request)
    else:
        inventory_form = InventoryForm()

    context = {
       'inventory_form': inventory_form,
       'inventory_label': inventory_form,
    }
    return render(request, 'inventorys/inventory_create.html', context)

@login_required 
@permission_required('inventorys.update_inventorys', raise_exception=True)
def inventory_update(request, id):
    inventory = get_object_or_404(Inventory, id=id)
    if request.method == 'POST':
        inventory_form = InventoryForm(request.POST, request.FILES, instance=inventory)
        if inventory_form.is_valid():
          inventory = inventory_form.save(commit=False)
          inventory.updated_by = request.user
          inventory.companyID = Company.objects.get(id=request.session.get('current_company_id'))
          inventory.save()
          messages.success(request, f'تم تحديث بيانات المخزن {inventory.name_ar} بنجاح')
          return redirect('inventorys')
    inventory_form = InventoryForm(instance=inventory)
    context = {
        'inventory':inventory,
        'inventory_form': inventory_form,
        'inventory_label': InventoryForm(),
    }
    return render(request, 'inventorys/inventory_update.html', context)

@login_required
@permission_required('inventorys.reade_inventorys', raise_exception=True)
def inventory_reade(request, id):
    inventory_form =  get_object_or_404(Inventory, id=id)
    context = {
       'inventory':inventory_form,
        'inventory_form': inventory_form,
        'inventory_label': InventoryForm(), 
    }
    return render(request, 'inventorys/inventory_reade.html', context)

@login_required 
@permission_required('inventorys.delete_inventorys', raise_exception=True)
def inventory_delete(request, id):
    inventory = Inventory.objects.get(id=id)
    if 'btndelete' in request.POST:
        inventory.delete()
        messages.success(request, f'تم حذف المخزن {inventory.name_ar} بنجاح')
        return redirect('invoices_sales')
    context = {
        'inventory':inventory,
        'inventory_form': inventory,
        'inventory_label': InventoryForm(),
    }
    return render(request, 'inventorys/inventory_delete.html', context)

@login_required
@permission_required('inventorys.delete_inventorys', raise_exception=True)
def inventorys(request):
    inventory = Inventory.objects.all().order_by("id")
    context = {
        'inventorys':inventory,
        'SetComboBox': SetComboBox()
    }
    return render(request, 'inventorys/inventorys.html', context)

@login_required
def inventorys_search(request):
    # الحصول على معايير البحث من الطلب
    search_name = request.GET.get('search_name', '')
    search_inventoryID = request.GET.get('inventoryID', '')
    inventorys_query = Inventory.objects.all()
    # استعلام الفواتير بين تاريخين
    if search_name:
        inventorys_query = inventorys_query.filter(name_ar=search_name)
    if search_inventoryID:
        inventorys_query = inventorys_query.filter(id=search_inventoryID) 
    
    # الحصول على الشركة الحالية من الجلسة
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'الرجاء تحديد الشركة للعمل عليها.')
        return redirect('companys')

   # الحصول على الأصناف الخاصة بالشركة الحالية
    inventorys = inventorys_query.filter(companyID_id=current_company_id).order_by("-id")
    
    # إعداد السياق
    context = {
        'inventorys': inventorys,
        'SetComboBox': SetComboBox(request.GET),
        'search_name': search_name,  # تمرير معايير البحث إلى القالب
        'search_inventoryID': search_inventoryID,  # تمرير معايير البحث إلى القالب
    }
    return render(request, 'inventorys/inventorys.html', context)

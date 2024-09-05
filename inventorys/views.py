# Create your views here.
from django.db.models import Sum
from django.shortcuts import render, redirect
from sales.models import InvoicesSalesBody
from django.contrib import messages
from purchases.models import InvoicesPurchasesBody
from products.models import Items
from basicinfo.forms import InvoiceSearchForm

def product_quantity_summary(request):
    # الحصول على الشركة الحالية من جلسة المستخدم
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'الرجاء تحديد الشركة للعمل عليها.')
        return redirect('companys')

    # الحصول على معايير البحث من الطلب
    search_date = request.GET.get('search_date', '')
    search_inventoryID = request.GET.get('inventoryID', '')
    search_ItemGrop = request.GET.get('ItemGrop', '')
    search_itemID = request.GET.get('itemID', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

    # إجمالي الكميات المشتراة لكل منتج
    purchased_quantities = InvoicesPurchasesBody.objects.filter(
        invoiceHeadID__companyID_id=current_company_id)
    
    if start_date and end_date:
        purchased_quantities = purchased_quantities.filter(invoiceHeadID__date__range=[start_date, end_date])
    if search_date:
        purchased_quantities = purchased_quantities.filter(invoiceHeadID__date=search_date)
    if search_inventoryID:
        purchased_quantities = purchased_quantities.filter(inventoryID=search_inventoryID)
    if search_itemID:
        purchased_quantities = purchased_quantities.filter(itemID=search_itemID)
    if search_ItemGrop:
        purchased_quantities = purchased_quantities.filter(itemID__itemGropID=search_ItemGrop)
    
    purchased_quantities = purchased_quantities.values('itemID').annotate(
        total_purchased_quantity=Sum('quantity'))

    # إجمالي الكميات المباعة لكل منتج
    sold_quantities = InvoicesSalesBody.objects.filter(
        invoiceHeadID__companyID_id=current_company_id)
    
    if start_date and end_date:
        sold_quantities = sold_quantities.filter(invoiceHeadID__date__range=[start_date, end_date])
    if search_date:
        sold_quantities = sold_quantities.filter(invoiceHeadID__date=search_date)
    if search_inventoryID:
        sold_quantities = sold_quantities.filter(inventoryID=search_inventoryID)
    if search_itemID:
        sold_quantities = sold_quantities.filter(itemID=search_itemID)
    if search_ItemGrop:
        sold_quantities = sold_quantities.filter(itemID__itemGropID=search_ItemGrop)

    sold_quantities = sold_quantities.values('itemID').annotate(
        total_sold_quantity=Sum('quantity'))

    # تحويل النتائج إلى قاموس لسهولة الوصول
    purchased_dict = {item['itemID']: item['total_purchased_quantity'] for item in purchased_quantities}
    sold_dict = {item['itemID']: item['total_sold_quantity'] for item in sold_quantities}

    # الحصول على قائمة بجميع المنتجات
    all_item_ids = set(purchased_dict.keys()).union(set(sold_dict.keys()))

    # إنشاء قائمة بالمقارنة
    items_comparison = []
    total_purchased_sum = 0
    total_sold_sum = 0
    total_difference_sum = 0

    for item_id in all_item_ids:
        purchased_qty = purchased_dict.get(item_id, 0)
        sold_qty = sold_dict.get(item_id, 0)
        difference = purchased_qty - sold_qty

        # حساب المجاميع الرأسية
        total_purchased_sum += purchased_qty
        total_sold_sum += sold_qty
        total_difference_sum += difference

        items_comparison.append({
            'item_id': item_id,
            'purchased_quantity': purchased_qty,
            'sold_quantity': sold_qty,
            'difference': difference
        })

    # جلب أسماء المنتجات
    items = Items.objects.filter(id__in=all_item_ids)
    items_names = {item.id: item.name_ar for item in items}

    # تحديث المقارنة بإضافة أسماء المنتجات
    for item in items_comparison:
        item['item_name'] = items_names.get(item['item_id'], 'غير معروف')

    # إضافة المجاميع الرأسية إلى السياق
    context = {
        'items_comparison': items_comparison,
        'total_purchased_sum': total_purchased_sum,  # مجموع الكميات المشتراة
        'total_sold_sum': total_sold_sum,  # مجموع الكميات المباعة
        'total_difference_sum': total_difference_sum,  # مجموع الفرق
        # 'search_inventory_id': search_inventory_id,  # تمرير معايير البحث إلى القالب
        # 'search_item_id': search_item_id,  # تمرير معايير البحث إلى القالب
        'search_form': InvoiceSearchForm(request.GET),
    }
    return render(request, 'inventorys/product_quantity_summary.html', context)
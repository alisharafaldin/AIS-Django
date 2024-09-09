# Create your views here.
from django.utils import timezone
from django.db.models import Sum , F,  DecimalField, ExpressionWrapper, Max
from decimal import Decimal
from django.shortcuts import render, redirect
from sales.models import InvoicesSalesBody
from django.contrib import messages
from purchases.models import InvoicesPurchasesBody
from products.models import Items
from basicinfo.forms import InvoiceSearchForm
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_date
from django.db.models import Sum

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

    # الحصول على معايير الترتيب من الطلب
    ordering = request.GET.get('ordering', 'item_name')  # الترتيب الافتراضي بناءً على اسم المنتج
    direction = request.GET.get('direction', 'asc')  # الاتجاه الافتراضي هو تصاعدي

    # تحديد حقل الترتيب والاتجاه
    if direction == 'desc':
        ordering = f'-{ordering}'

    # فلترة الكميات المشتراة والمباعة بناءً على معايير البحث
    purchased_quantities = InvoicesPurchasesBody.objects.filter(
        invoiceHeadID__companyID_id=current_company_id
    )
    
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

    sold_quantities = InvoicesSalesBody.objects.filter(
        invoiceHeadID__companyID_id=current_company_id
    )
    
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

    # ترتيب البيانات بناءً على معايير الترتيب بعد الفلترة
    items_comparison = sorted(items_comparison, key=lambda x: x[ordering.strip('-')], reverse=direction == 'desc')

    # إضافة المجاميع الرأسية إلى السياق
    context = {
        'items_comparison': items_comparison,
        'total_purchased_sum': total_purchased_sum,  # مجموع الكميات المشتراة
        'total_sold_sum': total_sold_sum,  # مجموع الكميات المباعة
        'total_difference_sum': total_difference_sum,  # مجموع الفرق
        'search_date': search_date,  # تمرير معايير البحث إلى القالب
        'start_date': start_date,  # تمرير معايير البحث إلى القالب
        'end_date': end_date,  # تمرير معايير البحث إلى القالب
        'search_itemID': search_itemID,  # تمرير معايير البحث إلى القالب
        'search_ItemGrop': search_ItemGrop,  # تمرير معايير البحث إلى القالب
        'search_inventoryID': search_inventoryID,  # تمرير معايير البحث إلى القالب
        'search_form': InvoiceSearchForm(request.GET),  # تمرير معايير البحث الحالية
        'ordering': ordering.strip('-'),  # تمرير ترتيب الحقل الحالي إلى القالب
        'direction': direction,  # تمرير اتجاه الترتيب الحالي إلى القالب
    }
    
    return render(request, 'inventorys/product_quantity_summary.html', context)


def net_sales(request):
    # الحصول على الشركة الحالية من جلسة المستخدم
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'الرجاء تحديد الشركة للعمل عليها.')
        return redirect('companys')

# الحصول على معايير البحث من الطلب
    search_date = request.GET.get('search_date', '')
    search_inventoryID = request.GET.get('inventoryID', '')
    search_itemGrop = request.GET.get('itemGropID', '')
    search_itemID = request.GET.get('itemID', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

    # الحصول على معايير الترتيب من الطلب
    ordering = request.GET.get('ordering', 'item_name')  # الترتيب الافتراضي بناءً على اسم المنتج
    direction = request.GET.get('direction', 'asc')  # الاتجاه الافتراضي هو تصاعدي

    # تحديد حقل الترتيب والاتجاه
    if direction == 'desc':
        ordering = f'-{ordering}'

    # فلترة الكميات المشتراة بناءً على معايير البحث
    purchased_quantities = InvoicesPurchasesBody.objects.filter(
        invoiceHeadID__companyID_id=current_company_id
    )

    if search_itemID:
        purchased_quantities = purchased_quantities.filter(itemID=search_itemID)
    if search_itemGrop:
        purchased_quantities = purchased_quantities.filter(itemID__itemGropID=search_itemGrop)

    # حساب أعلى سعر شراء لكل منتج
    max_purchase_prices = purchased_quantities.values('itemID').annotate(
        max_purchase_price=Max('unit_price')
    )

    # فلترة الكميات المباعة بناءً على معايير البحث
    sold_quantities = InvoicesSalesBody.objects.filter(
        invoiceHeadID__companyID_id=current_company_id
    )

    if start_date and end_date:
        sold_quantities = sold_quantities.filter(invoiceHeadID__date__range=[start_date, end_date])
    if search_date:
        sold_quantities = sold_quantities.filter(invoiceHeadID__date=search_date)
    if search_inventoryID:
        sold_quantities = sold_quantities.filter(inventoryID=search_inventoryID)
    if search_itemID:
        sold_quantities = sold_quantities.filter(itemID=search_itemID)
    if search_itemGrop:
        sold_quantities = sold_quantities.filter(itemID__itemGropID=search_itemGrop)

    # حساب الكميات المباعة
    sold_quantities = sold_quantities.values('itemID').annotate(
        total_sold_quantity=Sum('quantity'),
        total_sales_price=Sum(
            ExpressionWrapper(
                F('quantity') * F('unit_price') / F('invoiceHeadID__rate'),
                output_field=DecimalField()  # تأكد من استخدام DecimalField
            )
        )
    ).filter(total_sold_quantity__gt=0)  # استبعاد المنتجات التي ليس لها حركة بيع

    # تحويل النتائج إلى قاموس لسهولة الوصول
    max_purchase_prices_dict = {item['itemID']: Decimal(item['max_purchase_price']) for item in max_purchase_prices}
    sold_dict = {item['itemID']: item for item in sold_quantities}

    # الحصول على قائمة بجميع المنتجات
    all_item_ids = set(max_purchase_prices_dict.keys()).union(set(sold_dict.keys()))

    # إنشاء قائمة بالمقارنة
    items_comparison = []
    total_purchase_sum = Decimal('0.00')
    total_sales_sum = Decimal('0.00')
    total_net_sales_sum = Decimal('0.00')
    total_Profit_rate_sum = Decimal('0.00')

    for item_id in all_item_ids:
        max_purchase_price = max_purchase_prices_dict.get(item_id, Decimal('0.00'))
        sold_info = sold_dict.get(item_id, {})

        sold_qty = Decimal(sold_info.get('total_sold_quantity', '0'))  # تأكد من تحويل الكمية إلى Decimal
        sales_price = Decimal(sold_info.get('total_sales_price', '0'))  # تأكد من تحويل السعر إلى Decimal

        if sold_qty > 0:  # استبعاد العناصر التي ليس لها حركة بيع
            # حساب التكلفة الإجمالية
            cost_price = max_purchase_price * sold_qty

            # حساب صافي المبيعات
            net_sales = sales_price - cost_price

            Profit_rate = net_sales / cost_price * 100
            # حساب المجاميع الرأسية
            total_purchase_sum += cost_price
            total_sales_sum += sales_price
            total_net_sales_sum += net_sales
            total_Profit_rate_sum = total_net_sales_sum / total_purchase_sum * 100

            items_comparison.append({
                'item_id': item_id,
                'purchased_quantity': 0,  # نحتاج فقط الكميات المباعة
                'sold_quantity': sold_qty,
                'purchase_price': max_purchase_price,
                'sales_price': sales_price,
                'cost_price': cost_price,
                'net_sales': net_sales,
                'Profit_rate':Profit_rate
            })

    # جلب أسماء المنتجات
    items = Items.objects.filter(id__in=all_item_ids)
    items_names = {item.id: item.name_ar for item in items}

    # تحديث المقارنة بإضافة أسماء المنتجات
    for item in items_comparison:
        item['item_name'] = items_names.get(item['item_id'], 'غير معروف')

    # ترتيب البيانات بناءً على معايير الترتيب بعد الفلترة
    items_comparison = sorted(items_comparison, key=lambda x: x[ordering.strip('-')], reverse=direction == 'desc')

    # إضافة المجاميع الرأسية إلى السياق
    context = {
        'items_comparison': items_comparison,
        'total_purchase_sum': total_purchase_sum,  # مجموع التكلفة
        'total_sales_sum': total_sales_sum,  # مجموع المبيعات
        'total_net_sales_sum': total_net_sales_sum,  # مجموع صافي المبيعات
        'total_Profit_rate_sum': total_Profit_rate_sum,
        'search_date': search_date,  # تمرير معايير البحث إلى القالب
        'start_date': start_date,  # تمرير معايير البحث إلى القالب
        'end_date': end_date,  # تمرير معايير البحث إلى القالب
        'search_itemID': search_itemID,  # تمرير معايير البحث إلى القالب
        'search_itemGrop': search_itemGrop,  # تمرير معايير البحث إلى القالب
        'search_inventoryID': search_inventoryID,  # تمرير معايير البحث إلى القالب
        'search_form': InvoiceSearchForm(request.GET),  # تمرير معايير البحث الحالية
        'ordering': ordering.strip('-'),  # تمرير ترتيب الحقل الحالي إلى القالب
        'direction': direction,  # تمرير اتجاه الترتيب الحالي إلى القالب
        'now': timezone.now(),  # تأكد من تمرير الوقت الحالي
    }
    
    return render(request, 'inventorys/net_sales.html', context)

def net_sales_search(request):
    
    # الحصول على الشركة الحالية من جلسة المستخدم
    current_company_id = request.session.get('current_company_id')
    if not current_company_id:
        messages.error(request, 'الرجاء تحديد الشركة للعمل عليها.')
        return redirect('companys')

    # الحصول على معايير البحث من الطلب
    search_date = request.GET.get('search_date', '')
    search_inventoryID = request.GET.get('inventoryID', '')
    search_itemGrop = request.GET.get('itemGropID', '')
    search_itemID = request.GET.get('itemID', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

    # الحصول على معايير الترتيب من الطلب
    ordering = request.GET.get('ordering', 'item_name')  # الترتيب الافتراضي بناءً على اسم المنتج
    direction = request.GET.get('direction', 'asc')  # الاتجاه الافتراضي هو تصاعدي

    # تحديد حقل الترتيب والاتجاه
    if direction == 'desc':
        ordering = f'-{ordering}'

    # فلترة الكميات المشتراة بناءً على معايير البحث
    purchased_quantities = InvoicesPurchasesBody.objects.filter(
        invoiceHeadID__companyID_id=current_company_id
    )

    if search_itemID:
        purchased_quantities = purchased_quantities.filter(itemID=search_itemID)
    if search_itemGrop:
        purchased_quantities = purchased_quantities.filter(itemID__itemGropID=search_itemGrop)

    # حساب أعلى سعر شراء لكل منتج
    max_purchase_prices = purchased_quantities.values('itemID').annotate(
        max_purchase_price=Max('unit_price')
    )

    # فلترة الكميات المباعة بناءً على معايير البحث
    sold_quantities = InvoicesSalesBody.objects.filter(
        invoiceHeadID__companyID_id=current_company_id
    )

    if start_date and end_date:
        sold_quantities = sold_quantities.filter(invoiceHeadID__date__range=[start_date, end_date])
    if search_date:
        sold_quantities = sold_quantities.filter(invoiceHeadID__date=search_date)
    if search_inventoryID:
        sold_quantities = sold_quantities.filter(inventoryID=search_inventoryID)
    if search_itemID:
        sold_quantities = sold_quantities.filter(itemID=search_itemID)
    if search_itemGrop:
        sold_quantities = sold_quantities.filter(itemID__itemGropID=search_itemGrop)

    # حساب الكميات المباعة
    sold_quantities = sold_quantities.values('itemID').annotate(
        total_sold_quantity=Sum('quantity'),
        total_sales_price=Sum(
            ExpressionWrapper(
                F('quantity') * F('unit_price') / F('invoiceHeadID__rate'),
                output_field=DecimalField()  # تأكد من استخدام DecimalField
            )
        )
    ).filter(total_sold_quantity__gt=0)  # استبعاد المنتجات التي ليس لها حركة بيع

    # تحويل النتائج إلى قاموس لسهولة الوصول
    max_purchase_prices_dict = {item['itemID']: Decimal(item['max_purchase_price']) for item in max_purchase_prices}
    sold_dict = {item['itemID']: item for item in sold_quantities}

    # الحصول على قائمة بجميع المنتجات
    all_item_ids = set(max_purchase_prices_dict.keys()).union(set(sold_dict.keys()))

    # إنشاء قائمة بالمقارنة
    items_comparison = []
    total_purchase_sum = Decimal('0.00')
    total_sales_sum = Decimal('0.00')
    total_net_sales_sum = Decimal('0.00')

    for item_id in all_item_ids:
        max_purchase_price = max_purchase_prices_dict.get(item_id, Decimal('0.00'))
        sold_info = sold_dict.get(item_id, {})

        sold_qty = Decimal(sold_info.get('total_sold_quantity', '0'))  # تأكد من تحويل الكمية إلى Decimal
        sales_price = Decimal(sold_info.get('total_sales_price', '0'))  # تأكد من تحويل السعر إلى Decimal

        if sold_qty > 0:  # استبعاد العناصر التي ليس لها حركة بيع
            # حساب التكلفة الإجمالية
            cost_price = max_purchase_price * sold_qty

            # حساب صافي المبيعات
            net_sales = sales_price - cost_price

            # حساب المجاميع الرأسية
            total_purchase_sum += cost_price
            total_sales_sum += sales_price
            total_net_sales_sum += net_sales

            items_comparison.append({
                'item_id': item_id,
                'purchased_quantity': 0,  # نحتاج فقط الكميات المباعة
                'sold_quantity': sold_qty,
                'purchase_price': max_purchase_price,
                'sales_price': sales_price,
                'cost_price': cost_price,
                'net_sales': net_sales
            })

    # جلب أسماء المنتجات
    items = Items.objects.filter(id__in=all_item_ids)
    items_names = {item.id: item.name_ar for item in items}

    # تحديث المقارنة بإضافة أسماء المنتجات
    for item in items_comparison:
        item['item_name'] = items_names.get(item['item_id'], 'غير معروف')

    # ترتيب البيانات بناءً على معايير الترتيب بعد الفلترة
    items_comparison = sorted(items_comparison, key=lambda x: x[ordering.strip('-')], reverse=direction == 'desc')

    # إضافة المجاميع الرأسية إلى السياق
    context = {
        'items_comparison': items_comparison,
        'total_purchase_sum': total_purchase_sum,  # مجموع التكلفة
        'total_sales_sum': total_sales_sum,  # مجموع المبيعات
        'total_net_sales_sum': total_net_sales_sum,  # مجموع صافي المبيعات
        'search_date': search_date,  # تمرير معايير البحث إلى القالب
        'start_date': start_date,  # تمرير معايير البحث إلى القالب
        'end_date': end_date,  # تمرير معايير البحث إلى القالب
        'search_itemID': search_itemID,  # تمرير معايير البحث إلى القالب
        'search_itemGrop': search_itemGrop,  # تمرير معايير البحث إلى القالب
        'search_inventoryID': search_inventoryID,  # تمرير معايير البحث إلى القالب
        'search_form': InvoiceSearchForm(request.GET),  # تمرير معايير البحث الحالية
        'ordering': ordering.strip('-'),  # تمرير ترتيب الحقل الحالي إلى القالب
        'direction': direction,  # تمرير اتجاه الترتيب الحالي إلى القالب
    }
    
    return render(request, 'inventorys/net_sales.html', context)
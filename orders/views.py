from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Items
from orders.models import Order, OrderDetails, Payment
from django.utils import timezone
# Create your views here.

def add_to_cart(request):
    # للتحقق أن المنتج والكمية والسعر موجودين وأن يكون مسجل دخول وغير أنونيموس
    if 'pro_id' in request.GET and 'qty' in request.GET and 'price' in request.GET and  request.user.is_authenticated and not request.user.is_anonymous:
        pro_id = request.GET['pro_id']
        qty = request.GET['qty']
        # للتحقق أن المستخدم ليس له طلب غير مكتمل
        order = Order.objects.all().filter(userID=request.user, is_finished=False)
        #للتحقق أن المنتج المختار موجود
        if not Items.objects.all().filter(id=pro_id).exists():
            return redirect('products')
        #تجهيز المنتج المختار    
        pro = Items.objects.get(id=pro_id)
        if order:
            #يعني وجود طلب قديم غير مكتكمل
            old_order = Order.objects.get(userID=request.user, is_finished=False)
            # للتحقق من عدم تكرار المنتج في نفس الطلب
            if OrderDetails.objects.all().filter(orderID=old_order, productID=pro).exists():
                orderdetails = OrderDetails.objects.get(orderID=old_order, productID=pro)
                orderdetails.quantity += int(qty)
                orderdetails.save()
            else:
                orderdetails = OrderDetails.objects.create(productID=pro, orderID=old_order, price=pro.price, quantity=qty)
            messages.success(request, 'سيتم إضافة المنتج إلى الطلب الحالي')
                # messages.success(request, 'was added to cart for old order')
        else:
            #ليس له طلب قديم
            new_order = Order()
            new_order.userID = request.user
            new_order.order_date = timezone.now()
            new_order.is_finished = False
            new_order.save()# يجب حفظ الطلب أولاً ليتم إضافة التفاصيل
            orderdetails = OrderDetails.objects.create(productID=pro, orderID=new_order, price=pro.price, quantity=qty)
            messages.success(request, 'جاري عمل طلب جديد ..') 
            # messages.success(request, 'was added to cart for new order') 
        return redirect('/products/' + request.GET['pro_id'])
    else: 
        # في حال عدم تسجيل الدخول
        if 'pro_id' in request.GET:
            return redirect('/products/' + request.GET['pro_id'])
        else:
            messages.error(request, 'الرجاء تسجيل الدخول لإتمام طلب الشراء')
            return redirect('index')

def cart(request):
    context = None
    #للتحقق أن المستخدم مسجل دخول وليس مجهول
    if request.user.is_authenticated and not request.user.is_anonymous:
        # للتحقق من وجود طلب 
        if Order.objects.all().filter(userID=request.user, is_finished=False):
            #تحضير الطلبات والتفاصيل وإجمالي القيمة
            order = Order.objects.get(userID=request.user, is_finished=False)
            orderdetails = OrderDetails.objects.all().filter(orderID=order)
            total = 0
            for sub in orderdetails:
                total += sub.price * sub.quantity
            context = {
                'order':order,
                'orderdetails':orderdetails,
                'order_count': OrderDetails.objects.all(),
                'total':total,
            }
    return render(request, 'orders/cart.html', context)

def remove_from_cart(request, orderdetails_id):
    if request.user.is_authenticated and not request.user.is_anonymous and orderdetails_id:
        orderdetails = OrderDetails.objects.get(id=orderdetails_id)
        if orderdetails.orderID.userID.id==request.user.id:
            orderdetails.delete()
    return redirect('cart')

def add_qty(request, orderdetails_id):
    if request.user.is_authenticated and not request.user.is_anonymous and orderdetails_id:
        orderdetails = OrderDetails.objects.get(id=orderdetails_id)
        if orderdetails.orderID.userID.id==request.user.id:
            orderdetails.quantity += 1
            orderdetails.save()
    return redirect('cart')

def sub_qty(request, orderdetails_id):
    if request.user.is_authenticated and not request.user.is_anonymous and orderdetails_id:
        orderdetails = OrderDetails.objects.get(id=orderdetails_id)
        if orderdetails.orderID.userID.id==request.user.id:
            if orderdetails.quantity>1:
                orderdetails.quantity -= 1
                orderdetails.save()
    return redirect('cart')

def payment(request):
    context = None
    ship_address = None
    ship_phone = None
    cart_number = None
    expire = None
    security_code = None
    is_added = None
    # للتحقق أن الدالة بوست وأن المستخدم ضغط على ذر الدفع
    if request.method == 'POST' and 'btnpayment' in request.POST  and 'ship_address' in request.POST and 'ship_phone' in request.POST and 'cart_number' in request.POST and 'expire' in request.POST and 'security_code' in request.POST:
        #هنا عملية الدفع بعد الضغط على الذر

        ship_address = request.POST['ship_address']
        ship_phone = request.POST['ship_phone']
        cart_number = request.POST['cart_number']
        expire = request.POST['expire']
        security_code = request.POST['security_code']

           #للتحقق أن المستخدم مسجل دخول وليس مجهول
        if request.user.is_authenticated and not request.user.is_anonymous:
            # للتحقق من وجود طلب 
            if Order.objects.all().filter(userID=request.user, is_finished=False):
                #تحضير الطلبات والتفاصيل وإجمالي القيمة
                order = Order.objects.get(userID=request.user, is_finished=False)

                payment = Payment(
                orderID=order,
                ship_address=ship_address,
                ship_phone=ship_phone,
                cart_number=cart_number,
                expire=expire,
                security_code=security_code)

                payment.save()
                order.is_finished = True
                order.save()
                is_added = True

                messages.success(request, 'Your Order is Finished')

        context = {
            'ship_address':ship_address,
            'ship_phone':ship_phone,
            'cart_number':cart_number,
            'expire':expire,
            'security_code':security_code,
            'is_added':is_added,
        }
    else:
        #هنا العرض قبل الضغط على الدفع
        #للتحقق أن المستخدم مسجل دخول وليس مجهول
        if request.user.is_authenticated and not request.user.is_anonymous:
            # للتحقق من وجود طلب 
            if Order.objects.all().filter(userID=request.user, is_finished=False):
                #تحضير الطلبات والتفاصيل وإجمالي القيمة
                order = Order.objects.get(userID=request.user, is_finished=False)
                orderdetails = OrderDetails.objects.all().filter(orderID=order)
                total = 0
                for sub in orderdetails:
                    total += sub.price * sub.quantity
                context = {
                    'order':order,
                    'orderdetails':orderdetails,
                    'total':total,
                }
    return render(request, 'orders/payment.html', context)

def show_orders(request):
    context = None
    all_orders = None
    #للتحقق أن المستخدم مسجل دخول وليس مجهول
    if request.user.is_authenticated and not request.user.is_anonymous:
        # جلب جميع الطلبات الخاصة بالمستخدم
        all_orders = Order.objects.all().filter(userID=request.user)
        if all_orders:
            for x in all_orders:
                #تحضير الطلبات والتفاصيل وإجمالي القيمة
                order = Order.objects.get(id=x.id)
                orderdetails = OrderDetails.objects.all().filter(orderID=order)
                total = 0
                for sub in orderdetails:
                    total += sub.price * sub.quantity
                x.total = total
                x.items_count = orderdetails.count
    context = {'all_orders':all_orders}
    return render(request, 'orders/show_orders.html', context)


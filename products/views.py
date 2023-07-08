from django.shortcuts import get_object_or_404, render
from datetime import datetime
from .models import Product
# Create your views here.
def products(request):
    pro = Product.objects.all()
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

def product(request, pro_id):
    context = {
        'pro':get_object_or_404(Product, pk=pro_id)
    }
    return render(request, 'products/product.html', context)

def search(request):
    return render(request, 'products/search.html')
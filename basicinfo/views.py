from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from basicinfo.models import *
# Create your views here.

def basicinfo(request):
    return render(request , 'basicinfo/basicinfo.html')



# def sponser(request): 
#     context = {
#         'all_sponser':Sponser.objects.all(),
#         'all_company':Company.objects.all(),
#     }
#     return render(request, 'employees/sponser.html', context) 

# def add_sponser(request): 
#     new_sponser = Sponser()
#     new_sponser.sponsName = request.POST['sponsName']
#     new_sponser.companyID = request.POST['companyID']
#     new_sponser.save()
#     messages.success(request, 'تمت الإضافة بنجاح')
#     return redirect('sponser') 


# def generalsettings(request):
#     return render(request , 'employees/generalsettings.html')

# def countrie(request):
#     if request.method == 'POST' and 'btnsave' in request.POST:
#         new_countrie = Countries()
#         new_countrie.countryName_en = request.POST['countryName_en']
#         new_countrie.countryName_ar = request.POST['countryName_ar']
#         new_countrie.code = request.POST['code']
#         new_countrie.callKey = request.POST['callKey']
#         new_countrie.nationality = request.POST['nationality']
#         new_countrie.save()# يجب حفظ الطلب أولاً ليتم إضافة التفاصيل
#         messages.success(request, 'تمت إضافة دولة جديد بنجاح')
#     context = {'all_countrie':Countries.objects.all()}
#     return render(request, 'employees/countries.html', context)

# def delete_countrie(request, countrie_id):
#     if request.user.is_authenticated and not request.user.is_anonymous and countrie_id:
#         countrie = Countries.objects.get(id=countrie_id)
#         countrie.delete()
#         messages.error(request, 'تم حذف بيانات الدولة')
#     else:
#         messages.error(request, 'الرجاء تسجيل الدخول')
#     return redirect('countrie')

# def edit_countrie(request, countrie_id):
#     if request.user.is_authenticated and not request.user.is_anonymous and countrie_id:
#         countrie = Countries.objects.get(id=countrie_id)
#         context = {
#             'countryName_ar':countrie.countryName_ar,
#             'countryName_en':countrie.countryName_en,
#         }
#         messages.success(request, 'تمت تحديث البيانات بنجاح')
#         return render(request , 'employees/countries.html', context) 

# def gender(request): 
#     context = {
#         'all_gender':Gender.objects.all()
#     }
#     return render(request , 'employees/gender.html',context) 

# def add_gender(request): 
#     if request.method == 'POST' and request.POST['gender_ar'] and request.POST['gender_en']:
#         if 'btnsave' in request.POST:
#             new_gender = Gender()
#             new_gender.gender_ar = request.POST['gender_ar']
#             new_gender.gender_en = request.POST['gender_en']
#             new_gender.save()
#             messages.success(request, 'تمت الإضافة بنجاح')
#     return redirect('gender') 

# def edit_gender(request, gender_id):
#     if  request.user.is_authenticated and not request.user.is_anonymous and gender_id:
#         gender = Gender.objects.get(id=gender_id)
#         if request.method == 'POST' and 'btneditsave' in request.POST :
#             if request.POST['gender_ar'] and request.POST['gender_en']:
#                 gender.gender_ar = request.POST['gender_ar']
#                 gender.gender_en = request.POST['gender_en']
#                 gender.save()
#                 messages.success(request, 'تمت تحديث البيانات بنجاح')
#         else:
#             context = {
#                 'gender_ar':gender.gender_ar,
#                 'gender_en':gender.gender_en,
#                 'all_gender':Gender.objects.all(),
#             }
#             return render(request , 'employees/gender.html', context) 
#     messages.error(request, 'الرجاء تسجيل الدخول')

# def delete_gender(request, gender_id):
#     if request.user.is_authenticated and not request.user.is_anonymous and gender_id:
#         gender = Gender.objects.get(id=gender_id)
#         gender.delete()
#     else:
#         messages.error(request, 'الرجاء تسجيل الدخول')
#     return redirect('gender') 



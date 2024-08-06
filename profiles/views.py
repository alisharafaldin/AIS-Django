from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib import auth
from .models import UserProfile
from products.models import Items 
from .forms import UserProfileForm, UserForm
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

import re
# Create your views here.
def signup(request):
    if request.method == 'POST':
        user_profile_form = UserProfileForm(request.POST)
        if user_profile_form.is_valid():
            # حفظ المستخدم
            user = user_profile_form.save(commit=False)
            password = request.POST.get('password')
            user.set_password(password)
            user.save()
            
            # إنشاء وربط ملف UserProfile و Person مع المستخدم الجديد
            # UserProfile.objects.create(userID=user, personID=Person.objects.create())
            
            # يمكنك إجراء عمليات إضافية هنا مثل تسجيل الدخول تلقائيًا
            
            # توجيه المستخدم إلى الصفحة بعد التسجيل بنجاح
            return redirect('index')  # اسم العرض بعد تسجيل المستخدم بنجاح
    else:
        user_form = UserForm()
    
    context = {
        'user_form': user_form,
    }
    return render(request, 'profiles/signup.html', context)

def signin(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')

        if not username or not password:
            messages.error(request, 'الرجاء التحقق من إدخال إسم المستخدم وكلمة المرور')
            return redirect('signin')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if 'rememberme' not in request.POST:
                request.session.set_expiry(0)
            auth.login(request, user)
            messages.success(request, 'تم تسجيل الدخول بنجاح')
            return redirect('companys')
        else:
            messages.error(request, 'يوجد خطأ في إسم المستخدم أو كلمة المرور')
            return redirect('signin')
    else:
        return render(request, 'profiles/signin.html')

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(userID=request.user)

       # التحقق من أن كائن Person مرتبط بـ UserProfile، وإذا لم يكن كذلك، قم بإنشائه
    if user_profile.personID is None:
        # user_profile.personID = Person.objects.create()
        user_profile.save()

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        # person_form = PersonForm(request.POST, instance=user_profile)
        profile_form = UserProfileForm(request.POST, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            # person = person_form.save(commit=False)
            profile = profile_form.save(commit=False)

            # تحديث بيانات المستخدم
            user.set_password(request.POST['pass_field'])
            user.save()

            # تحديث بيانات العلومات العامة
            # person.save()

            # تحديث بيانات الملف الشخصي
            profile.save()
            
            messages.success(request, 'تم تحديث البيانات بنجاح')
            return redirect('profile')
        else:
            messages.error(request, 'الرجاء التحقق من البيانات المدخلة')
    else:
        user_form = UserForm(instance=request.user)
        # person_form = PersonForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)
    context = {
        'user_form': user_form,
        # 'person_form': person_form,
        'profile_form': profile_form,
    }
    return render(request, 'profiles/profile.html', context)

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('index')

def pro_fav(request, pro_id):
    # في حال تم تسجيل الدخول ولا يوجد مستخدم مجهول
    if request.user.is_authenticated and not request.user.is_anonymous:
        pro_fav = Items.objects.get(pk=pro_id)
        # للتحقق أن المنتج لم يتم إضافته في المفضلة من قبل نفس المستخدم
        if UserProfile.objects.filter(user=request.user ,Items_favorites=pro_fav).exists():
            messages.info(request, 'Already Items in the favorite list')
            messages.info(request, 'المنتج بالفعل في قائمة المفضلة')
        else:
            userprofile = UserProfile.objects.get(user=request.user)
            userprofile.Items_favorites.add(pro_fav)
            messages.success(request, 'Items has been favorited')
    else:
        messages.info(request, 'لإضافة المنتج في المفضلة يجب تسجيل الدخول أولاً')
    return redirect('/Itemss/' + str(pro_id))
    
def show_pro_fav(request):
    context = None
    # في حال تم تسجيل الدخول ولا يوجد مستخدم مجهول
    if request.user.is_authenticated and not request.user.is_anonymous:
        userInfo = UserProfile.objects.get(user=request.user)
        pro = userInfo.Items_favorites.all()
        context = { 'Itemss':pro }
    return render(request, 'Itemss/Itemss.html', context)

def user_reade(request, id):
  user_id = UserProfile.objects.get(id=id)
  context = {
    'user_reade':user_id,
  }
  return render(request, 'partials/_navbar.html', context)

class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        response = super().form_valid(form)
        # إضافة رسالة توضيحية هنا
        print("تم إرسال بريد إلكتروني لاستعادة كلمة المرور")
        return response


# def singup(request):
#     # في حال أن الرابط بوست وتم الضغط على زر حفظ
#     if request.method == 'POST' and 'btnsignup' in request.POST:
#         #variables for fildes
#         fname = None
#         lname = None
#         address = None
#         address2 = None
#         city = None
#         state = None
#         zip_number = None
#         email = None
#         username = None
#         password = None
#         terms = None
#         is_added = None
#         #Get Values from the form
#         if 'fname' in request.POST: fname = request.POST['fname']
#         else: messages.error(request, 'Error in first name')
#         if 'lname' in request.POST: lname = request.POST['lname']
#         else: messages.error(request, 'Error in last name')
#         if 'address' in request.POST: address = request.POST['address']
#         else: messages.error(request, 'Error in Address')
#         if 'address2' in request.POST: address2 = request.POST['address2']
#         else: messages.error(request, 'Error in Address 2')
#         if 'city' in request.POST: city = request.POST['city']
#         else: messages.error(request, 'Error in City')
#         if 'state' in request.POST: state = request.POST['state']
#         else: messages.error(request, 'Error in State')
#         if 'zip' in request.POST: zip_number = request.POST['zip']
#         else: messages.error(request, 'Error in Zip')
#         if 'email' in request.POST: email = request.POST['email']
#         else: messages.error(request, 'Error in Emila')
#         if 'user' in request.POST: username = request.POST['user']
#         else: messages.error(request, 'Error in username')
#         if 'pass' in request.POST: password = request.POST['pass']
#         else: messages.error(request, 'Error in password')
#         if 'terms' in request.POST: terms = request.POST['terms']
        
#         #Check the Values
#         if fname and lname and address and address2 and city and state and zip_number and email and username and password: 
#             if terms == 'on':
#                 #Check if username is taken
#                 if User.objects.filter(username=username).exists():
#                     messages.error(request, 'This username is taken')
#                 else:
#                     #Check if email is taken
#                     if User.objects.filter(email=email).exists():
#                         messages.error(request, 'This Email is taken')
#                     else:
#                        patt = "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$" 
#                        if re.match(patt, email):
#                             #add user
#                             user = User.objects.create_user(
#                                 first_name=fname,
#                                 last_name=lname,
#                                 email=email, 
#                                 username=username, 
#                                 password=password)
#                             user.save()
#                             #add user profile
#                             userprofile = UserProfile(
#                                 user=user,
#                                 address=address,
#                                 address2=address2,
#                                 city=city,
#                                 state=state,
#                                 zip_number=zip_number)
#                             userprofile.save()
#                             #Clear fields
#                             fname = ''
#                             lname = ''
#                             address = ''
#                             address2 = ''
#                             city = ''
#                             state = ''
#                             zip_number = ''
#                             email = ''
#                             username = ''
#                             password = ''
#                             terms = None
#                             #Success Message
#                             messages.success(request, 'Your Account is Created')
#                             is_added = True
#                        else:
#                         messages.error(request, 'Invalid Email')
#             else:
#                 messages.error(request, 'you must agree to the terms')
#         else:
#             messages.error(request, 'Check Empty Fieldes')
#         return render(request , 'profiles/signup.html', {
#             'fname' : fname,
#             'lname': lname,
#             'address': address,
#             'address2': address2,
#             'city': city,
#             'state': state,
#             'zip': zip_number,
#             'email': email,
#             'user': username,
#             'pass': password,
#             'is_added':is_added,
#         })
#     else:
#         return render(request , 'profiles/signup.html')

# def profile(request):
#     # تعديل الملف الشخصي
#     if request.method == 'POST' and 'btnsave' in request.POST:
#         # في حال التحقق من وجود مستخدم ولديه أي دي
#         if request.user is not None and request.user.id != None:
#             userprofile = UserProfile.objects.get(user=request.user)
#             # في حال وجود بيانات في الصفحة
#             if request.POST['fname'] and request.POST['lname'] and request.POST['address'] and request.POST['address2'] and request.POST['city'] and request.POST['state'] and request.POST['zip'] and request.POST['email'] and request.POST['user'] and request.POST['pass']:
#                 request.user.firest_name = request.POST['fname']
#                 request.user.last_name = request.POST['lname']
#                 userprofile.address = request.POST['address']
#                 userprofile.address2 = request.POST['address2']
#                 userprofile.city = request.POST['city']
#                 userprofile.state = request.POST['state']
#                 userprofile.zip_number = request.POST['zip']
#                 # request.user.email = request.POST['email']
#                 # request.user.username = request.POST['user']
#                 # في حال أن الباسوورد يبدأ بـ 'pbkdf2_sha256$'
#                 if not request.POST['pass'].startswith('pbkdf2_sha256$'):
#                     request.user.set_password(request.POST['pass'])
#                 request.user.save()
#                 userprofile.save()
#                 # auth.login(request, request.user)
#                 messages.success(request, 'تم تحديث البيانات بنجاح')
#             else:
#                 messages.error(request, 'Check your values and elements')
#         return redirect('profile')
#     else:
#         # في حال وجود مستخدم
#         if request.user is not None:
#             context = None
#             # في حال أن المستخدم ليس مجهول
#             if not request.user.is_anonymous:
#                 userprofile = UserProfile.objects.get(user=request.user)
#                 context = {
#                     'fname':request.user.first_name,
#                     'lname':request.user.last_name,
#                     'address':userprofile.address,
#                     'address2':userprofile.address2,
#                     'city':userprofile.city,
#                     'state':userprofile.state,
#                     'zip':userprofile.zip_number,
#                     'email':request.user.email,
#                     'user':request.user.username,
#                     'pass':request.user.password
#                 }
#             return render(request , 'profiles/profile.html', context)
#         else:
#             return redirect('profile')
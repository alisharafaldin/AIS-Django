from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib import auth
from .models import UserProfile
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
            # توجيه المستخدم إلى الصفحة بعد التسجيل بنجاح
            return redirect('index')  # اسم العرض بعد تسجيل المستخدم بنجاح
    else:
        user_form = UserForm()
        user_profile_form = UserProfileForm()
    context = {
        'user_form': user_form,
        'user_profile_form':user_profile_form,
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


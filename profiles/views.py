from django.contrib import auth
from .models import UserProfile
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserProfileForm, UserForm
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
import re


# دليل الأعمال

def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        user_profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and user_profile_form.is_valid():
            # حفظ المستخدم الجديد
            user = user_form.save()
            user.set_password(user_form.cleaned_data['password1'])
            user.save()

            # حفظ الملف الشخصي مع ربطه بالمستخدم الجديد
            user_profile = user_profile_form.save(commit=False)
            user_profile.userID = user  # تعيين userID للمستخدم الجديد
            user_profile.save()

            # تسجيل المستخدم بعد نجاح التسجيل
            login(request, user)
            messages.success(request, "تم التسجيل بنجاح")
            return redirect('index')
        else:
            # عرض رسائل الخطأ إذا كانت النماذج غير صالحة
            for field, errors in user_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            for field, errors in user_profile_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        user_form = UserCreationForm()
        user_profile_form = UserProfileForm()

    context = {
        'user_form': user_form,
        'user_profile_form': user_profile_form,
    }
    return render(request, 'dalilalaemal/profiles/signup.html', context)

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
        return render(request, 'dalilalaemal/profiles/signin.html')                           

@login_required
def profile(request):
    # جلب أو إنشاء كائن UserProfile للمستخدم الحالي
    user_profile, created = UserProfile.objects.get_or_create(userID=request.user)

    # التحقق من وجود كائن Person مرتبط بملف المستخدم، وإذا لم يكن موجودًا، نقوم بإنشائه
    if user_profile.userID is None:
        user_profile.userID = UserProfile.objects.create()  # إنشاء كائن Person جديد
        user_profile.save()  # حفظ التغييرات

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=user_profile)

        # التحقق من صحة البيانات في كلا النموذجين
        if user_form.is_valid() and profile_form.is_valid():
            # تحديث بيانات المستخدم
            user = user_form.save(commit=False)

            # التحقق مما إذا تم إدخال كلمة مرور جديدة وحقل التأكيد
            password = request.POST.get('pass_field')
            confirm_password = request.POST.get('confirm_pass_field')

            if password and password != "":
                # التحقق من تطابق كلمة المرور مع التأكيد
                if password == confirm_password:
                    user.set_password(password)
                    user.save()  # حفظ التغييرات في بيانات المستخدم
                    # تحديث الجلسة بحيث يبقى المستخدم مسجلاً للدخول بعد تغيير كلمة المرور
                    update_session_auth_hash(request, user)
                else:
                    # عرض رسالة خطأ إذا كانت كلمات المرور غير متطابقة
                    messages.error(request, 'كلمة المرور وتأكيد كلمة المرور غير متطابقتين.')
                    return redirect('profile')

            user.save()  # حفظ التغييرات في بيانات المستخدم

            # تحديث بيانات الملف الشخصي
            profile = profile_form.save(commit=False)
            profile.save()  # حفظ التغييرات في ملف المستخدم

            messages.success(request, 'تم تحديث البيانات بنجاح')
            return redirect('profile')  # إعادة توجيه المستخدم إلى صفحة الملف الشخصي
        else:
            messages.error(request, 'الرجاء التحقق من البيانات المدخلة')
    else:
        # إنشاء نماذج مع البيانات الحالية للمستخدم والملف الشخصي
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    # إرسال النماذج إلى القالب لعرضها
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'dalilalaemal/profile.html', context)

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


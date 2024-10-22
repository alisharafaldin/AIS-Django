from django.contrib import auth
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserProfileForm, UserForm, UserCreatForm
from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
import re

def handle_form_errors(head_form, request):
    """وظيفة مساعد لمعالجة الأخطاء وعرض الرسائل المناسبة."""
    for field, errors in head_form.errors.items():
        for error in errors:
            messages.error(request, f"خطأ في النموذج في الحقل '{field}': {error}")

def handle_formset_errors(head_form, formset, request):
    """وظيفة مساعد لمعالجة الأخطاء وعرض الرسائل المناسبة."""
    for field, errors in head_form.errors.items():
        for error in errors:
            messages.error(request, f"خطأ في نموذج الرأس في الحقل '{field}': {error}")
    for form_index, form in enumerate(formset.forms):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f"خطأ في نموذج التفاصيل {form_index + 1} في الحقل '{field}': {error}")
    for error in formset.non_form_errors():
        messages.error(request, f"خطأ في الـ FormSet: {error}")

def signup(request):
    if request.method == 'POST':
        user_creat_form = UserCreatForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_creat_form.is_valid() and profile_form.is_valid():
            # حفظ user_creat_form الجديد
            user = user_creat_form.save()

            # حفظ الملف الشخصي مع ربطه بالمستخدم الجديد
            user_profile = profile_form.save(commit=False)
            user_profile.userID = user  # تعيين userID للمستخدم الجديد
            user_profile.save()

            # تسجيل المستخدم بعد نجاح التسجيل
            login(request, user)
            messages.success(request, "تم التسجيل بنجاح")
            return redirect('dalil_home')
        else:
            # عرض رسائل الخطأ إذا كانت النماذج غير صالحة
            for field, errors in user_creat_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            for field, errors in profile_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        profile_form = UserProfileForm()
        user_creat_form = UserCreatForm()

    context = {
        'user_creat_form': user_creat_form,
        'profile_form': profile_form,
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
            return redirect('dalil_home')
        else:
            messages.error(request, 'يوجد خطأ في إسم المستخدم أو كلمة المرور')
            return redirect('signin')
    else:
        return render(request, 'dalilalaemal/profiles/signin.html')                           

@login_required
def profile(request):
    user = get_object_or_404(User, id=request.user.id)
    user_profile =  get_object_or_404(UserProfile, userID=user)
    context = {
        'user': user,
        'user_profile': user_profile,
    }
    return render(request, 'dalilalaemal/profiles/profile.html', context)

@login_required
def profile_update(request, id):
    # user_profile, created = UserProfile.objects.get_or_create(userID=request.user)
    # user = get_object_or_404(User, id=request.user.id)
    user_profile =  get_object_or_404(UserProfile, userID__id=id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=user_profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            # حفظ بيانات الملف الشخصي، مع التأكد من أن userID مرتبط بالمستخدم الحالي
            profile = profile_form.save(commit=False)  # لا تحفظ مباشرة حتى نربط userID
            profile.userID = request.user  # تعيين userID
            profile.save()
            messages.success(request, 'تم تحديث البيانات بنجاح.')
            return redirect('profile')
        else:
            handle_form_errors(user_form, request)
            handle_form_errors(profile_form, request)
            messages.error(request, 'الرجاء تصحيح الأخطاء في النموذج.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'dalilalaemal/profiles/profile_update.html', context)

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

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # لإبقاء المستخدم مسجلاً بعد تغيير كلمة المرور
            messages.success(request, 'تم تغيير كلمة المرور بنجاح.')
            return redirect('profile')
        else:
            messages.error(request, 'الرجاء تصحيح الأخطاء في النموذج.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})


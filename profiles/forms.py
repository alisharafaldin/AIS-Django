from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import UserCreationForm

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {
            'nationalityID': forms.Select(attrs={'class':'form-control', 'placeholder':'الجنسية'}),
            'countryID': forms.Select(attrs={'class':'form-control', 'placeholder':'بلد الإقامة'}),
            'genderID': forms.Select(attrs={'class':'form-control', 'placeholder':'الجنس'}),
            'dateOfBirth': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'placeholder':'تاريخ الميلاد'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الهاتف'}),
            'phoneOther': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم هاتف آخر'}),
            'photo': forms.ClearableFileInput(attrs={'class':'form-control', 'placeholder':'صورة شخصية'}),
            'terms': forms.CheckboxInput(attrs={'class':'form-control', 'style':'width: auto', 'placeholder':'الشروط'}),
            'active': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'نشط'}),
        }

class UserForm(forms.ModelForm):
    pass_field = forms.CharField(widget=forms.PasswordInput, required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'إسم المستخدم'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'البريد الإلكتروني'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الأخير'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الأول'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'كلمة المرور'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تأكيد كلمة المرور'}),
        }

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'كلمة المرور الجديدة'}),
        label="كلمة المرور الجديدة"
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تأكيد كلمة المرور الجديدة'}),
        label="تأكيد كلمة المرور الجديدة"
    )
class CustomUserCreationForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'كلمة المرور الجديدة'}),
        label="كلمة المرور الجديدة"
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تأكيد كلمة المرور الجديدة'}),
        label="تأكيد كلمة المرور الجديدة"
    )

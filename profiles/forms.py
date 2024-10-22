from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import UserCreationForm
from basicinfo.models import Countries

class UserProfileForm(forms.ModelForm):
       
    countryID = forms.ModelChoiceField(
        queryset=Countries.objects.all(),
        label='بلد الإقامة',
        empty_label="بلد الإقامة",
        required=False,
        widget=forms.Select(attrs={'name':'search_currencyID', 'class':'form-control', 'placeholder':'بلد الإقامة'})
    )
    nationalityID = forms.ModelChoiceField(
        queryset=Countries.objects.all(),
        label='الموطن الأصلي',
        empty_label="الموطن الأصلي",
        required=False,
        widget=forms.Select(attrs={'name':'search_currencyID', 'class':'form-control', 'placeholder':'الموطن الأصلي'})
    )
    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {
            'genderID': forms.Select(attrs={'class':'form-control', 'placeholder':'الجنس'}),
            'dateOfBirth': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'placeholder':'تاريخ الميلاد'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الهاتف'}),
            'phoneOther': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم هاتف آخر'}),
            'photo': forms.ClearableFileInput(attrs={'class':'form-control', 'placeholder':'صورة شخصية'}),
            'terms': forms.CheckboxInput(attrs={'class':'form-control', 'style':'width: auto', 'placeholder':'الشروط'}),
            'active': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'نشط'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'إسم المستخدم'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'البريد الإلكتروني'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الأول'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الأخير'}),
        }

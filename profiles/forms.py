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


class UserCreatForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'البريد الإلكتروني'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الإسم الأول'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الإسم الأخير'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'إسم المستخدم'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'كلمة المرور'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'تأكيد كلمة المرور'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserCreatForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'كلمة المرور'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تأكيد كلمة المرور'})

    def save(self, commit=True):
        user = super(UserCreatForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

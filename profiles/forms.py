from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
  class Meta:
      model = UserProfile
      fields = '__all__'
   

class UserForm(forms.ModelForm):
    pass_field = forms.CharField(widget=forms.PasswordInput, required=False)
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الأول'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الأخير'}),
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'إسم المستخدم'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'البريد الإلكتروني'}),
            'password': forms.TextInput(attrs={'class':'form-control', 'placeholder':'كلمة المرور'}),
            'password2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'تأكيد كلمة المرور'}),
        }
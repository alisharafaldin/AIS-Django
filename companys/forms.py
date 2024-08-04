from django import forms
from .models import Company, CompanyUser

class CompanyForm (forms.ModelForm):
  class Meta:
      model = Company
      fields = '__all__'
      
class CompanyUserForm (forms.ModelForm):
  class Meta:
      model = CompanyUser
      fields = '__all__'
      widgets = {
        'companyID': forms.Select(attrs={'class':'form-control', 'placeholder':'الشركة'}),
        'userID': forms.Select(attrs={'class':'form-control', 'placeholder':'المستخدم'}),
        'jobTitleID': forms.Select(attrs={'class':'form-control', 'placeholder':'المسمى الوظيفي'}),
    }

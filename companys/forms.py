from django import forms
from .models import Company, CompanyUser

class CompanyForm (forms.ModelForm):
  class Meta:
      model = Company
      fields = '__all__'
      widgets = {
        'name_ar': forms.TextInput(attrs={'class':'form-control','placeholder':'إسم الشركة عربي'}),
        'acronym_ar': forms.TextInput(attrs={'class':'form-control','placeholder':'الإسم المختصر عربي'}),
        'name_en': forms.TextInput(attrs={'class':'form-control','placeholder':'إسم الشركة إنجليزي'}),
        'acronym_en': forms.TextInput(attrs={'class':'form-control','placeholder':'الإسم المختصر إنجليزي'}),
        'who_are_we': forms.TextInput(attrs={'class':'form-control', 'placeholder':'من نحن'}),
        'businessTypeID': forms.Select(attrs={'class':'form-control', 'placeholder':'نوع الشركة'}),
        'countryID': forms.Select(attrs={'class':'form-control', 'placeholder':'الدولة'}),
        'regionID': forms.Select(attrs={'class':'form-control', 'placeholder':'المنطقة'}),
        'stateID': forms.Select(attrs={'class':'form-control', 'placeholder':'الولاية'}),
        'cityID': forms.Select(attrs={'class':'form-control', 'placeholder':'المدينة'}),
        'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'عنوان مقر الشركة'}),
        'google_maps_location': forms.URLInput(attrs={'class':'form-control', 'placeholder':'العوان على خرائط قوقل'}),
        'administrator': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الموظف المسؤول'}),
        'bankID': forms.Select(attrs={'class':'form-control', 'placeholder':'البنك'}),
        'branchBankID': forms.Select(attrs={'class':'form-control', 'placeholder':'الفرع'}),
        'typeAccBankID': forms.Select(attrs={'class':'form-control', 'placeholder':'نوع الحساب'}),
        'accountNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الحساب'}),
        'IBANNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الآيبان'}),
        'accountName': forms.TextInput(attrs={'class':'form-control', 'placeholder':'حساب البنك بإسم'}),
        'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الهاتف'}),
        'phoneOther': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم هاتف آخر'}),
        'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'البريد الإلكتروني'}),
        'website': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'الموقع الإلكتروني'}),
        'fax': forms.TextInput(attrs={'class':'form-control', 'placeholder':'فاكس'}),
        'POBox': forms.TextInput(attrs={'class':'form-control', 'placeholder':'صندوق بريد'}),
        'logo': forms.ClearableFileInput(attrs={'class':'form-control', 'placeholder':'شعار الشركة'}),
        'taxNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الرقم الضريبي'}),
        'active': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'نشط'}),
        'notes': forms.TextInput(attrs={'class':'form-control', 'placeholder':'ملاحظات'}),
    }
      
class CompanyUserForm (forms.ModelForm):
  class Meta:
      model = CompanyUser
      fields = '__all__'
      widgets = {
        'companyID': forms.Select(attrs={'class':'form-control', 'placeholder':'الشركة'}),
        'userID': forms.Select(attrs={'class':'form-control', 'placeholder':'المستخدم'}),
        'jobTitleID': forms.Select(attrs={'class':'form-control', 'placeholder':'المسمى الوظيفي'}),
    }

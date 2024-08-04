from django import forms
from .models import Persons, LegalPersons, BasicInfo

class BasicInfoForm(forms.ModelForm):
    class Meta:
        model = BasicInfo
        fields = '__all__'
        widgets = {
            'basicInfoID': forms.Select(attrs={'class':'form-control', 'placeholder':'المعلومات الأساسية'}),
            'nationalityID': forms.Select(attrs={'class':'form-control', 'placeholder':'الجنسية'}),
            'countryID': forms.Select(attrs={'class':'form-control', 'placeholder':'الدولة'}),
            'regionID': forms.Select(attrs={'class':'form-control', 'placeholder':'المنطقة'}),
            'stateID': forms.Select(attrs={'class':'form-control', 'placeholder':'الولاية'}),
            'cityID': forms.Select(attrs={'class':'form-control', 'placeholder':'المدينة'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'وصف العنوان '}),
            'google_maps_location': forms.URLInput(attrs={'class':'form-control', 'placeholder':'العوان على خرائط قوقل'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الهاتف'}),
            'phoneOther': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم هاتف آخر'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'إيميل'}),
            'website': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'الموقع الإلكتروني'}),
            'fax': forms.TextInput(attrs={'class':'form-control', 'placeholder':'فاكس'}),
            'POBox': forms.TextInput(attrs={'class':'form-control', 'placeholder':'صندوق بريد'}),
            'bankID': forms.Select(attrs={'class':'form-control', 'placeholder':'البنك'}),
            'branchBankID': forms.Select(attrs={'class':'form-control', 'placeholder':'الفرع'}),
            'typeAccBankID': forms.Select(attrs={'class':'form-control', 'placeholder':'نوع الحساب'}),
            'accountNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الحساب'}),
            'IBANNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الآيبان'}),
            'ownerAccount': forms.TextInput(attrs={'class':'form-control', 'placeholder':'صاحب الحساب'}),
            'attachments': forms.ClearableFileInput(attrs={'class':'form-control', 'placeholder':'مرفقات'}),
            'photo': forms.ClearableFileInput(attrs={'class':'form-control', 'placeholder':'صورة / لوقو'}),
            'notes': forms.TextInput(attrs={'class':'form-control', 'placeholder':'ملاحظات'}),
            'documentLink': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رابط المستندات'}),
            'active': forms.TextInput(attrs={'class':'form-control', 'placeholder':'ملاحظات'}),
        }

class PersonForm(forms.ModelForm):
    class Meta:
        model = Persons
        fields = '__all__'
        widgets = {
            'f_Name_ar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الأول'}),
            's_Name_ar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الثاني'}),
            't_Name_ar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الثالث'}),
            'fo_Name_ar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الرابع'}),
            'f_Name_en': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الأول'}),
            's_Name_en': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الثاني'}),
            't_Name_en': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الثالث'}),
            'fo_Name_en': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الرابع'}),
            'dateOfBirth': forms.TextInput(attrs={'class':'form-control', 'type':'date', 'placeholder':'تاريخ الميلاد'}),
            'genderID': forms.Select(attrs={'class':'form-control', 'placeholder':'الجنس', 'value':'الجنس'}),
            'socialStatusID': forms.Select(attrs={'class':'form-control', 'placeholder':'الحالة الإجتماعية'}),
            'typeID': forms.Select(attrs={'class':'form-control', 'placeholder':'نوع الهوية'}),
            'id_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الهوية'}),
            'id_ExpiredDate': forms.TextInput(attrs={'class':'form-control','type':'date', 'placeholder':'تاريخ إنتهاء الهوية'}),
            'workTradeID': forms.Select(attrs={'class':'form-control', 'placeholder':'المهنة'}),
            'workSpecialtyID': forms.Select(attrs={'class':'form-control', 'placeholder':'التخصص'}),
            'skillsID': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'المهارات'}),
            'languagesID': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'اللغات'}),
            'jobTitleID': forms.Select(attrs={'class':'form-control', 'placeholder':'المسمى الوظيفي'}),
        }

class LegalPersonsForm (forms.ModelForm):
  class Meta:
      model = LegalPersons
      fields = '__all__'
      widgets = {
        'name_ar': forms.TextInput(attrs={'class':'form-control','placeholder':'إسم الشركة عربي'}),
        'acronym_ar': forms.TextInput(attrs={'class':'form-control','placeholder':'الإسم المختصر عربي'}),
        'name_en': forms.TextInput(attrs={'class':'form-control','placeholder':'إسم الشركة إنجليزي'}),
        'acronym_en': forms.TextInput(attrs={'class':'form-control','placeholder':'الإسم المختصر إنجليزي'}),
        'who_are_we': forms.TextInput(attrs={'class':'form-control', 'placeholder':'من نحن'}),
        'businessTypeID': forms.Select(attrs={'class':'form-control', 'placeholder':'نوع الشركة'}),
        'administrator': forms.TextInput(attrs={'class':'form-control','placeholder':'الموظف المسؤول'}),
        'phoneAdmin': forms.TextInput(attrs={'class':'form-control','placeholder':'هاتف الموظف المسؤول'}),
        'taxNumber': forms.TextInput(attrs={'class':'form-control','placeholder':'الرقم الضريبي'}),
    }
    

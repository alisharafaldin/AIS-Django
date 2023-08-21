from django import forms
from .models import Person, Cities


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        # def __init__(self, *args, **kwargs):
        #   super().__init__(*args, **kwargs)
        #   self.fields['cityID'].queryset = Cities.objects.none()
        # لعمل إستثناء حقل
        # exclude = ('f_Name_ar')
        widgets = {
            'f_Name_ar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الأول'}),
            's_Name_ar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الثاني'}),
            't_Name_ar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الثالث'}),
            'fo_Name_ar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الرابع'}),
            'f_Name_en': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الأول'}),
            's_Name_en': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الثاني'}),
            't_Name_en': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الثالث'}),
            'fo_Name_en': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الرابع'}),
            'dateOfBirth': forms.TextInput(attrs={'class':'form-control','type':'date', 'placeholder':'تاريخ الميلاد'}),
            'genderID': forms.Select(attrs={'class':'form-control', 'placeholder':'الجنس', 'value':'الجنس'}),
            'nationalityID': forms.Select(attrs={'class':'form-control', 'placeholder':'الجنسية'}),
            'socialStatusID': forms.Select(attrs={'class':'form-control', 'placeholder':'الحالة الإجتماعية'}),
            'typeID': forms.Select(attrs={'class':'form-control', 'placeholder':'نوع الهوية'}),
            'id_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الهوية'}),
            'id_ExpiredDate': forms.TextInput(attrs={'class':'form-control','type':'date', 'placeholder':'تاريخ إنتهاء الهوية'}),
            'countryID': forms.Select(attrs={'class':'form-control', 'placeholder':'الدولة'}),
            'regionID': forms.Select(attrs={'class':'form-control', 'placeholder':'المنطقة'}),
            'stateID': forms.Select(attrs={'class':'form-control', 'placeholder':'الولاية'}),
            'cityID': forms.Select(attrs={'class':'form-control', 'placeholder':'المدينة'}),
            'desAddress': forms.TextInput(attrs={'class':'form-control', 'placeholder':'وصف مكان السكن'}),
            'workTradeID': forms.Select(attrs={'class':'form-control', 'placeholder':'المهنة'}),
            'workSpecialtyID': forms.Select(attrs={'class':'form-control', 'placeholder':'التخصص'}),
            'mobileNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الجوال'}),
            'mobileNumberAnother': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم جوال آخر'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'إيميل'}),
            'bankID': forms.Select(attrs={'class':'form-control', 'placeholder':'البنك'}),
            'branchBankID': forms.Select(attrs={'class':'form-control', 'placeholder':'الفرع'}),
            'typeAccBankID': forms.Select(attrs={'class':'form-control', 'placeholder':'نوع الحساب'}),
            'accountNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الحساب'}),
            'IBANNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الآيبان'}),
            'ownerAccount': forms.TextInput(attrs={'class':'form-control', 'placeholder':'صاحب الحساب'}),
            'attachments': forms.FileInput(attrs={'class':'form-control', 'placeholder':'مرفقات'}),
            'emp_Photo': forms.FileInput(attrs={'class':'form-control', 'placeholder':'صورة شخصية'}),
            'notes': forms.TextInput(attrs={'class':'form-control', 'placeholder':'ملاحظات'}),
        }
      
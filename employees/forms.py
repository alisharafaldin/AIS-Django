from django import forms
from .models import EmpInfo

class EmpForm(forms.ModelForm):
    class Meta:
        model = EmpInfo
        fields = '__all__'
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
            'genderID': forms.Select(attrs={'class':'form-control', 'placeholder':'الجنس'}),
            'nationalityID': forms.Select(attrs={'class':'form-control', 'placeholder':'الجنسية'}),
            'socialStatusID': forms.Select(attrs={'class':'form-control', 'placeholder':'الحالة الإجتماعية'}),
            'typeID': forms.Select(attrs={'class':'form-control', 'placeholder':'نوع الهوية'}),
            'id_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الرابع'}),
            'visaNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم التأشيرة'}),
            'companyID': forms.Select(attrs={'class':'form-control', 'placeholder':'الشركة'}),
            'sponserID': forms.Select(attrs={'class':'form-control', 'placeholder':'الكفيل'}),
            'workTradeID': forms.Select(attrs={'class':'form-control', 'placeholder':'المهنة'}),
            'workSpecialtyID': forms.Select(attrs={'class':'form-control', 'placeholder':'التخصص'}),
            'workingStatusID': forms.Select(attrs={'class':'form-control', 'placeholder':'حالة العمل'}),
            'passportNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الجواز'}),
            'passportExpiryDate': forms.TextInput(attrs={'class':'form-control','type':'date', 'placeholder':'تاريخ إنتهاء الجواز'}),
            'medicalInsuranceExpirDate': forms.TextInput(attrs={'class':'form-control', 'placeholder':'تاريخ إنتهاء التأمين الطبي'}),
            'borderNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الحدود'}),
            'enteryDate': forms.TextInput(attrs={'class':'form-control','type':'date', 'placeholder':'تايخ الدخول'}),
            'businessOfficeNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم مكتب العمل'}),
            'mobileNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الجوال'}),
            'bankID': forms.Select(attrs={'class':'form-control', 'placeholder':'البنك'}),
            'accountNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الحساب'}),
            'iqamaNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الإقامة'}),
            'iqamaReleaseDate': forms.TextInput(attrs={'class':'form-control','type':'date', 'placeholder':'تاريخ الإصدار'}),
            'iqamaExpiredDate': forms.TextInput(attrs={'class':'form-control','type':'date', 'placeholder':'تاريخ الإنتهاء'}),
            'salaryInsurance': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'راتب التأمينات'}),
            'contractSalary': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'إجمالي الراتب'}),
            'fixedExtra': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'إضافي ثابت'}),
            'workStartingDate': forms.TextInput(attrs={'class':'form-control','type':'date', 'placeholder':'تاريخ بداية العمل'}),
            'endDateOfService': forms.TextInput(attrs={'class':'form-control', 'placeholder':'تاريخ إنتهاء العمل'}),
            'emp_Photo': forms.FileInput(attrs={'class':'form-control', 'placeholder':'صور شخصية'}),
            'coronaCheck': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'كرونا'}),
            'tawaklna': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'توكلنا'}),
            'sahaty': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'صحتي'}),
            'medicalInsurance': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'تأمين طبي'}),
            'muqeemCopy': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'نسخة مقيم'}),
            'notes': forms.TextInput(attrs={'class':'form-control', 'placeholder':'ملاحظات'}),
            'documentLink': forms.URLInput(attrs={'class':'form-control', 'placeholder':'رابط الوثائق'}),
        }
from django import forms
from .models import ShareholdersInfo , Contracts

class ShareholderForm(forms.ModelForm):
    class Meta:
        model = ShareholdersInfo
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
            'dateOfBirth': forms.TextInput(attrs={'class':'form-control', 'placeholder':'تاريخ الميلاد'}),
            'genderID': forms.Select(attrs={'class':'form-control', 'placeholder':'الجنس'}),
            'nationalityID': forms.Select(attrs={'class':'form-control', 'placeholder':'الجنسية'}),
            'socialStatusID': forms.Select(attrs={'class':'form-control', 'placeholder':'الحالة الإجتماعية'}),
            'typeID': forms.Select(attrs={'class':'form-control', 'placeholder':'نوع الهوية'}),
            'id_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الهوية'}),
            'id_ExpiredDate': forms.TextInput(attrs={'class':'form-control', 'placeholder':'تاريخ إنتهاء الهوية'}),
            'workTradeID': forms.Select(attrs={'class':'form-control', 'placeholder':'المهنة'}),
            'workSpecialtyID': forms.Select(attrs={'class':'form-control', 'placeholder':'التخصص'}),
            'mobileNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الجوال'}),
            'mobileNumberAnother': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم جوال آخر'}),
            # 'countreyID': forms.Select(attrs={'class':'form-control', 'placeholder':'الدولة'}),
            'stateID': forms.Select(attrs={'class':'form-control', 'placeholder':'الولاية'}),
            'cityID': forms.Select(attrs={'class':'form-control', 'placeholder':'المدينة'}),
            'detailsAddress': forms.TextInput(attrs={'class':'form-control', 'placeholder':'وصف عنوان السكن'}),
            'bankID': forms.Select(attrs={'class':'form-control', 'placeholder':'البنك'}),
            'branchBankID': forms.Select(attrs={'class':'form-control', 'placeholder':'فرع البنك'}),
            'typeAccBankID': forms.Select(attrs={'class':'form-control', 'placeholder':'نوع الحساب'}),
            'accountNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الحساب'}),
            'IBANNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الآيبان'}),
            'ownerAccount': forms.TextInput(attrs={'class':'form-control', 'placeholder':'إسم صاحب الحساب'}),
            'Photo': forms.FileInput(attrs={'class':'form-control', 'placeholder':'صور شخصية'}),
            'notes': forms.TextInput(attrs={'class':'form-control', 'placeholder':'ملاحظات'}),
            'documentLink': forms.URLInput(attrs={'class':'form-control', 'placeholder':'رابط الوثائق'}),
            'marketerID': forms.Select(attrs={'class':'form-control', 'placeholder':'المسوق'}),
        }

class ContractsForm(forms.ModelForm):
    class Meta:
        model = Contracts
        fields = '__all__'
        widgets = {
            'shareholdersID': forms.Select(attrs={'placeholder':'المساهم','class':'form-control'}),
            'dateOfContract': forms.TextInput(attrs={'placeholder':'تاريخ العقد','class':'form-control'}),
            'contractNumber': forms.TextInput(attrs={'placeholder':'رقم العقد','class':'form-control'}),
            'axisID': forms.Select(attrs={'placeholder':'المحور','class':'form-control'}),
            'numberReceipt': forms.TextInput(attrs={'placeholder':'رقم الإيصال','class':'form-control'}),
            'numberOfShares': forms.TextInput(attrs={'placeholder':'عدد الأسهم','class':'form-control'}),
            'amountOfShare': forms.TextInput(attrs={'placeholder':'سعر السهم','class':'form-control'}),
            'profitOfShare': forms.TextInput(attrs={'placeholder':'ربح السهم','class':'form-control'}),
            'dateOfDividend': forms.TextInput(attrs={'placeholder':'تاريخ توزيع الأرباح ','class':'form-control'}),
            'witnes1ID': forms.Select(attrs={'placeholder':'الشاهد الأول','class':'form-control'}),
        }
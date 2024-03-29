from django import forms
from .models import Qayd, QaydDetails , AccountsTree

class AccountsTreeForm(forms.ModelForm):
    class Meta:
        model = AccountsTree
        fields = '__all__'
        widgets = {
            'code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رمز الحساب'}),
            'name_ar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'إسم الحساب عربي'}),
            'name_en': forms.TextInput(attrs={'class':'form-control', 'placeholder':'إسم الحساب إنجليزي'}),
            'typeID': forms.Select(attrs={'class':'form-control', 'placeholder':'نوع الحساب'}),
            'natureID': forms.Select(attrs={'class':'form-control', 'placeholder':'طبيعة الميزانية'}),
            'categoryID': forms.Select(attrs={'class':'form-control', 'placeholder':'تصنيف الحساب'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'وصف الحساب'}),
            'is_can_pay': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'إمكانية الدفع و السداد من الحساب'}),     
        }

class QaydForm(forms.ModelForm):
    class Meta:
        model = Qayd
        fields = '__all__'
        widgets = {
            # 'created_py': forms.Select(attrs={'class':'form-control', 'placeholder':'المستخدم'}),
            'date': forms.TextInput(attrs={'class':'form-control',  'type':'date' , 'placeholder':'تاريخ القيد'}),
            'typeTransactionID': forms.Select(attrs={'class':'form-control', 'placeholder':'العملية'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'وصف القيد', 'style':'height: 50px;'}),
            'attachments': forms.FileInput(attrs={'class':'form-control', 'placeholder':'مرفقات القيد', 'value':"{{qayd_form.attachments}}"}),
        }

class QaydDetailsForm(forms.ModelForm):
    class Meta:
        model = QaydDetails
        fields = '__all__'
        widgets = {
            'qaydID': forms.Select(attrs={'class':'form-control', 'placeholder':'رأس القيد'}),
            'date': forms.TextInput(attrs={'class':'form-control',  'type':'date' , 'placeholder':'تاريخ القيد'}),
            'accountID': forms.Select(attrs={'class':'form-control', 'placeholder':'الحساب'}),
            'rate': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'سعر الصرف'}),
            'debit': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'مدين'}),
            'credit': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'دائن'}),
            'currencyID': forms.Select(attrs={'class':'form-control', 'placeholder':'العملة'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'وصف القيد'}),
            'projectID': forms.Select(attrs={'class':'form-control', 'placeholder':'المشروع'}),
            'empID': forms.Select(attrs={'class':'form-control', 'placeholder':'الموظف'}),       
        }



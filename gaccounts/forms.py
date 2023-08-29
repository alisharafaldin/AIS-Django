from django import forms
from .models import Qayd, QaydDetails , AccountsTree, BondsCatchPay

class AccountsTreeForm(forms.ModelForm):
    class Meta:
        model = AccountsTree
        fields = '__all__'
        widgets = {
            'accCode': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رمز الحساب'}),
            'accName_ar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'إسم الحساب عربي'}),
            'accName_en': forms.TextInput(attrs={'class':'form-control', 'placeholder':'إسم الحساب إنجليزي'}),
            'accTypeID': forms.Select(attrs={'class':'form-control', 'placeholder':'نوع الحساب'}),
            'accBudgetID': forms.Select(attrs={'class':'form-control', 'placeholder':'توجيه الميزانية'}),
            'accDorCID': forms.Select(attrs={'class':'form-control', 'placeholder':'طبيعة الحساب'}),
            'accParentID': forms.Select(attrs={'class':'form-control', 'placeholder':'الحساب الأب'}),
            'accDes': forms.TextInput(attrs={'class':'form-control', 'placeholder':'وصف الحساب'}),
            'is_can_pay': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'إمكانية الدفع و السداد من الحساب'}),     
        }

class QaydForm(forms.ModelForm):
    class Meta:
        model = Qayd
        fields = '__all__'
        widgets = {
            'id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'معرف القيد'}),
            'userID': forms.Select(attrs={'class':'form-control', 'placeholder':'المستخدم'}),
            'dateQayd': forms.TextInput(attrs={'class':'form-control',  'type':'date' , 'placeholder':'تاريخ القيد'}),
            'currencyID': forms.Select(attrs={'class':'form-control', 'placeholder':'العملة'}),
            'desQayd': forms.Textarea(attrs={'class':'form-control', 'placeholder':'وصف القيد', 'style':'height: 50px;'}),
            'attachments': forms.FileInput(attrs={'class':'form-control', 'placeholder':'مرفقات القيد', 'value':"{{qayd_form.attachments}}"}),
            'details': forms.TextInput(attrs={'class':'form-control', 'placeholder':'تفاصيل القيد'}),     
        }

class QaydDetailsForm(forms.ModelForm):
    class Meta:
        model = QaydDetails
        fields = '__all__'
        widgets = {
            'qaydID': forms.Select(attrs={'class':'form-control', 'placeholder':'رأس القيد'}),
            'debit': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'مدين'}),
            'credit': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'دائن'}),
            'desQaydDetails': forms.TextInput(attrs={'class':'form-control', 'placeholder':'وصف القيد'}),
            'qaydID': forms.Select(attrs={'class':'form-control', 'placeholder':'راس القيد'}),
            'accID': forms.Select(attrs={'class':'form-control', 'placeholder':'الحساب'}),
            'projectID': forms.Select(attrs={'class':'form-control', 'placeholder':'المشروع'}),
            'empID': forms.Select(attrs={'class':'form-control', 'placeholder':'الموظف'}),       
        }

class BondsCatchPayForm(forms.ModelForm):
    class Meta:
        model = BondsCatchPay
        fields = '__all__'
        widgets = {
            'userID': forms.Select(attrs={'class':'form-control', 'placeholder':'أمين الصندوق'}),
            'dateBond': forms.TextInput(attrs={'class':'form-control',  'type':'date' , 'placeholder':'تاريخ السند'}),
            'typeBondID': forms.Select(attrs={'class':'form-control', 'placeholder':'نوع السند'}),
            'currencyID': forms.Select(attrs={'class':'form-control', 'placeholder':'العملة'}),
            'exchangeRate': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'سعر الصرف'}),
            'amount': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'المبلغ'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'وصف السند', 'style':'height: 50px;'}),
            'recipient': forms.TextInput(attrs={'class':'form-control', 'placeholder':'المستلم'}),
            'empID': forms.Select(attrs={'class':'form-control', 'placeholder':'الموظف'}), 
            'projectID': forms.Select(attrs={'class':'form-control', 'placeholder':'المشروع'}),        
            'shareholderID': forms.Select(attrs={'class':'form-control', 'placeholder':'المشروع'}),   
        }
from django import forms
from .models import Qayd, QaydDetails , AccountsTree

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
            # 'id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'معرف القيد'}),
            'userID': forms.Select(attrs={'name':'userID', 'class':'form-control', 'placeholder':'المستخدم'}),
            'dateQayd': forms.TextInput(attrs={'name':'dateQayd', 'class':'form-control',  'type':'date' , 'placeholder':'تاريخ القيد'}),
            'currencyID': forms.Select(attrs={'name':'currencyID', 'class':'form-control', 'placeholder':'العملة'}),
            'desQayd': forms.Textarea(attrs={'name':'desQayd', 'class':'form-control', 'placeholder':'وصف القيد', 'style':'height: 50px;'}),
            'attachments': forms.FileInput(attrs={'name':'attachments', 'class':'form-control', 'placeholder':'مرفقات القي'}),
            'details': forms.TextInput(attrs={'name':'details','class':'form-control', 'placeholder':'تفاصيل القيد'}),     
        }

class QaydDetailsForm(forms.ModelForm):
    class Meta:
        model = QaydDetails
        fields = '__all__'
        widgets = {
            'debit': forms.NumberInput(attrs={'name':'debit','class':'form-control', 'placeholder':'مدين'}),
            'credit': forms.NumberInput(attrs={'name':'credit','class':'form-control', 'placeholder':'دائن'}),
            'desQaydDetails': forms.TextInput(attrs={'name':'desQaydDetails','class':'form-control', 'placeholder':'وصف القيد'}),
            'qaydID': forms.Select(attrs={'name':'qaydID','class':'form-control', 'placeholder':'راس القيد'}),
            'accID': forms.Select(attrs={'name':'accID','class':'form-control', 'placeholder':'الحساب'}),
            'projectID': forms.Select(attrs={'name':'projectID','class':'form-control', 'placeholder':'المشروع'}),
            'empID': forms.Select(attrs={'name':'empID','class':'form-control', 'placeholder':'الموظف'}),       
        }


#  new_qayd = Qayd()
#     new_qayd.userID = request.user
#     new_qayd.dateQayd = timezone.now()
#     new_qayd.attachments = request.attachment
#     new_qayd.accCurrencyID = request.currency
#     new_qayd.desQayd = request.desqayd
#     new_qayd.save()
#     qayddetails = QaydDetails.objects.create(qaydID=new_qayd)
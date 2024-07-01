from django import forms
from .models import Qayd, QaydDetails , AccountsTree
from django.forms import modelformset_factory, formset_factory
from django.forms import BaseModelFormSet


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
            'created_py': forms.Select(attrs={'class':'form-control', 'placeholder':'المستخدم', 'value':"{{qayd_form.attachments}}"}),
        }

class QaydDetailsForm(forms.ModelForm):
    class Meta:
        model = QaydDetails
        fields = '__all__'
        widgets = {
            'id': forms.Select(attrs={'class':'form-control', 'placeholder':' id'}),
            'qaydID': forms.Select(attrs={'class':'form-control', 'placeholder':'رأس القيد'}),
            'date_details': forms.TextInput(attrs={'class':'form-control',  'type':'date' , 'placeholder':'تاريخ القيد'}),
            'accountID': forms.Select(attrs={'class':'form-control', 'placeholder':'الحساب'}),
            'rate': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'سعر الصرف'}),
            'debit': forms.NumberInput(attrs={'class':'form-control debit-input', 'placeholder':'مدين', 'onchange':'calculateTotals()'}),
            'credit': forms.NumberInput(attrs={'class':'form-control credit-input', 'placeholder':'دائن', 'onchange':'calculateTotals()'}),
            'currencyID': forms.Select(attrs={'class':'form-control', 'placeholder':'العملة'}),
            'description_details': forms.TextInput(attrs={'class':'form-control', 'placeholder':'وصف القيد'}),
            'projectID': forms.Select(attrs={'class':'form-control', 'placeholder':'المشروع'}),
            'empID': forms.Select(attrs={'class':'form-control', 'placeholder':'الموظف'}),       
        }
    

class BaseQaydDetailsFormSet(BaseModelFormSet):
    def clean(self):
        super().clean()
        # لا تقم بالتحقق من التكرار في هذا الـ FormSet
        # إذا كان لديك قواعد معينة لتجنب التكرار، قم بإضافتها هنا
        # على سبيل المثال:
        seen = set()
        for form in self.forms:
            if form.cleaned_data:
                qaydID = form.cleaned_data.get('qaydID')
                accountID = form.cleaned_data.get('accountID')
                currencyID = form.cleaned_data.get('currencyID')
                key = (qaydID, accountID, currencyID)
                if key in seen:
                    raise forms.ValidationError("Please correct the duplicate values below.")
                seen.add(key)



QaydDetailsFormSet = modelformset_factory(QaydDetails, form=QaydDetailsForm, extra=2)  # extra=3 يعني أننا نريد إضافة 3 نماذج إضافية
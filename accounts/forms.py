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
            'date': forms.DateTimeInput(attrs={'class':'form-control',  'type':'datetime-local' , 'placeholder':'تاريخ القيد'}),
            'typeTransactionID': forms.Select(attrs={'class':'form-control', 'placeholder':'العملية'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'وصف القيد', 'style':'height: 50px;'}),
            'attachments': forms.FileInput(attrs={'class':'form-control', 'placeholder':'مرفقات القيد', 'value':"{{qayd_form.attachments}}"}),
            'updated_at': forms.DateTimeInput(attrs={'class':'form-control',  'type':'datetime-local' , 'placeholder':'تاريخ التعديل'}),
            'details': forms.CheckboxSelectMultiple,
            'created_by': forms.Select(attrs={'class':'form-control', 'placeholder':'المنشئ'}),

        }
    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     if self.instance.pk:  # إذا كان الكائن موجودًا بالفعل (تعديل)
    #         instance.created_by = self.instance.created_by  # حافظ على القيمة الأصلية لـ 'created_by'
    #     if commit:
    #         instance.save()
    #     return instance
    
    # ضبط حقل created_byكنموذج للقراءة فقط في حال اتعديل  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['created_by'].widget = forms.HiddenInput()  # إخفاء الحقل في نموذج التعديل
        else:
            self.fields['created_by'].required = True  # تأكيد أن الحقل مطلوب عند الإنشاء
 
class QaydDetailsForm(forms.ModelForm):
    DELETE = forms.BooleanField(required=False, initial=False)
    class Meta:
        model = QaydDetails
        fields = '__all__'
        widgets = {
            'DELETE': forms.CheckboxInput(),
            'accountID': forms.Select(attrs={'class':'form-control', 'placeholder':'الحساب'}),
            'rate': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'سعر الصرف'}),
            'debit': forms.NumberInput(attrs={'class':'form-control debit-input', 'placeholder':'مدين', 'onchange':'calculateTotals()'}),
            'credit': forms.NumberInput(attrs={'class':'form-control credit-input', 'placeholder':'دائن', 'onchange':'calculateTotals()'}),
            'currencyID': forms.Select(attrs={'class':'form-control', 'placeholder':'العملة'}),
            'description_details': forms.TextInput(attrs={'class':'form-control', 'placeholder':'وصف القيد'}),
            'projectID': forms.Select(attrs={'class':'form-control', 'placeholder':'المشروع'}),
            'empID': forms.Select(attrs={'class':'form-control', 'placeholder':'الموظف'}), 
        }

QaydDetailsFormSet = modelformset_factory(QaydDetails, form=QaydDetailsForm, extra=2, can_delete=True)  # extra=3 يعني أننا نريد إضافة 3 نماذج إضافية
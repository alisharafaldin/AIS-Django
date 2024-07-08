from django import forms
from .models import Qayd, QaydDetails , AccountsTree, Countries
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
            'date': forms.DateTimeInput(attrs={'class':'form-control',  'type':'datetime-local' , 'placeholder':'التاريخ '}),
            'typeTransactionID': forms.Select(attrs={'class':'form-control', 'placeholder':'العملية'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'وصف القيد', 'style':'height: 50px;'}),
            'attachments': forms.FileInput(attrs={'class':'form-control', 'placeholder':'مرفقات القيد', 'value':"{{qayd_form.attachments}}"}),
            'updated_at': forms.DateTimeInput(attrs={'class':'form-control',  'type':'datetime-local' , 'placeholder':'تاريخ التعديل'}),
            'details': forms.CheckboxSelectMultiple,
            # 'created_by': forms.Select(attrs={'class':'form-control', 'placeholder':'المنشئ'}),

        }
    # ضبط حقل created_byكنموذج للقراءة فقط في حال اتعديل  
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.instance.pk:
    #         self.fields['created_by'].widget = forms.HiddenInput()  # إخفاء الحقل في نموذج التعديل
    #     else:
    #         self.fields['created_by'].required = True  # تأكيد أن الحقل مطلوب عند الإنشاء
 
class QaydDetailsForm(forms.ModelForm):
    DELETE = forms.BooleanField(required=False, initial=False)
    # currency_ar = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
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
    #التأكد من أن على الأقل إحدى القيمتين ليست صفراً
    def clean(self):
        cleaned_data = super().clean()
        credit = cleaned_data.get('credit')
        debit = cleaned_data.get('debit')
        if credit == 0 and debit == 0:
            raise forms.ValidationError('يجب أن تكون إحدى القيمتين على الأقل غير صفرية أو حذف السطر.')
        return cleaned_data

# نموذج المجموعة مع دالة التحقق
QaydDetailsFormSet = modelformset_factory(
    QaydDetails,
    form=QaydDetailsForm,
    extra=2, # عدد النماذج الإفتراضية
    can_delete=True, # إمكانية الحذف
    min_num=2, # الحد الأدنى لعدد النماذج
    validate_min=True, # التحقق من عدد النماذج
    ) 

# للتحقق من توازن القيد
class BaseQaydDetailsFormSet(forms.BaseModelFormSet):
    def clean(self):
        super().clean()
        total_credit = 0
        total_debit = 0

        for form in self.forms:
            if form.cleaned_data:
                total_credit += form.cleaned_data.get('credit', 0)
                total_debit += form.cleaned_data.get('debit', 0)

        if total_credit != total_debit:
            raise forms.ValidationError('قيمة المدين يجب أن تكون مساوية لقيمة الدائن.')

# إنشاء نموذج المجموعة باستخدام الفئة الأساسية المخصصة
QaydDetailsFormSet = modelformset_factory(QaydDetails, form=QaydDetailsForm, formset=BaseQaydDetailsFormSet, extra=2)
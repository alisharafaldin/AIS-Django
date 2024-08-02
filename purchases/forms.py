from django import forms
from .models import Suppliers, InvoiceHead, InvoiceBody
from django.forms import modelformset_factory

class SuppliersForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = '__all__'
        widgets = {
           'legalPersonsID': forms.Select(attrs={'class':'form-control', 'placeholder':'معرف المورد'}),
   }

class InvoiceHeadForm(forms.ModelForm):
    class Meta:
        model = InvoiceHead
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'class':'form-control',  'type':'datetime-local' , 'placeholder':'التاريخ '}),
            'supplierID': forms.Select(attrs={'class':'form-control', 'placeholder':'العملية'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'وصف القيد', 'style':'height: 50px;'}),
            'attachments': forms.ClearableFileInput(attrs={'class':'form-control', 'placeholder':'مرفقات القيد', 'value':"{{qayd_form.attachments}}"}),
            'updated_at': forms.DateTimeInput(attrs={'class':'form-control',  'type':'datetime-local' , 'placeholder':'تاريخ التعديل'}),
            'details': forms.CheckboxSelectMultiple,
        }

class InvoiceBodyForm(forms.ModelForm):
    DELETE = forms.BooleanField(required=False, initial=False)
    class Meta:
        model = InvoiceBody
        fields = '__all__'
        widgets = {
            'DELETE': forms.CheckboxInput(),
            'invoiceHeadID': forms.Select(attrs={'class':'form-control', 'placeholder':'رأس الفاتورة'}),
            'itemsDetailstID': forms.Select(attrs={'class':'form-control itemsDetailstID', 'placeholder':'المنتج'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control debit-input quantity', 'placeholder':'الكمية'}),
            'unit_price': forms.NumberInput(attrs={'class':'form-control unit_price', 'placeholder':'سعر الوحدة'}),
            'discount': forms.NumberInput(attrs={'class':'form-control discount' , 'placeholder':'الخصم'}),
            'total_price_before_tax': forms.NumberInput(attrs={'class':'form-control total_price_before_tax', 'placeholder':'إجمالي السعر'}),
            'tax_rate': forms.NumberInput(attrs={'class':'form-control tax_rate', 'placeholder':'نسبة الضريبة'}),
            'tax_value': forms.NumberInput(attrs={'class':'form-control tax_value', 'placeholder':'قيمة الضريبة'}),
            'total_price_after_tax': forms.NumberInput(attrs={'class':'form-control total_price_after_tax', 'placeholder':'إجمالي السعر بعد الخصم'}),
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
InvoiceBodyFormSet = modelformset_factory(
    InvoiceBody,
    form=InvoiceBodyForm,
    extra=2, # عدد النماذج الإفتراضية
    can_delete=True, # إمكانية الحذف
    min_num=2, # الحد الأدنى لعدد النماذج
    validate_min=True, # التحقق من عدد النماذج
    ) 

# إنشاء نموذج المجموعة باستخدام الفئة الأساسية المخصصة
InvoiceBodyFormSet = modelformset_factory(InvoiceBody, form=InvoiceBodyForm, extra=2)
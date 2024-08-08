from django import forms
from .models import Customers, InvoicesSalesHead, InvoicesSalesBody
from django.forms import modelformset_factory

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'
        widgets = {
           'legalPersonsID': forms.Select(attrs={'class':'form-control', 'placeholder':'معرف المورد'}),
   }

class InvoiceHeadForm(forms.ModelForm):
    class Meta:
        model = InvoicesSalesHead
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'class':'form-control',  'type':'datetime-local' , 'placeholder':'التاريخ '}),
            'customerID': forms.Select(attrs={'class':'form-control', 'placeholder':'العميل'}),
            'typeTransactionID': forms.Select(attrs={'disabled': 'disabled','class':'form-control', 'placeholder':'نوع المعاملة'}),
            'inventoryID': forms.Select(attrs={'class':'form-control', 'placeholder':'المخزن'}),
            'typePaymentID': forms.Select(attrs={'class':'form-control', 'placeholder':'طريقة الدفع'}),
            'typeDeliveryID': forms.Select(attrs={'class':'form-control', 'placeholder':'طريقة التسليم'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'وصف الفاتورة', 'style':'height: 50px;'}),
            'attachments': forms.ClearableFileInput(attrs={'class':'form-control', 'placeholder':'مرفقات الفاتورة', 'value':"{{qayd_form.attachments}}"}),
            'updated_at': forms.DateTimeInput(attrs={'class':'form-control', 'type':'datetime-local', 'placeholder':'تاريخ التعديل'}),
            'details': forms.CheckboxSelectMultiple,
        }

class InvoiceBodyForm(forms.ModelForm):
    DELETE = forms.BooleanField(required=False, initial=False)
    class Meta:
        model = InvoicesSalesBody
        fields = '__all__'
        widgets = {
            'DELETE': forms.CheckboxInput(),
            'invoiceHeadID': forms.Select(attrs={'class':'form-control', 'placeholder':'رأس الفاتورة'}),
            'itemID': forms.Select(attrs={'class':'form-control itemID', 'placeholder':'المنتج'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control debit-input quantity', 'placeholder':'الكمية'}),
            'unit_price': forms.NumberInput(attrs={'class':'form-control unit_price', 'placeholder':'سعر الوحدة'}),
            'discount': forms.NumberInput(attrs={'class':'form-control discount' , 'placeholder':'الخصم'}),
            'total_price_before_tax': forms.NumberInput(attrs={'readonly':'readonly','class':'form-control total_price_before_tax', 'placeholder':'إجمالي السعر'}),
            'tax_rate': forms.NumberInput(attrs={'class':'form-control tax_rate', 'placeholder':'نسبة الضريبة'}),
            'tax_value': forms.NumberInput(attrs={'readonly':'readonly','class':'form-control tax_value', 'placeholder':'قيمة الضريبة'}),
            'total_price_after_tax': forms.NumberInput(attrs={'readonly':'readonly','class':'form-control total_price_after_tax', 'placeholder':'إجمالي السعر بعد الخصم'}),
    }
    #التأكد من أن على الأقل إحدى القيمتين ليست صفراً
    # def clean(self):
    #     cleaned_data = super().clean()
    #     credit = cleaned_data.get('credit')
    #     debit = cleaned_data.get('debit')
    #     if credit == 0 and debit == 0:
    #         raise forms.ValidationError('يجب أن تكون إحدى القيمتين على الأقل غير صفرية أو حذف السطر.')
    #     return cleaned_data

# نموذج المجموعة مع دالة التحقق
InvoiceBodyFormSet = modelformset_factory(
    InvoicesSalesBody,
    form=InvoiceBodyForm,
    extra=2, # عدد النماذج الإفتراضية
    can_delete=True, # إمكانية الحذف
    min_num=2, # الحد الأدنى لعدد النماذج
    validate_min=True, # التحقق من عدد النماذج
    ) 

# إنشاء نموذج المجموعة باستخدام الفئة الأساسية المخصصة
InvoiceBodyFormSet = modelformset_factory(InvoicesSalesBody, form=InvoiceBodyForm, extra=2)
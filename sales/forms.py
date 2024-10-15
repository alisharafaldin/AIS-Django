from django import forms
from .models import Customers, InvoicesSalesHead, InvoicesSalesBody
from basicinfo.models import Countries
from products.models import Items
from django.forms import modelformset_factory
from django_select2.forms import Select2Widget


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'
        widgets = {
           'legalPersonsID': forms.Select(attrs={'class':'form-control', 'placeholder':'معرف المورد'}),
   }

class InvoiceHeadForm(forms.ModelForm):
    currencyID = forms.ModelChoiceField(
        queryset=Countries.objects.all(),
        empty_label="اختر العملة",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    customerID = forms.ModelChoiceField(
        queryset=Customers.objects.all(),
        label='العميل',
        empty_label="اختر العميل",
        required=False,
        widget=Select2Widget(attrs={'class':'form-control',
                                     'placeholder':'العميل',
                                       'style': 'data-width:100%', 'height': '100px'}),)

    class Meta:
        model = InvoicesSalesHead
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'placeholder':'التاريخ'}),
            'rate': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'سعر الصرف'}),
            'typeTransactionID': forms.Select(attrs={'disabled':'disabled','class':'form-control', 'placeholder':'نوع المعاملة'}),
            'inventoryID': forms.Select(attrs={'class':'form-control', 'placeholder':'المخزن'}),
            'typePaymentID': forms.Select(attrs={'class':'form-control', 'placeholder':'طريقة الدفع'}),
            'typeDeliveryID': forms.Select(attrs={'class':'form-control', 'placeholder':'طريقة التسليم'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'وصف الفاتورة', 'style':'height: 50px;'}),
            'attachments': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'updated_at': forms.DateTimeInput(attrs={'class':'form-control', 'type':'datetime-local', 'placeholder':'تاريخ التعديل'}),
            'details': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        company_id = kwargs.pop('companyID', None)  # استلام الشركة الحالية من العرض
        super(InvoiceHeadForm, self).__init__(*args, **kwargs)
        # تخصيص تسمية حقل currencyID
        self.fields['currencyID'].label_from_instance = lambda obj: obj.currency_ar

        # تصفية العملاء بناءً على الشركة
        if company_id: 
            self.fields['customerID'].queryset = Customers.objects.filter(companyID_id=company_id)
   
class InvoiceBodyForm(forms.ModelForm):
    DELETE = forms.BooleanField(required=False, initial=False)
    itemID = forms.ModelChoiceField(
        queryset=Items.objects.all(),
        label='المنتج',
        empty_label="اختر المنتج",
        required=False,
        widget=Select2Widget(attrs={'class':'form-control',
                                     'placeholder':'المنتج',
                                       'data-width': '100%', 'height': '36px'}))
    class Meta:
        model = InvoicesSalesBody
        fields = '__all__'
        widgets = {
            'DELETE': forms.CheckboxInput(),
            'invoiceHeadID': forms.Select(attrs={'class':'form-control', 'placeholder':'رأس الفاتورة'}),
            'inventoryID': forms.Select(attrs={'class':'form-control', 'placeholder':'المخزن'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control debit-input quantity', 'placeholder':'الكمية'}),
            'unit_price': forms.NumberInput(attrs={'class':'form-control unit_price', 'placeholder':'سعر الوحدة'}),
            'discount': forms.NumberInput(attrs={'class':'form-control discount' , 'placeholder':'الخصم'}),
            'total_price_before_tax': forms.NumberInput(attrs={'readonly':'readonly','class':'form-control total_price_before_tax', 'placeholder':'إجمالي السعر'}),
            'tax_rate': forms.NumberInput(attrs={'class':'form-control tax_rate', 'placeholder':'نسبة الضريبة'}),
            'tax_value': forms.NumberInput(attrs={'readonly':'readonly','class':'form-control tax_value', 'placeholder':'قيمة الضريبة'}),
            'total_price_after_tax': forms.NumberInput(attrs={'readonly':'readonly','class':'form-control total_price_after_tax', 'placeholder':'إجمالي السعر بعد الخصم'}),
            'total_price_local_currency': forms.NumberInput(attrs={'readonly':'readonly','class':'form-control total_price_local_currency', 'placeholder':'إجمالي السعر بعد الخصم'}),
        }

    #تعيين قيمة إفتراضية للمخزن في تفاصيل الفاتورة
    # def __init__(self, *args, **kwargs):
    #     super(InvoiceBodyForm, self).__init__(*args, **kwargs)

    #     invoice_head = None
        
    #     if 'instance' in kwargs:
    #         # إذا كان النموذج يتعامل مع كائن موجود
    #         invoice_head = kwargs['instance'].invoiceHeadID
    #     else:
    #         # إذا كان النموذج جديدًا
    #         invoice_head = kwargs['initial'].get('invoiceHeadID', None)

    #     if invoice_head and not self.instance.pk:
    #         # تعيين المخزن الافتراضي من رأس الفاتورة
    #         self.fields['inventoryID'].initial = invoice_head.inventoryID

    #     # هذا الحقل يظل قابلًا للتعديل
    #     self.fields['inventoryID'].widget.attrs.update({'class': 'form-control'})

    #التأكد من إضافة منتج قبل الحفظ
    def clean(self):
        cleaned_data = super().clean()
        # التحقق مما إذا كان السطر محددًا للحذف
        delete = cleaned_data.get('DELETE')
        if delete:
            return cleaned_data  # تجاوز التحقق إذا كان السطر سيتم حذفه
        item = cleaned_data.get('itemID')
        # التحقق من أن itemID ليس None وأنه يحتوي على قيمة صحيحة
        if not item:
            raise forms.ValidationError('يجب إضافة منتج أو حذف السطر.')
        return cleaned_data

# إنشاء نموذج المجموعة باستخدام الفئة الأساسية المخصصة
InvoiceBodyFormSet = modelformset_factory(InvoicesSalesBody, form=InvoiceBodyForm, can_delete=True, extra=3)
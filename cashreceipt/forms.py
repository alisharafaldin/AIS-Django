from django import forms
from .models import CashReceiptHead, CashReceiptBody
from basicinfo.models import Countries
from sales.models import Customers
from django.db.models import Q #لعمل أكثر من تصفية
from accounts.models import AccountsTree
from django.forms import modelformset_factory
from django_select2.forms import Select2Widget


class CashReceiptHeadForm(forms.ModelForm):
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
        model = CashReceiptHead
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'placeholder':'التاريخ'}),
            'typeTransactionID': forms.Select(attrs={'disabled':'disabled','class':'form-control', 'placeholder':'نوع المعاملة'}),
            'accountID': forms.Select(attrs={'class':'form-control', 'placeholder':'الحساب الدائن'}),
            'typePaymentID': forms.Select(attrs={'class':'form-control', 'placeholder':'طريقة الدفع'}),
            'employeeID': forms.Select(attrs={'class':'form-control', 'placeholder':'الموظف'}),
            'inventoryID': forms.Select(attrs={'class':'form-control', 'placeholder':'الفرع'}),
            'amountCredit': forms.NumberInput(attrs={'class':'form-control amountCredit', 'placeholder':'المبلغ الدائن'}),
            'rate': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'سعر الصرف'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'وصف الفاتورة', 'style':'height: 50px;'}),
            'attachments': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'updated_at': forms.DateTimeInput(attrs={'class':'form-control', 'type':'datetime-local', 'placeholder':'تاريخ التعديل'}),
            'details': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        company_id = kwargs.pop('companyID', None)  # استلام الشركة الحالية من العرض
        super().__init__(*args, **kwargs)
        
        # تخصيص تسمية حقل currencyID
        self.fields['currencyID'].label_from_instance = lambda obj: obj.currency_ar

        # تصفية العملاء بناءً على الشركة
        if company_id: 
            self.fields['customerID'].queryset = Customers.objects.filter(companyID_id=company_id)
   
class CashReceiptBodyForm(forms.ModelForm):
    DELETE = forms.BooleanField(required=False, initial=False)
    currencyID = forms.ModelChoiceField(
        queryset=Countries.objects.all(),
        empty_label="اختر العملة",
        widget=forms.Select(attrs={'class': 'form-control'}),
        )

    class Meta:
        model = CashReceiptBody
        fields = '__all__'
        widgets = {
            'DELETE': forms.CheckboxInput(),
            'CashReceiptHeadID': forms.Select(attrs={'class':'form-control', 'placeholder':'رأس سند القبض'}),
            'accountID': forms.Select(attrs={'class':'form-control', 'placeholder':'الحساب المدين'}),
            'employeeID': forms.Select(attrs={'class':'form-control', 'placeholder':'الموظف'}),
            'amountDebit': forms.NumberInput(attrs={'class':'form-control amountDebit', 'placeholder':'المبلغ المدين'}),
            'rate': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'سعر الصرف'}),
            'amountDebit_local_currency': forms.NumberInput(attrs={'readonly':'readonly','class':'form-control total_price_local_currency', 'placeholder':'إجمالي السعر بعد الخصم'}),
            'transactionNumber': forms.Textarea(attrs={'class':'form-control', 'placeholder':'رقم العملية', 'style':'height: 50px;'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'الوصف', 'style':'height: 50px;'}),
           
        }
    def __init__(self, *args, **kwargs):
        company_id = kwargs.pop('companyID', None)  # استلام الشركة الحالية من العرض
        super(CashReceiptBodyForm, self).__init__(*args, **kwargs)  # تم تصحيح هذا السطر
        
        # تخصيص تسمية حقل currencyID
        self.fields['currencyID'].label_from_instance = lambda obj: obj.currency_ar
        if company_id:
            print(f"Filtering accounts with companyID: {company_id}")  # Debugging line
            self.fields['accountID'].queryset = AccountsTree.objects.filter(
                Q(companyID=company_id) | Q(companyID__isnull=True), typeID=2)
        else:
            self.fields['accountID'].queryset = AccountsTree.objects.none()
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
        item = cleaned_data.get('accountID')
        # التحقق من أن accountID ليس None وأنه يحتوي على قيمة صحيحة
        if not item:
            raise forms.ValidationError('يجب إضافة حساب أو حذف السطر.')
        return cleaned_data

# إنشاء نموذج المجموعة باستخدام الفئة الأساسية المخصصة
CashReceiptFormSet = modelformset_factory(CashReceiptBody, form=CashReceiptBodyForm, can_delete=True, extra=2)
from django import forms
from sales.models import Customers, Inventory
from purchases.models import Suppliers
from products.models import Items, ItemGrop
from .models import Persons, LegalPersons, BasicInfo, Countries, Region, States, Cities, BusinessScope
from companys.models import Company
from accounts.models import AccountsTree
from django_select2.forms import Select2Widget

class InvoiceSearchForm(forms.Form):
    sequence = forms.CharField(
        required=False, 
        label='رقم القيد',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم القيد'})
    )

    currencyID = forms.ModelChoiceField(
        queryset=Countries.objects.all(),
        label='العملة',
        empty_label="اختر العملة",
        required=False,
        widget=forms.Select(attrs={'name':'search_currencyID', 'class':'form-control', 'placeholder':'العملة'})
    )

    inventoryID = forms.ModelChoiceField(
        queryset=Inventory.objects.all(),
        label='المخزن',
        empty_label="اختر المخزن",
        required=False,
        widget=forms.Select(attrs={'class':'form-control', 'placeholder':'المخزن'})
    )

    customerID = forms.ModelChoiceField(
        queryset=Customers.objects.all(),
        label='العميل',
        empty_label="اختر العميل",
        required=False,
        widget=Select2Widget(attrs={'class':'form-control', 'placeholder':'العميل'})
    )
  
    suppliersID = forms.ModelChoiceField(
        queryset=Suppliers.objects.all(),
        label='المورد',
        empty_label="اختر المورد",
        required=False,
        widget=Select2Widget(attrs={'class':'form-control', 'placeholder':'المورد'})
    )

    itemID = forms.ModelChoiceField(
        queryset=Items.objects.all(),
        label='المنتج',
        empty_label="اختر المنتج",
        required=False,
        widget=Select2Widget(attrs={'class':'form-control', 'placeholder':'المنتج'})
    )
   
    ItemGrop = forms.ModelChoiceField(
        queryset=ItemGrop.objects.all(),
        label='الأصناف',
        empty_label="اختر الصنف",
        required=False,
        widget=Select2Widget(attrs={'class':'form-control', 'placeholder':'الصنف'})
    )
    
    companyID = forms.ModelChoiceField(
        queryset=Company.objects.all(),
        label='الشركة',
        empty_label="اختر الشركة",
        required=False,
        widget=Select2Widget(attrs={'class':'form-control', 'placeholder':'الشركة'})
    )
    
    accountID = forms.ModelChoiceField(
        queryset=AccountsTree.objects.all(),
        label='الحساب',
        empty_label="اختر الحساب",
        required=False,
        widget=Select2Widget(attrs={'class':'form-control', 'placeholder':'العميل'})
    )

    businessScopeID = forms.ModelChoiceField(
        queryset=BusinessScope.objects.all(),
        label='مجال العمل',
        empty_label="اختر مجال العمل",
        required=False,
        widget=Select2Widget(attrs={'class':'form-control', 'placeholder':'مجال العمل'})
    )

    regionID = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        label='المنق',
        empty_label="اختر المنطقة ",
        required=False,
        widget=Select2Widget(attrs={'class':'form-control', 'placeholder':'المنطقة'})
    )

    stateID = forms.ModelChoiceField(
        queryset=States.objects.all(),
        label='الولاية',
        empty_label="اختر الولاية ",
        required=False,
        widget=Select2Widget(attrs={'class':'form-control', 'placeholder':'الولاية'})
    )

    cityID = forms.ModelChoiceField(
        queryset=Cities.objects.all(),
        label='المدينة',
        empty_label="اختر المدينة ",
        required=False,
        widget=Select2Widget(attrs={'class':'form-control', 'placeholder':'المدينة'})
    )


    def __init__(self, *args, **kwargs):
        company_id = kwargs.pop('companyID', None)  # احصل على companyID من kwargs
        super(InvoiceSearchForm, self).__init__(*args, **kwargs)
        # تخصيص تسمية حقل currencyID
        self.fields['currencyID'].label_from_instance = lambda obj: obj.currency_ar
        if company_id:
            # تخصيص queryset بناءً على companyID
            self.fields['currencyID'].queryset = Countries.objects.filter(companyID=company_id)
            self.fields['inventoryID'].queryset = Inventory.objects.filter(companyID=company_id)
            self.fields['customerID'].queryset = Customers.objects.filter(companyID=company_id)
            self.fields['supplierID'].queryset = Suppliers.objects.filter(companyID=company_id)
            self.fields['itemID'].queryset = Items.objects.filter(companyID=company_id)
            self.fields['ItemGrop'].queryset = ItemGrop.objects.filter(companyID=company_id)

class BasicInfoForm(forms.ModelForm):
    class Meta:
        model = BasicInfo
        fields = '__all__'
        widgets = {
            'nationalityID': forms.Select(attrs={'class':'form-control', 'placeholder':'الجنسية'}),
            'countryID': forms.Select(attrs={'class':'form-control', 'placeholder':'الدولة'}),
            'regionID': forms.Select(attrs={'class':'form-control', 'placeholder':'المنطقة'}),
            'stateID': forms.Select(attrs={'class':'form-control', 'data-placeholder': 'اختر الولاية'}),
            'cityID': forms.Select(attrs={'class':'form-control', 'placeholder':'المدينة'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'وصف العنوان '}),
            'google_maps_location': forms.URLInput(attrs={'class':'form-control', 'placeholder':'العوان على خرائط قوقل'}),
            'latitude': forms.TextInput(attrs={'class':'form-control', 'type':'number', 'placeholder':'خط العرض latitude'}),
            'longitude': forms.TextInput(attrs={'class':'form-control', 'type':'number', 'placeholder':'خط الطول longitude'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الهاتف'}),
            'phoneOther': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم هاتف آخر'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'إيميل'}),
            'website': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'الموقع الإلكتروني'}),
            'fax': forms.TextInput(attrs={'class':'form-control', 'placeholder':'فاكس'}),
            'POBox': forms.TextInput(attrs={'class':'form-control', 'placeholder':'صندوق بريد'}),
            'bankID': forms.Select(attrs={'class':'form-control', 'placeholder':'البنك'}),
            'branchBankID': forms.Select(attrs={'class':'form-control', 'placeholder':'الفرع'}),
            'typeAccBankID': forms.Select(attrs={'class':'form-control', 'placeholder':'نوع الحساب'}),
            'accountNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الحساب'}),
            'IBANNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الآيبان'}),
            'ownerAccount': forms.TextInput(attrs={'class':'form-control', 'placeholder':'صاحب الحساب'}),
            'attachments': forms.ClearableFileInput(attrs={'class':'form-control', 'placeholder':'مرفقات'}),
            'photo': forms.ClearableFileInput(attrs={'class':'form-control', 'placeholder':'صورة / لوقو'}),
            'notes': forms.TextInput(attrs={'class':'form-control', 'placeholder':'ملاحظات'}),
            'documentLink': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رابط المستندات'}),
            'active': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'نشط'}),
        }

class PersonForm(forms.ModelForm):
    class Meta:
        model = Persons
        fields = '__all__'
        widgets = {
            'basicInfoID': forms.Select(attrs={'class':'form-control', 'placeholder':'المعلومات الأساسية'}),
            'f_Name_ar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الأول'}),
            's_Name_ar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الثاني'}),
            't_Name_ar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الثالث'}),
            'fo_Name_ar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الرابع'}),
            'f_Name_en': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الأول'}),
            's_Name_en': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الثاني'}),
            't_Name_en': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الثالث'}),
            'fo_Name_en': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الإسم الرابع'}),
            'dateOfBirth': forms.TextInput(attrs={'class':'form-control', 'type':'date', 'placeholder':'تاريخ الميلاد'}),
            'genderID': forms.Select(attrs={'class':'form-control', 'placeholder':'الجنس', 'value':'الجنس'}),
            'socialStatusID': forms.Select(attrs={'class':'form-control', 'placeholder':'الحالة الإجتماعية'}),
            'typeID': forms.Select(attrs={'class':'form-control', 'placeholder':'نوع الهوية'}),
            'id_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'رقم الهوية'}),
            'id_ExpiredDate': forms.TextInput(attrs={'class':'form-control','type':'date', 'placeholder':'تاريخ إنتهاء الهوية'}),
            'workTradeID': forms.Select(attrs={'class':'form-control', 'placeholder':'المهنة'}),
            'workSpecialtyID': forms.Select(attrs={'class':'form-control', 'placeholder':'التخصص'}),
            'skillsID': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'المهارات'}),
            'languagesID': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'اللغات'}),
            'jobTitleID': forms.Select(attrs={'class':'form-control', 'placeholder':'المسمى الوظيفي'}),
        }

class LegalPersonsForm (forms.ModelForm):
  class Meta:
      model = LegalPersons
      fields = '__all__'
      widgets = {
        'basicInfoID': forms.Select(attrs={'class':'form-control', 'placeholder':'المعلومات الأساسية'}),
        'businessScopeID': forms.Select(attrs={'class':'form-control', 'placeholder':'مجال العمل'}),
        'businessScopeSpecializationID': forms.Select(attrs={'class':'form-control', 'placeholder':'تخصص مجال العمل'}),
        'name_ar': forms.TextInput(attrs={'class':'form-control','placeholder':'إسم الشركة عربي'}),
        'acronym_ar': forms.TextInput(attrs={'class':'form-control','placeholder':'الإسم المختصر عربي'}),
        'name_en': forms.TextInput(attrs={'class':'form-control','placeholder':'إسم الشركة إنجليزي'}),
        'acronym_en': forms.TextInput(attrs={'class':'form-control','placeholder':'الإسم المختصر إنجليزي'}),
        'who_are_we': forms.TextInput(attrs={'class':'form-control', 'placeholder':'من نحن'}),
        'businessTypeID': forms.Select(attrs={'class':'form-control', 'placeholder':'نوع الشركة'}),
        'administrator': forms.TextInput(attrs={'class':'form-control','placeholder':'الموظف المسؤول'}),
        'phoneAdmin': forms.TextInput(attrs={'class':'form-control','placeholder':'هاتف الموظف المسؤول'}),
        'taxNumber': forms.TextInput(attrs={'class':'form-control','placeholder':'الرقم الضريبي'}),
    }
    

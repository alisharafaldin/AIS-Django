from django import forms
from .models import  Inventory



class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'
        widgets = {
            'name_ar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الصنف عربي'}),
            'name_en': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الصنف إنجليزي'}),
            'countryID': forms.Select(attrs={'class':'form-control', 'placeholder':'الدولة'}),
            'regionID': forms.Select(attrs={'class':'form-control', 'placeholder':'المنطقة'}),
            'stateID': forms.NumberInput(attrs={'class':'form-control debit-input', 'placeholder':'الولاية'}),
            'cityID': forms.Select(attrs={'class':'form-control', 'placeholder':'المدينة'}),
            'address': forms.ClearableFileInput(attrs={'class':'form-control', 'placeholder':'وصف العنوان'}),
            'google_maps_location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'عنوان خرائط قوقل'}),
            'administratorID': forms.Select(attrs={'class':'form-control', 'placeholder':'أمين المخزن'}),
            'phoneAdmin': forms.TextInput(attrs={'class':'form-control', 'placeholder':'هاتف أمين المخزن'}),
            'notes': forms.TextInput(attrs={'class':'form-control', 'placeholder':'ملاحظات'}),
            'available': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'متاح'}),     
        }



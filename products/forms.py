from django import forms
from .models import  ItemType, ItemGrop, Item, ItemDetails
from django.forms import modelformset_factory, formset_factory
from django.forms import BaseModelFormSet

class ItemTypeForm(forms.ModelForm):
    class Meta:
        model = ItemType
        fields = '__all__'
        widgets = {
            'name_ar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'إسم الحساب عربي'}),
            'name_en': forms.TextInput(attrs={'class':'form-control', 'placeholder':'إسم الحساب إنجليزي'}),
        }

class ItemGropForm(forms.ModelForm):
    class Meta:
        model = ItemGrop
        fields = '__all__'
        widgets = {
            'itemTypeID': forms.Select(attrs={'class':'form-control', 'placeholder':'معرف نوع الصنف'}),
            'name_ar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'مجموعة الأصناف عربي'}),
            'name_en': forms.TextInput(attrs={'class':'form-control', 'placeholder':'مجموعة الأصناف إنجليزي'}),
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'itemGropID': forms.Select(attrs={'class':'form-control', 'placeholder':'معرف مجموعة الصنف'}),
            'name_ar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'مجموعة الأصناف عربي'}),
            'name_en': forms.TextInput(attrs={'class':'form-control', 'placeholder':'مجموعة الأصناف إنجليزي'}),
        }

class ItemDetailsForm(forms.ModelForm):
    class Meta:
        model = ItemDetails
        fields = '__all__'
        widgets = {
            'itemID': forms.Select(attrs={'class':'form-control', 'placeholder':'معرف مجموعة الصنف'}),
            'colorID': forms.Select(attrs={'class':'form-control', 'placeholder':'لون الصنف'}),
            'sizeID': forms.Select(attrs={'class':'form-control', 'placeholder':'مقاس الصنف'}),
            'photo': forms.ClearableFileInput(attrs={'class':'form-control', 'placeholder':'صورة شخصية'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'وصف الصنف'}),

        }



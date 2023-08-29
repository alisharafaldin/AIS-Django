from django import forms
from .models import ShareholdersInfo , Contracts

class ShareholderForm(forms.ModelForm):
    class Meta:
        model = ShareholdersInfo
        fields = '__all__'
        # لعمل إستثناء حقل
        # exclude = ('f_Name_ar')
        widgets = {
          'marketerID': forms.Select(attrs={'class':'form-control', 'placeholder':'المسوق'}),
        }

class ContractsForm(forms.ModelForm):
    class Meta:
        model = Contracts
        fields = '__all__'
        widgets = {
            'shareholdersID': forms.Select(attrs={'placeholder':'المساهم','class':'form-control'}),
            'dateOfContract': forms.TextInput(attrs={'placeholder':'تاريخ العقد','class':'form-control'}),
            'contractNumber': forms.TextInput(attrs={'placeholder':'رقم العقد','class':'form-control'}),
            'axisID': forms.Select(attrs={'placeholder':'المحور','class':'form-control'}),
            'numberReceipt': forms.TextInput(attrs={'placeholder':'رقم الإيصال','class':'form-control'}),
            'numberOfShares': forms.TextInput(attrs={'placeholder':'عدد الأسهم','class':'form-control'}),
            'amountOfShare': forms.TextInput(attrs={'placeholder':'سعر السهم','class':'form-control'}),
            'profitOfShare': forms.TextInput(attrs={'placeholder':'ربح السهم','class':'form-control'}),
            'dateOfDividend': forms.TextInput(attrs={'placeholder':'تاريخ توزيع الأرباح ','class':'form-control'}),
            'witnes1ID': forms.Select(attrs={'placeholder':'الشاهد الأول','class':'form-control'}),
        }
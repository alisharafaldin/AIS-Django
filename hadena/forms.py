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
      'dateOfContract': forms.TextInput(attrs={'type':'date', 'placeholder':'تاريخ العقد','class':'form-control'}),
      'contractNumber': forms.TextInput(attrs={'placeholder':'رقم العقد','class':'form-control'}),
      'cycleID': forms.Select(attrs={'placeholder':'الدورة','class':'form-control'}),
      'typeContractID': forms.Select(attrs={'placeholder':'نوع العقد','class':'form-control'}),
      'receiptID': forms.Select(attrs={'placeholder':'رقم الإيصال','class':'form-control'}),
      'numberOfShares': forms.TextInput(attrs={'placeholder':'عدد الأسهم','class':'form-control'}),
      'amountOfShare': forms.TextInput(attrs={'placeholder':'سعر السهم','class':'form-control'}),
      'profitRate': forms.TextInput(attrs={'placeholder':'معدل الربحية % ','class':'form-control'}),
      'dateOfDividend': forms.TextInput(attrs={'type':'date', 'placeholder':'تاريخ توزيع الأرباح ','class':'form-control'}),
      'witnes1ID': forms.Select(attrs={'placeholder':'الشاهد الأول','class':'form-control'}),
      'witnes2ID': forms.Select(attrs={'placeholder':'الشاهد الثاني','class':'form-control'}),
      'notes': forms.TextInput(attrs={'placeholder':'ملاحظات','class':'form-control'}),
    }
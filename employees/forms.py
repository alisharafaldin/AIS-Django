from django import forms
from .models import EmployeeInfo

class EmpForm(forms.ModelForm):
  class Meta:
      model = EmployeeInfo
      fields = '__all__'
      # لعمل إستثناء حقل
      # exclude = ('f_Name_ar')
      widgets = {
        'workEndDate': forms.TextInput(attrs={'class':'form-control','type':'date', 'placeholder':'تاريخ بداية العمل'}),
        'workEndDate': forms.TextInput(attrs={'class':'form-control','type':'date', 'placeholder':'تاريخ بداية العمل'}),
        'contractSalary': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'إجمالي الراتب'}),
        'fixedExtra': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'إضافي ثابت'}),
        'workingStatusID': forms.Select(attrs={'class':'form-control', 'placeholder':'حالة العمل'}),
        'workStartDate': forms.TextInput(attrs={'class':'form-control','type':'date', 'placeholder':'تاريخ نهاية العمل'}),
      }

from django.db import models
from datetime import date 
from employees.models import EmpInfo
from employees.models import TypeID
from employees.models import TypeAccBank
from employees.models import BranchBank
from employees.models import Bank
from employees.models import Cities
from employees.models import WorkSpecialty
from employees.models import WorkTrade
from employees.models import SocialStatus
from employees.models import Gender
from employees.models import Countries
from employees.models import States
from employees.models import Company

class Axis(models.Model):
    axis_ar = models.CharField(verbose_name='المحور عربي',max_length=100)
    axis_er = models.CharField(verbose_name='المحور إنجليزي',max_length=100, blank=True, null=True)
    directSupervisor = models.CharField(verbose_name='المشرف المباشر',max_length=100, blank=True, null=True)
    phoneDirectSupervisor = models.CharField(verbose_name='جوال المشرف المباشر',max_length=100, blank=True, null=True)
    countryID = models.ForeignKey(Countries, verbose_name='الدولة',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    statesID = models.ForeignKey(States, verbose_name='المنطقة',on_delete=models.PROTECT, blank=True, null=True)
    def __str__(self):
        return str(self.axis_ar)

class ShareholdersInfo(models.Model):
    f_Name_ar = models.CharField(verbose_name='الإسم الأول عربي',max_length=100, blank=True, null=True)
    s_Name_ar = models.CharField(verbose_name='الإسم الثاني عربي',max_length=100, blank=True, null=True)
    t_Name_ar = models.CharField(verbose_name='الإسم الثالث عربي',max_length=100, blank=True, null=True)
    fo_Name_ar = models.CharField(verbose_name='الإسم الرابع عربي',max_length=100, blank=True, null=True)
    f_Name_en = models.CharField(verbose_name='الإسم الأول إنجليزي',max_length=100, blank=True, null=True)
    s_Name_en = models.CharField(verbose_name='الإسم الثاني إنجليزي',max_length=100, blank=True, null=True)
    t_Name_en = models.CharField(verbose_name='الإسم الثالث إنجليزي',max_length=100, blank=True, null=True)
    fo_Name_en = models.CharField(verbose_name='الإسم الرابع إنجليزي',max_length=100, blank=True, null=True)
    dateOfBirth = models.DateField(verbose_name='تاريخ الميلاد', blank=True, null=True)
    genderID = models.ForeignKey(Gender, verbose_name='الجنس', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    nationalityID = models.ForeignKey(Countries, verbose_name='الجنسية', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    socialStatusID = models.ForeignKey(SocialStatus, verbose_name='الحالة الإجتماعية', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    workTradeID = models.ForeignKey(WorkTrade, verbose_name='المهنة', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    workSpecialtyID = models.ForeignKey(WorkSpecialty, verbose_name='التخصص', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    mobileNumber = models.CharField(verbose_name='رقم الجوال',max_length=100, blank=True, null=True)
    mobileNumberAnother = models.CharField(verbose_name='رقم جوال آخر',max_length=100, blank=True, null=True)
    # countreyID = models.ForeignKey(Countries, verbose_name='الدولة', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    companyID = models.ForeignKey(Company, verbose_name='الشركة', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    stateID = models.ForeignKey(States, verbose_name='الولاية', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    cityID = models.ForeignKey(Cities, verbose_name='المدينة', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    detailsAddress = models.CharField(verbose_name='وصف عنوان السكن',max_length=100, blank=True, null=True)
    bankID = models.ForeignKey(Bank, verbose_name='البنك',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    branchBankID = models.ForeignKey(BranchBank, verbose_name='فرع البنك',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    typeAccBankID = models.ForeignKey(TypeAccBank, verbose_name='نوع الحساب',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    accountNumber = models.CharField(verbose_name='رقم الحساب المصرفي',max_length=100, blank=True, null=True)
    IBANNumber = models.CharField(verbose_name='رقم الآيبان المصرفي',max_length=100, blank=True, null=True)
    ownerAccount = models.CharField(verbose_name='إسم صاحب الحساب',max_length=100, blank=True, null=True)
    typeID = models.ForeignKey(TypeID , verbose_name='نوع الهوية',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    id_number = models.CharField(verbose_name='رقم الهوية',max_length=100, blank=True, null=True)
    id_ExpiredDate = models.DateField(verbose_name='تاريخ إنتهاء الهوية', blank=True, null=True)
    Photo = models.ImageField(verbose_name='صورة شخصية', upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    notes = models.TextField(verbose_name='ملاحظات', blank=True, null=True)
    documentLink = models.CharField(verbose_name='رابط المستندات',max_length=100, blank=True, null=True)
    marketerID = models.ForeignKey(EmpInfo , verbose_name='المسووق',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الموظف في حالة حذف المسوق
    def __str__(self):
        return str(self.f_Name_ar) + " " + str(self.s_Name_ar)

class Contracts(models.Model):
    shareholdersID = models.ForeignKey(ShareholdersInfo, related_name='Shareholders', verbose_name='المساهم', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    dateOfContract = models.DateField(verbose_name='تاريخ العقد', blank=True, null=True)
    contractNumber = models.CharField(verbose_name='رقم العقد',max_length=100, blank=True, null=True)
    axisID = models.ForeignKey(Axis, verbose_name='المحور', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    numberReceipt = models.CharField(verbose_name='رقم الإيصال',max_length=100, blank=True, null=True)
    numberOfShares = models.IntegerField(verbose_name='عدد الأسهم', default=1)
    amountOfShare = models.IntegerField(verbose_name='سعر السهم', default=1200000)
    profitOfShare = models.IntegerField(verbose_name='ربح السهم', default=8)
    dateOfDividend = models.DateField(verbose_name='تاريخ توزيع الأرباح', blank=True, null=True)
    witnes1ID = models.ForeignKey(EmpInfo , verbose_name='الشاهد الأول',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الموظف في حالة حذف المسوق
    # Witnes2ID = models.ForeignKey(EmpInfo , verbose_name='الشاهد الثاني',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الموظف في حالة حذف المسوق
    def __str__(self):
        return str(self.shareholdersID)
    
    
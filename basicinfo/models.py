from django.db import models
from datetime import date 
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

class Countries(models.Model):
  name_ar = models.CharField(verbose_name='إسم الدولة عربي',max_length=50)
  name_en = models.CharField(verbose_name='إسم الدولة إنجليزي',max_length=50)
  code = models.CharField(verbose_name='الرمز الموحد',max_length=50)
  callKey = models.CharField(verbose_name='مفتاح الإتصال',max_length=50)
  nationality_ar = models.CharField(verbose_name='الجنسية عربي',max_length=50, blank=True, null=True)
  nationality_en = models.CharField(verbose_name='الجنسية إنجليزي',max_length=50, blank=True, null=True)
  currency_ar = models.CharField(verbose_name='العملة عربي',max_length=50, blank=True, null=True)
  currency_en = models.CharField(verbose_name='العملة إنجليزي',max_length=50, blank=True, null=True)
  fractional_ar = models.CharField(verbose_name='الكسر عربي',max_length=50, blank=True, null=True)
  fractional_en = models.CharField(verbose_name='الكسر إنجليزي',max_length=50, blank=True, null=True)
  symbol_ar = models.CharField(verbose_name='الرمز عربي',max_length=50, blank=True, null=True)
  symbol_en = models.CharField(verbose_name='الرمز إنجليزي',max_length=50, blank=True, null=True)
  
  def __str__(self):
      return str(self.currency_ar)
    
  def get_currency_ar(self):
        return str(self.currency_ar)
  
class Region(models.Model):
  countryID = models.ForeignKey(Countries, verbose_name='معرف الدولة',on_delete=models.PROTECT) #لن يتم حزف الصنف في حالة حذف الموظف
  name_ar = models.CharField(verbose_name='إسم المنطقة عربي',max_length=50, blank=True, null=True)
  name_en = models.CharField(verbose_name='إسم المنطقة إنجليزي',max_length=50, blank=True, null=True)
  capitalRegion = models.CharField(verbose_name='عاصمة المنطقة',max_length=50, blank=True, null=True)
  imageRegion = models.ImageField(verbose_name=' صورة للمنطقة', upload_to='photos/%Y/%m/%d/', null=True, blank=True)
  def __str__(self):
    return str(self.name_ar)
    
class States(models.Model):
  regionID = models.ForeignKey(Region, verbose_name='معرف المنطقة',on_delete=models.PROTECT) #لن يتم حزف الصنف في حالة حذف الموظف
  name_ar = models.CharField(verbose_name='إسم الولاية عربي',max_length=50, blank=True, null=True)
  name_en = models.CharField(verbose_name='إسم الولاية إنجليزي',max_length=50, blank=True, null=True)
  capitalState = models.CharField(verbose_name='عاصمةالولاية',max_length=50, blank=True, null=True)
  population = models.IntegerField(verbose_name='عدد السكان', blank=True, null=True)
  def __str__(self):
    return str(self.name_ar)
  
class Cities(models.Model):
    stateID = models.ForeignKey(States, verbose_name='معرف الولاية',on_delete=models.PROTECT) #لن يتم حزف الصنف في حالة حذف الموظف
    name_ar = models.CharField(verbose_name='إسم المدينة عربي',max_length=50, blank=True, null=True)
    name_en = models.CharField(verbose_name='إسم المدينة إنجليزي',max_length=50, blank=True, null=True)
    capitalCity = models.CharField(verbose_name='عاصمةالمحلية',max_length=50, blank=True, null=True)
    population = models.IntegerField(verbose_name='عدد السكان', blank=True, null=True)
    def __str__(self):
        return str(self.name_ar)

class CalendarYears(models.Model):
    year = models.CharField(verbose_name='العام',max_length=50)
    def __str__(self):
        return str(self.year)

class CalendarMonths(models.Model):
    month_ar = models.CharField(verbose_name='الشهر عربي',max_length=50)
    month_en = models.CharField(verbose_name='الشهر إنجليزي',max_length=50)
    month_en_sort = models.CharField(verbose_name='إختصار الشهر إنجليزي',max_length=50)
    daysOfMonth = models.CharField(verbose_name='أيام الشهر',max_length=50)
    def __str__(self):
        return str(self.month_ar)

class CalendarWeek(models.Model):
    day_ar = models.CharField(verbose_name='اليوم عربي',max_length=50)
    day_en = models.CharField(verbose_name='اليوع إنجليزي',max_length=50)
    day_short_en = models.CharField(verbose_name=' اليوع إنجليزي مختصر',max_length=50)
    workDay = models.BooleanField(default=True, verbose_name='يوم عمل',max_length=50)
    def __str__(self):
        return str(self.day_ar)

class Gender(models.Model):
    gender_ar = models.CharField(verbose_name='الجنس عربي',max_length=50)
    gender_en = models.CharField(verbose_name='الجنس إنجليزي',max_length=50)
    def __str__(self):
        return str(self.gender_ar)

class SocialStatus(models.Model):
    socialStatus_ar = models.CharField(verbose_name='الحالة الإجتماعية عربي',max_length=50)
    socialStatus_en = models.CharField(verbose_name='الحالة الإجتماعية إنجليزي',max_length=50)
    def __str__(self):
        return str(self.socialStatus_ar)

class WorkTrade(models.Model):
    workTrade_ar = models.CharField(verbose_name='المهنة عربي',max_length=100)
    workTrade_en = models.CharField(verbose_name='المهنة إنجليزي',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.workTrade_ar)

class WorkSpecialty(models.Model):
    workTradeID = models.ForeignKey(WorkTrade, verbose_name='معرف المهنة',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    workSpecialty_ar = models.CharField(verbose_name='التخصص عربي',max_length=100)
    workSpecialty_en = models.CharField(verbose_name='التخصص إنجليزي',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.workSpecialty_ar)

class JobTitle(models.Model):
    name_ar = models.CharField(verbose_name='المسمى الوظيفي عربي',max_length=100)
    name_en = models.CharField(verbose_name='المسمى الوظيفي إنجليزي',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.name_ar) 
       
class WorkingStatus(models.Model):
    workingStatus_ar = models.CharField(verbose_name='حالة العمل عربي',max_length=100)
    workingStatus_en = models.CharField(verbose_name='حالة العمل إنجليزي',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.workingStatus_ar)

class Bank(models.Model):
    bank_ar = models.CharField(verbose_name='البنك عربي',max_length=100)
    bank_en = models.CharField(verbose_name='البنك إنجليزي',max_length=100,blank=True, null=True)
    bank_Symbol = models.CharField(verbose_name=' رمز البنك',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.bank_ar)
    
class BranchBank(models.Model):
    bankID = models.ForeignKey(Bank, verbose_name='معرف البنك',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    branchBank_AR = models.CharField(verbose_name='قرع البنك عربي',max_length=100)
    branchBank_EN = models.CharField(verbose_name='قرع البنك إنجليزي',max_length=100,blank=True, null=True)
    bank_Symbol = models.CharField(verbose_name=' رمز البنك',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.branchBank_AR)
    
class TypeAccBank(models.Model):
    TypeAccBank_AR = models.CharField(verbose_name='نوع الحساب عربي',max_length=100)
    TypeAccBank_EN = models.CharField(verbose_name='نوع الحساب إنجليزي',max_length=100,blank=True, null=True)
    bank_Symbol = models.CharField(verbose_name=' رمز البنك',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.TypeAccBank_AR)

class TypeID(models.Model):
    typeID_ar = models.CharField(verbose_name='نوع الهوية عربي',max_length=100)
    typeID_en = models.CharField(verbose_name='نوع الهوية إنجليزي',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.typeID_ar)

class TypeTransaction(models.Model):
  typeTransaction_ar = models.CharField(verbose_name='نوع المعاملة عربي',max_length=100)
  typeTransaction_en = models.CharField(verbose_name='نوع المعاملة إنجليزي',max_length=100,blank=True, null=True)
  def __str__(self):
    return str(self.typeTransaction_ar)
  
class Project(models.Model):
    name_ar = models.CharField(verbose_name='المشروع عربي',max_length=100)
    name_er = models.CharField(verbose_name='المشروع إنجليزي',max_length=100)
    directSupervisor = models.CharField(verbose_name='المشرف المباشر',max_length=100)
    phoneDirectSupervisor = models.CharField(verbose_name='جوال المشرف المباشر',max_length=100)
    countryID = models.ForeignKey(Countries, verbose_name='الدولة',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    regionID = models.ForeignKey(Region, verbose_name='المنطقة',on_delete=models.PROTECT, blank=True, null=True)
    def __str__(self):
        return str(self.name_ar)
    
class SubProject(models.Model):
    projectID = models.ForeignKey(Project, default=1, verbose_name='المشروع الرئيس', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    noPro = models.CharField(verbose_name='رقم المشروع الفرعي ',default="1", max_length=100)
    name_ar = models.CharField(verbose_name='مشروع فرعي عربي',max_length=100)
    name_er = models.CharField(verbose_name='مشروع فرعي إنجليزي',max_length=100)
    def __str__(self):
        return str(self.noPro)

class Person(models.Model):
    f_Name_ar = models.CharField(verbose_name='الإسم الأول عربي',max_length=100, blank=True, null=True)
    s_Name_ar = models.CharField(verbose_name='الإسم الثاني عربي',max_length=100, blank=True, null=True)
    t_Name_ar = models.CharField(verbose_name='الإسم الثالث عربي',max_length=100, blank=True, null=True)
    fo_Name_ar = models.CharField(verbose_name='الإسم الرابع عربي',max_length=100, blank=True, null=True)
    f_Name_en = models.CharField(verbose_name='الإسم الأول إنجليزي',max_length=100, blank=True, null=True)
    s_Name_en = models.CharField(verbose_name='الإسم الثاني إنجليزي',max_length=100, blank=True, null=True)
    t_Name_en = models.CharField(verbose_name='الإسم الثالث إنجليزي',max_length=100, blank=True, null=True)
    fo_Name_en = models.CharField(verbose_name='الإسم الرابع إنجليزي',max_length=100, blank=True, null=True)
    dateOfBirth = models.DateField(verbose_name='تاريخ الميلاد', blank=True, null=True)
    genderID = models.ForeignKey(Gender, verbose_name='الجنس', default=1, on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    nationalityID = models.ForeignKey(Countries, related_name='nationalityID', default=1, verbose_name='الجنسية', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    socialStatusID = models.ForeignKey(SocialStatus, verbose_name='الحالة الإجتماعية', default=1, on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    typeID = models.ForeignKey(TypeID , verbose_name='نوع الهوية', default=1,on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    id_number = models.CharField(verbose_name='رقم الهوية',max_length=100, blank=True, null=True)
    id_ExpiredDate = models.DateField(verbose_name='تاريخ إنتهاء الهوية', blank=True, null=True)    
    countryID = models.ForeignKey(Countries, related_name='countryID', default=1, verbose_name='الدولة', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    regionID = models.ForeignKey(Region, verbose_name='المنطقة', default=1, on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    stateID = models.ForeignKey(States, verbose_name='الولاية', default=1, on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    cityID = models.ForeignKey(Cities, verbose_name='المدينة', default=1, on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    desAddress = models.CharField(verbose_name='وصف عنوان السكن',max_length=100, blank=True, null=True)
    mobileNumber = models.CharField(verbose_name='رقم الجوال',max_length=100, blank=True, null=True)
    mobileNumberAnother = models.CharField(verbose_name='رقم جوال آخر',max_length=100, blank=True, null=True)
    email = models.EmailField(verbose_name='البريد الإلكتروني',max_length=100, blank=True, null=True)
    workTradeID = models.ForeignKey(WorkTrade, verbose_name='المهنة', default=1, on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    workSpecialtyID = models.ForeignKey(WorkSpecialty, verbose_name='التخصص', default=1, on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    bankID = models.ForeignKey(Bank, verbose_name='البنك', default=1,on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    branchBankID = models.ForeignKey(BranchBank, verbose_name='فرع البنك', default=1,on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    typeAccBankID = models.ForeignKey(TypeAccBank, verbose_name='نوع الحساب', default=1,on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    accountNumber = models.CharField(verbose_name='رقم الحساب المصرفي',max_length=100, blank=True, null=True)
    IBANNumber = models.CharField(verbose_name='رقم الآيبان المصرفي',max_length=100, blank=True, null=True)
    ownerAccount = models.CharField(verbose_name='إسم صاحب الحساب',max_length=100, blank=True, null=True)
    photo = models.ImageField(verbose_name='صورة شخصية', upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    notes = models.TextField(verbose_name='ملاحظات', blank=True, null=True)
    attachments = models.FileField(verbose_name='مرفقات', blank=True, null=True)
    documentLink = models.CharField(verbose_name='رابط المستندات',max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_by', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='تاريخ الإنشاء',auto_now_add=True, blank=True, null=True)
    updated_by = models.ForeignKey(User, verbose_name='المُعدِل', related_name='updated_by', on_delete=models.PROTECT, blank=True, null=True)
    updated_at = models.DateTimeField(verbose_name='تاريخ التعديل', auto_now=True, blank=True, null=True)
   
    def __str__(self):
        return str(self.f_Name_ar)
    
    def fullName_ar(self):
        return f"{self.f_Name_ar} {self.s_Name_ar} {self.t_Name_ar} {self.fo_Name_ar}"
    
    def fullName_en(self):
        return f"{self.f_Name_en} {self.s_Name_en} {self.t_Name_en} {self.fo_Name_en}"
from django.db import models
from colorfield.fields import ColorField
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
      return str(self.name_ar)
    
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
    name_ar = models.CharField(verbose_name='الشهر عربي',max_length=50)
    name_en = models.CharField(verbose_name='الشهر إنجليزي',max_length=50)
    name_en_sort = models.CharField(verbose_name='إختصار الشهر إنجليزي',max_length=50)
    daysOfMonth = models.CharField(verbose_name='أيام الشهر',max_length=50)
    def __str__(self):
        return str(self.name_ar)

class CalendarWeek(models.Model):
    name_ar = models.CharField(verbose_name='اليوم عربي',max_length=50)
    name_en = models.CharField(verbose_name='اليوع إنجليزي',max_length=50)
    day_short_en = models.CharField(verbose_name=' اليوع إنجليزي مختصر',max_length=50)
    workDay = models.BooleanField(default=True, verbose_name='يوم عمل',max_length=50)
    def __str__(self):
        return str(self.name_ar)

class Gender(models.Model):
    name_ar = models.CharField(verbose_name='الجنس عربي',max_length=50)
    name_en = models.CharField(verbose_name='الجنس إنجليزي',max_length=50)
    def __str__(self):
        return str(self.name_ar)

class SocialStatus(models.Model):
    name_ar = models.CharField(verbose_name='الحالة الإجتماعية عربي',max_length=50)
    name_en = models.CharField(verbose_name='الحالة الإجتماعية إنجليزي',max_length=50)
    def __str__(self):
        return str(self.name_ar)

class WorkTrade(models.Model):
    name_ar = models.CharField(verbose_name='المهنة عربي',max_length=100)
    name_en = models.CharField(verbose_name='المهنة إنجليزي',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.name_ar)

class WorkSpecialty(models.Model):
    workTradeID = models.ForeignKey(WorkTrade, verbose_name='معرف المهنة',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    name_ar = models.CharField(verbose_name='التخصص عربي',max_length=100)
    name_en = models.CharField(verbose_name='التخصص إنجليزي',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.name_ar)

class JobTitle(models.Model):
    name_ar = models.CharField(verbose_name='المسمى الوظيفي عربي',max_length=100)
    name_en = models.CharField(verbose_name='المسمى الوظيفي إنجليزي',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.name_ar) 
       
class WorkingStatus(models.Model):
    name_ar = models.CharField(verbose_name='حالة العمل عربي',max_length=100)
    name_en = models.CharField(verbose_name='حالة العمل إنجليزي',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.name_ar)

class Bank(models.Model):
    name_ar = models.CharField(verbose_name='البنك عربي',max_length=100)
    name_en = models.CharField(verbose_name='البنك إنجليزي',max_length=100,blank=True, null=True)
    name_Symbol = models.CharField(verbose_name=' رمز البنك',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.name_ar)
    
class BranchBank(models.Model):
    bankID = models.ForeignKey(Bank, verbose_name='معرف البنك',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    name_ar = models.CharField(verbose_name='قرع البنك عربي',max_length=100)
    name_en = models.CharField(verbose_name='قرع البنك إنجليزي',max_length=100,blank=True, null=True)
    name_Symbol = models.CharField(verbose_name=' رمز البنك',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.name_ar)
    
class TypeAccBank(models.Model):
    name_ar = models.CharField(verbose_name='نوع الحساب عربي',max_length=100)
    name_en = models.CharField(verbose_name='نوع الحساب إنجليزي',max_length=100,blank=True, null=True)
    name_Symbol = models.CharField(verbose_name=' رمز البنك',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.name_ar)

class TypeID(models.Model):
    name_ar = models.CharField(verbose_name='نوع الهوية عربي',max_length=100)
    name_en = models.CharField(verbose_name='نوع الهوية إنجليزي',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.name_ar)

class TypeTransaction(models.Model):
  name_ar = models.CharField(verbose_name='نوع المعاملة عربي',max_length=100)
  name_en = models.CharField(verbose_name='نوع المعاملة إنجليزي',max_length=100,blank=True, null=True)
  def __str__(self):
    return str(self.name_ar)

class TargetGroup(models.Model):
  name_ar = models.CharField(verbose_name='الفئة المستهدفة عربي',max_length=100)
  name_en = models.CharField(verbose_name='الفئة المستهدفة إنجليزي',max_length=100,blank=True, null=True)
  def __str__(self):
    return str(self.name_ar)
  
class BusinessType(models.Model):
    name_ar = models.CharField(verbose_name='نوع العمل عربي',max_length=100)
    name_en = models.CharField(verbose_name='نوع العمل إنجليزي',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.name_ar)
    
class BusinessScope(models.Model):
    name_ar = models.CharField(verbose_name='مجال العمل عربي',max_length=100)
    name_en = models.CharField(verbose_name='مجال العمل إنجليزي',max_length=100,blank=True, null=True)
    logo = models.ImageField(verbose_name='صورة / لوقو', upload_to='logo_businessScope', null=True, blank=True)
    icone = models.CharField(verbose_name='أيقونة المجال',max_length=150,blank=True, null=True)
    
    def __str__(self):
        return str(self.name_ar)
    
class BusinessScopeSpecialization(models.Model):
    businessScopeID = models.ForeignKey(BusinessScope, verbose_name='معرف مجال العمل',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    name_ar = models.CharField(verbose_name='تخصص مجال العمل عربي',max_length=100)
    name_en = models.CharField(verbose_name='تخصص مجال العمل إنجليزي',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.name_ar)
    
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
        return str(self.name_ar)
    
class Size(models.Model):
    name = models.CharField(verbose_name='المقاس',max_length=100)
    name_gr = models.CharField(verbose_name='مقاس المملكة المتحدة',max_length=100,blank=True, null=True)
    name_fr = models.CharField(verbose_name='مقاس فرنسا',max_length=100,blank=True, null=True)
    name_us = models.CharField(verbose_name='مقاس الولايات المتحدة',max_length=100,blank=True, null=True)
    name_de = models.CharField(verbose_name='مقاس ألمانيا',max_length=100,blank=True, null=True)
    name_it = models.CharField(verbose_name='مقاس إيطاليا',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.name)

class Color(models.Model):
    name_ar = models.CharField(verbose_name='اللون عربي',max_length=100)
    name_en = models.CharField(verbose_name='اللون إنجليزي',max_length=100,blank=True, null=True)
    color = models.CharField(max_length=7, default="#FF0000", help_text="Enter the color in hex format, e.g., #FFFFFF")
    def __str__(self):
        return str(self.name_ar)

class Languages(models.Model):
  name_ar = models.CharField(verbose_name='اللغات عربي',max_length=100)
  name_en = models.CharField(verbose_name='اللغات إنجليزي',max_length=100,blank=True, null=True)
  def __str__(self):
    return str(self.name_ar)
 
class Skills(models.Model):
  name_ar = models.CharField(verbose_name='المهارات عربي',max_length=100)
  name_en = models.CharField(verbose_name='المهارات إنجليزي',max_length=100,blank=True, null=True)
  def __str__(self):
    return str(self.name_ar)
 
class TypeDelivery(models.Model):
  name_ar = models.CharField(verbose_name='طريقة التسليم عربي',max_length=100)
  name_en = models.CharField(verbose_name='طريقة التسليم إنجليزي',max_length=100,blank=True, null=True)
  def __str__(self):
    return str(self.name_ar)  
  
class TypePayment(models.Model):
  name_ar = models.CharField(verbose_name='طريقة الدفع عربي',max_length=100)
  name_en = models.CharField(verbose_name='طريقة الدفع إنجليزي',max_length=100,blank=True, null=True)
  def __str__(self):
    return str(self.name_ar)  
  
class TypeUnit(models.Model):
  name_ar = models.CharField(verbose_name='وحدة القياس عربي',max_length=100)
  name_en = models.CharField(verbose_name='وحدة القياس إنجليزي',max_length=100,blank=True, null=True)
  def __str__(self):
    return str(self.name_ar)  
  
class BasicInfo(models.Model):
    nationalityID = models.ForeignKey(Countries, verbose_name='الجنسية', related_name='nationalityID', default=1, on_delete=models.PROTECT, blank=True, null=True) 
    countryID = models.ForeignKey(Countries, verbose_name='بلد الإقامة', related_name='countryID', default=3, on_delete=models.PROTECT, blank=True, null=True) 
    regionID = models.ForeignKey(Region, verbose_name='المنطقة', on_delete=models.PROTECT, blank=True, null=True)
    stateID = models.ForeignKey(States, verbose_name='الولاية', on_delete=models.PROTECT, blank=True, null=True)
    cityID = models.ForeignKey(Cities, verbose_name='المدينة', related_name='basicInfo', on_delete=models.PROTECT, blank=True, null=True) 
    address = models.CharField(verbose_name='وصف العنوان',max_length=100, blank=True, null=True)
    google_maps_location = models.URLField(verbose_name='العنوان على خرائط قوقل', max_length=500, blank=True, null=True)
    latitude = models.DecimalField('خط العرض', max_digits=9, decimal_places=7, blank=True, null=True)
    longitude = models.DecimalField('خط الطول', max_digits=9, decimal_places=7, blank=True, null=True)
    phone = models.CharField(verbose_name='رقم الهاتف',max_length=100, blank=True, null=True)
    phoneOther = models.CharField(verbose_name='رقم هاتف آخر',max_length=100, blank=True, null=True)
    email = models.EmailField(verbose_name='البريد الإلكتروني',max_length=100, blank=True, null=True)
    website = models.CharField(verbose_name='الموقع الإلكتروني',max_length=100, blank=True, null=True)
    fax = models.CharField(verbose_name='فاكس',max_length=100, blank=True, null=True)
    POBox = models.CharField(verbose_name='صندوق بريد',max_length=100, blank=True, null=True)
    bankID = models.ForeignKey(Bank, verbose_name='البنك', on_delete=models.PROTECT, blank=True, null=True)
    branchBankID = models.ForeignKey(BranchBank, verbose_name='فرع البنك', on_delete=models.PROTECT, blank=True, null=True) 
    typeAccBankID = models.ForeignKey(TypeAccBank, verbose_name='نوع الحساب', on_delete=models.PROTECT, blank=True, null=True) 
    accountNumber = models.CharField(verbose_name='رقم الحساب المصرفي',max_length=100, blank=True, null=True)
    IBANNumber = models.CharField(verbose_name='رقم الآيبان المصرفي',max_length=100, blank=True, null=True)
    ownerAccount = models.CharField(verbose_name='إسم صاحب الحساب',max_length=100, blank=True, null=True)
    photo = models.ImageField(verbose_name='صورة / لوقو', upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    notes = models.TextField(verbose_name='ملاحظات', blank=True, null=True)
    attachments = models.FileField(verbose_name='مرفقات', upload_to='attach_dalil', blank=True, null=True)
    documentLink = models.CharField(verbose_name='رابط المستندات',max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True, verbose_name="نشط", blank=True, null=True)
    delete = models.BooleanField(default=False, verbose_name="حذف", blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_by', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='تاريخ الإنشاء',auto_now_add=True, blank=True, null=True)
    updated_by = models.ForeignKey(User, verbose_name='المُعدِل', related_name='updated_by', on_delete=models.PROTECT, blank=True, null=True)
    updated_at = models.DateTimeField(verbose_name='تاريخ التعديل', auto_now=True, blank=True, null=True)
    def __int__ (self):
        return self.id

class LegalPersons(models.Model):
    basicInfoID = models.OneToOneField(BasicInfo, on_delete=models.CASCADE, related_name='legalpersons', blank=True)
    name_ar = models.CharField(verbose_name='إسم الشركة عربي',max_length=100)
    acronym_ar = models.CharField(verbose_name='الإسم المختصر عربي',max_length=100, blank=True, null=True)
    name_en = models.CharField(verbose_name='إسم الشركة إنجليزي',max_length=100, blank=True, null=True)
    acronym_en = models.CharField(verbose_name='الإسم المختصر إنجليزي',max_length=100, blank=True, null=True)
    who_are_we = models.TextField(verbose_name='من نحن', max_length=250, blank=True, null=True)
    businessTypeID = models.ForeignKey(BusinessType, default=2, verbose_name='نوع الشركة',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    businessScopeID = models.ForeignKey(BusinessScope, verbose_name='مجال العمل', related_name="legalpersons", on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    businessScopeSpecializationID = models.ForeignKey(BusinessScopeSpecialization, verbose_name='تخصص مجال العمل',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    administrator = models.CharField(verbose_name='الموظف المسؤول',max_length=100, blank=True, null=True)
    phoneAdmin = models.CharField(verbose_name='هاتف الموظف المسؤول',max_length=100, blank=True, null=True)
    taxNumber = models.CharField(verbose_name='الرقم الضريبي',max_length=100, blank=True, null=True)
    def __str__(self):
        return str(self.name_ar )
    
class Persons(models.Model):
    basicInfoID = models.OneToOneField(BasicInfo, on_delete=models.CASCADE, related_name='persons', blank=True)
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
    socialStatusID = models.ForeignKey(SocialStatus, verbose_name='الحالة الإجتماعية', default=1, on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    typeID = models.ForeignKey(TypeID , verbose_name='نوع الهوية', default=1,on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    id_number = models.CharField(verbose_name='رقم الهوية',max_length=100, blank=True, null=True)
    id_ExpiredDate = models.DateField(verbose_name='تاريخ إنتهاء الهوية', blank=True, null=True)    
    workTradeID = models.ForeignKey(WorkTrade, verbose_name='المهنة', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    workSpecialtyID = models.ForeignKey(WorkSpecialty, verbose_name='التخصص', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    skillsID = models.ManyToManyField(Skills, verbose_name='المهارات', blank=True) #لن يتم حزف الصنف في حالة حذف الموظف
    languagesID = models.ManyToManyField(Languages, verbose_name='اللغات', blank=True) #لن يتم حزف الصنف في حالة حذف الموظف
    jobTitleID = models.ForeignKey(JobTitle, verbose_name='المسمى الوظيفي', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
   
    def __str__(self):
        return str(self.f_Name_ar)
    
    def fullName_ar(self):
        return f"{self.f_Name_ar} {self.s_Name_ar} {self.t_Name_ar} {self.fo_Name_ar}"
    
    def fullName_en(self):
        return f"{self.f_Name_en} {self.s_Name_en} {self.t_Name_en} {self.fo_Name_en}"
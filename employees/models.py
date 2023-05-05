from django.db import models
from datetime import date 

class Countries(models.Model):
    countryName_ar = models.CharField(verbose_name='إسم الدولة عربي',max_length=50)
    countryName_en = models.CharField(verbose_name='إسم الدولة إنجليزي',max_length=50)
    code = models.CharField(verbose_name='الرمز الموحد',max_length=50)
    callKey = models.CharField(verbose_name='مفتاح الإتصال',max_length=50)
    nationality = models.CharField(verbose_name='الجنسية',max_length=50, blank=True, null=True)
    def __str__(self):
        return str(self.countryName_ar)
    
class Region(models.Model):
    countryID = models.ForeignKey(Countries, default=13, verbose_name='معرف الدولة',on_delete=models.PROTECT) #لن يتم حزف الصنف في حالة حذف الموظف
    RegionName_ar = models.CharField(verbose_name='إسم المنطقة عربي',max_length=50, blank=True, null=True)
    RegionName_en = models.CharField(verbose_name='إسم المنطقة إنجليزي',max_length=50, blank=True, null=True)
    capitalRegion = models.CharField(verbose_name='عاصمة المنطقة',max_length=50, blank=True, null=True)
    imageRegion = models.ImageField(verbose_name=' صورة للمنطقة', upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    def __str__(self):
        return str(self.RegionName_ar)
    
class States(models.Model):
    regionID = models.ForeignKey(Region, verbose_name='معرف المنطقة',on_delete=models.PROTECT) #لن يتم حزف الصنف في حالة حذف الموظف
    stateName_ar = models.CharField(verbose_name='إسم الولاية عربي',max_length=50, blank=True, null=True)
    stateName_en = models.CharField(verbose_name='إسم الولاية إنجليزي',max_length=50, blank=True, null=True)
    population = models.IntegerField(verbose_name='عدد السكان', blank=True, null=True)
    def __str__(self):
        return str(self.stateName_ar)
    
class Cities(models.Model):
    stateID = models.ForeignKey(States, verbose_name='معرف الولاية',on_delete=models.PROTECT) #لن يتم حزف الصنف في حالة حذف الموظف
    cityName_ar = models.CharField(verbose_name='إسم المدينة عربي',max_length=50, blank=True, null=True)
    cityName_en = models.CharField(verbose_name='إسم المدينة إنجليزي',max_length=50, blank=True, null=True)
    population = models.IntegerField(verbose_name='عدد السكان', blank=True, null=True)
    def __str__(self):
        return str(self.cityName_ar)

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

class BusinessType(models.Model):
    type_ar = models.CharField(verbose_name='نوع العمل عربي',max_length=100)
    type_en = models.CharField(verbose_name='نوع العمل إنجليزي',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.type_ar)
    
class TypeID(models.Model):
    typeID_ar = models.CharField(verbose_name='نوع الهوية عربي',max_length=100)
    typeID_en = models.CharField(verbose_name='نوع الهوية إنجليزي',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.typeID_ar)

class Company(models.Model):
    compName_ar = models.CharField(verbose_name='الإسم عربي',max_length=100)
    compName_en = models.CharField(verbose_name='الإسم إنجليزي',max_length=100, blank=True, null=True)
    compAcronym_ar = models.CharField(verbose_name='الإسم المختصر عربي',max_length=100, blank=True, null=True)
    compAcronym_en = models.CharField(verbose_name='الإسم المختصر إنجليزي',max_length=100, blank=True, null=True)
    businessTypeID = models.ForeignKey(BusinessType, default=1, verbose_name='نوع الشركة',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    countryID = models.ForeignKey(Countries, default=13, verbose_name='الدولة',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    compbankID = models.ForeignKey(Bank, verbose_name='البنك',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    compPhone = models.CharField(verbose_name='رقم الهاتف',max_length=100, blank=True, null=True)
    compOwner = models.CharField(verbose_name='المالك',max_length=100, blank=True, null=True)
    ownerPhone = models.CharField(verbose_name='هاتف المالك',max_length=100, blank=True, null=True)
    compEmail = models.CharField(verbose_name='الإيميل',max_length=100, blank=True, null=True)
    compWebsite = models.CharField(verbose_name='الموقع الإلكتروني',max_length=100, blank=True, null=True)
    compAdministrator = models.CharField(verbose_name='المسؤول',max_length=100, blank=True, null=True)
    compFax = models.CharField(verbose_name='فاكس',max_length=100, blank=True, null=True)
    compPOBox = models.CharField(verbose_name='صندوق البري',max_length=100, blank=True, null=True)
    compRegionID = models.CharField(verbose_name='المنطقة',max_length=100, blank=True, null=True)
    compCommercialRegister = models.CharField(verbose_name='السجل التجاري',max_length=100, blank=True, null=True)
    compBusinessOfficeNo = models.CharField(verbose_name='مكتب العمل',max_length=100, blank=True, null=True)
    compWaselNo = models.CharField(verbose_name='واصل',max_length=100, blank=True, null=True)
    compZakatAndIncomeNo = models.CharField(verbose_name='الزكاء والضريبة',max_length=100, blank=True, null=True)
    compSocialSecurityNo = models.CharField(verbose_name='التأمينات الاجتماعية',max_length=100, blank=True, null=True)
    compChamberOfCommerceNo = models.CharField(verbose_name='الغرفة التجارية',max_length=100, blank=True, null=True)
    compMunicipalAffairsNo = models.CharField(verbose_name='شؤون البلدية',max_length=100, blank=True, null=True)
    compNotes = models.CharField(verbose_name='ملاحظات',max_length=100, blank=True, null=True)
    compBankAccount = models.CharField(verbose_name='رقم الحساب',max_length=100, blank=True, null=True)
    compDocumentLink = models.CharField(verbose_name='رابط المستندات',max_length=100, blank=True, null=True)
    who_i = models.TextField(max_length=250, blank=True, null=True)
    image = models.ImageField(verbose_name='شعار الشركة', upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    active = models.BooleanField(default=False, verbose_name="نشط", blank=True, null=True)
    def __str__(self):
        return str(self.compName_ar)

class Project(models.Model):
    proName_ar = models.CharField(verbose_name='المشروع عربي',max_length=100)
    proName_er = models.CharField(verbose_name='المشروع إنجليزي',max_length=100)
    directSupervisor = models.CharField(verbose_name='المشرف المباشر',max_length=100)
    phoneDirectSupervisor = models.CharField(verbose_name='جوال المشرف المباشر',max_length=100)
    countryID = models.ForeignKey(Countries, verbose_name='الدولة',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    regionID = models.ForeignKey(Region, verbose_name='المنطقة',on_delete=models.PROTECT, blank=True, null=True)
    def __str__(self):
        return str(self.proName_ar)
    
class SubProject(models.Model):
    projectID = models.ForeignKey(Project, default=1, verbose_name='المشروع الرئيس', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    noPro = models.CharField(verbose_name='رقم المشروع الفرعي ',default="1", max_length=100)
    subProName_ar = models.CharField(verbose_name='مشروع فرعي عربي',max_length=100)
    subProName_er = models.CharField(verbose_name='مشروع فرعي إنجليزي',max_length=100)
    def __str__(self):
        return str(self.noPro)

class Sponser(models.Model):
    sponsName = models.CharField(verbose_name='إسم الكفيل', max_length=100)
    companyID = models.ForeignKey(Company, verbose_name='الشركة',on_delete=models.CASCADE) #لن يتم حزف الصنف في حالة حذف الموظف
    def __str__(self):
        return str(self.sponsName)

class EmpInfo(models.Model):
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
    companyID = models.ForeignKey(Company, verbose_name='الشركة', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    sponserID = models.ForeignKey(Sponser, verbose_name='الكفيل', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    workTradeID = models.ForeignKey(WorkTrade, verbose_name='المهنة', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    workSpecialtyID = models.ForeignKey(WorkSpecialty, verbose_name='التخصص', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    workingStatusID = models.ForeignKey(WorkingStatus, verbose_name='حالة العمل', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    passportNumber = models.CharField(verbose_name='رقم الجواز',max_length=100, blank=True, null=True)
    visaNumber = models.CharField(verbose_name='رقم التأشيرة',max_length=100, blank=True, null=True)
    passportExpiryDate = models.DateField(verbose_name='تاريخ إنتهاء الجواز', blank=True, null=True)
    medicalInsuranceExpirDate = models.DateField(verbose_name='تاريخ إنتهاء التأمين الطبي', blank=True, null=True)
    borderNumber = models.CharField(verbose_name='رقم الحدود',max_length=100, blank=True, null=True)
    enteryDate = models.DateField(verbose_name='تاريخ الدخول', blank=True, null=True)
    businessOfficeNumber = models.CharField(verbose_name='رقم مكتب العمل',max_length=100, blank=True, null=True)
    mobileNumber = models.CharField(verbose_name='رقم الجوال',max_length=100, blank=True, null=True)
    mobileNumberAnother = models.CharField(verbose_name='رقم جوال آخر',max_length=100, blank=True, null=True)
    # countreyID = models.ForeignKey(Countries, verbose_name='الدولة', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
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
    iqamaNumber = models.CharField(verbose_name='رقم الإقامة',max_length=100, blank=True, null=True)
    iqamaExpiredDate = models.DateField(verbose_name='تاريخ إنتهاء الإقامة', blank=True, null=True)
    salaryInsurance = models.DecimalField(verbose_name="راتب التأمينات", default=400, decimal_places=2, max_digits=10, blank=True, null=True)
    contractSalary = models.DecimalField(verbose_name="راتب العق", default=1200, decimal_places=2, max_digits=10, blank=True, null=True)
    fixedExtra = models.DecimalField(verbose_name="إضافي ثابت", default=0, decimal_places=2, max_digits=10, blank=True, null=True)
    iqamaReleaseDate = models.DateField(verbose_name='تاريخ إصدار الإقامة', blank=True, null=True)
    workStartingDate = models.DateField(verbose_name='تاريخ بداية العمل', blank=True, null=True)
    endDateOfService = models.DateField(verbose_name='تاريخ نهاية العمل', blank=True, null=True)
    emp_Photo = models.ImageField(verbose_name='صورة شخصية', upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    coronaCheck = models.BooleanField(default=True, verbose_name="فحص كرونا", blank=True, null=True)
    tawaklna = models.BooleanField(default=True, verbose_name="توكلنا", blank=True, null=True)
    sahaty = models.BooleanField(default=True, verbose_name="صحتي", blank=True, null=True)
    medicalInsurance = models.BooleanField(default=True, verbose_name="تأمين طبي", blank=True, null=True)
    muqeemCopy = models.BooleanField(default=True, verbose_name="نسخة مقيم", blank=True, null=True)
    notes = models.TextField(verbose_name='ملاحظات', blank=True, null=True)
    documentLink = models.CharField(verbose_name='رابط المستندات',max_length=100, blank=True, null=True)
    def __str__(self):
        return str(self.f_Name_ar)

class ProjectRotation(models.Model):
    empID = models.ForeignKey(EmpInfo, verbose_name='العامل', on_delete=models.PROTECT) #لن يتم حزف الصنف في حالة حذف الموظف
    projectID = models.ForeignKey(Project, verbose_name='المشروع', on_delete=models.PROTECT) #لن يتم حزف الصنف في حالة حذف الموظف
    subProjectID = models.ForeignKey(SubProject, verbose_name='مشروع فرعي', on_delete=models.PROTECT) #لن يتم حزف الصنف في حالة حذف الموظف
    yearID = models.ForeignKey(CalendarYears, verbose_name='العام', on_delete=models.PROTECT) #لن يتم حزف الصنف في حالة حذف الموظف
    monthID = models.ForeignKey(CalendarMonths, verbose_name='الشهر', on_delete=models.PROTECT) #لن يتم حزف الصنف في حالة حذف الموظف
    dateEntry = models.DateField(verbose_name='تاريخ الدخول')
    dateExit = models.DateField(verbose_name='تاريخ الخروج')
    workHours = models.IntegerField(verbose_name='ساعات العمل', default=0)
    ExtraHours = models.IntegerField(verbose_name='الساعات الإضافية', default=0)
    totalHours = models.IntegerField(verbose_name='إجمالي الساعات', default=0)
    absentDays = models.IntegerField(verbose_name='أيام الغياب', default=0)
    sellingPrice = models.IntegerField(verbose_name='سعر بيع الساعة', default=0)
    purchasingPrice = models.IntegerField(verbose_name='سعر شراء الساعة', default=0)
    otherAllowances = models.IntegerField(verbose_name='بدلات أخرى', default=0)
    notesOtherAllowances = models.TextField(verbose_name='وصف البدلات', default=0)
    otherDiscounts = models.IntegerField(verbose_name='خصومات أخرى', default=0)
    notesOtherDiscounts = models.TextField(verbose_name='وصف الخصومات', default=0)
    def __str__(self):
        return self.projectID # تعويض إسم الجدول في الداتا بيس بإسم الكلاس
    class Meta:
        verbose_name = 'دوران المشروع' # تغيير إسم الجدول
        ordering = ['projectID'] # ترتيب العناصر تنازلي
        ordering = ['-projectID'] # ترتيب العتاصر تصاعدي


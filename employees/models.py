from django.db import models
from basicinfo.models import *
from companys.models import Company
# from profiles.models import UserProfile

class Employee(models.Model):
    companyID = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True)
    sequence = models.PositiveIntegerField(editable=False)  # الحقل التسلسلي
    personID = models.OneToOneField(Persons, on_delete=models.CASCADE, blank=True)
    workStartDate = models.DateField(verbose_name='تاريخ بداية العمل', blank=True, null=True)
    contractSalary = models.DecimalField(verbose_name="راتب العقد", default=1200, decimal_places=2, max_digits=10, blank=True, null=True)
    fixedExtra = models.DecimalField(verbose_name="إضافي ثابت", default=0, decimal_places=2, max_digits=10, blank=True, null=True)
    workingStatusID = models.ForeignKey(WorkingStatus, verbose_name='حالة العمل', default=1, on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    workEndDate = models.DateField(verbose_name='تاريخ نهاية العمل', blank=True, null=True)

    def __str__(self):
        return str(self.personID)

class ProjectRotation(models.Model):
    empID = models.ForeignKey(Employee, verbose_name='العامل', on_delete=models.PROTECT) #لن يتم حزف الصنف في حالة حذف الموظف
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
    # class Meta:
    #     verbose_name = 'دوران المشروع' # تغيير إسم الجدول
    #     ordering = ['projectID'] # ترتيب العناصر تنازلي
    #     ordering = ['-projectID'] # ترتيب العتاصر تصاعدي


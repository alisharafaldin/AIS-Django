from django.db import models
from basicinfo.models import Cities, States, Region, Countries
from companys.models import Company
from employees.models import Employee
from django.contrib.auth.models import User

# Create your models here.

class Inventory (models.Model):
    companyID = models.ForeignKey(Company, related_name='inventorys_company_set', on_delete=models.PROTECT,blank=True)
    sequence = models.PositiveIntegerField(editable=False)  # الحقل التسلسلي
    name_ar = models.CharField(verbose_name='المخزن عربي', max_length=100)
    name_en = models.CharField(verbose_name='المخزن إنجليزي', max_length=100, blank=True, null=True)
    countryID = models.ForeignKey(Countries, verbose_name='الدولة', related_name='inventorys_country_set', default=1, on_delete=models.PROTECT, blank=True, null=True) 
    regionID = models.ForeignKey(Region, verbose_name='المنطقة', related_name='inventorys_region_set', default=1, on_delete=models.PROTECT, blank=True, null=True)
    stateID = models.ForeignKey(States, verbose_name='الولاية', related_name='inventorys_state_set', default=1, on_delete=models.PROTECT, blank=True, null=True)
    cityID = models.ForeignKey(Cities, verbose_name='المدينة',  related_name='inventorys_city_set', default=1, on_delete=models.PROTECT, blank=True, null=True) 
    administratorID = models.ForeignKey(Employee, verbose_name='الموظف المسؤول', related_name='inventorys_administrator_set', on_delete=models.PROTECT, blank=True, null=True)
    address = models.CharField(verbose_name='وصف العنوان', max_length=100, blank=True, null=True)
    google_maps_location = models.URLField(verbose_name='العنوان على خرائط قوقل', max_length=500, blank=True, null=True)
    phoneAdmin = models.CharField(verbose_name='هاتف الموظف المسؤول', max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(User, verbose_name='المنشئ', related_name='created_by_inventory', on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='تاريخ الإنشاء',auto_now_add=True, blank=True, null=True)
    updated_by = models.ForeignKey(User, verbose_name='المُعدِل', related_name='updated_by_inventory', on_delete=models.PROTECT, blank=True, null=True)
    updated_at = models.DateTimeField(verbose_name='تاريخ التعديل', auto_now=True, blank=True, null=True)
    notes = models.TextField(verbose_name='ملاحظات', blank=True, null=True)
    available = models.BooleanField(verbose_name='متاح', default=True, blank=True, null=True)
    def __str__(self):
        return str(self.name_ar)
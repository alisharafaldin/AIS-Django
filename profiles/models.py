from django.db import models
from django.contrib.auth.models import User
from basicinfo.models import Countries, Gender


# Create your models here.

class UserProfile(models.Model):
    userID = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user', blank=True)
    nationalityID = models.ForeignKey(Countries, verbose_name='الجنسية', on_delete=models.PROTECT, blank=True, null=True) 
    countryID = models.ForeignKey(Countries, verbose_name='بلد الإقامة', related_name='user_countryID', default=2, on_delete=models.PROTECT, blank=True, null=True)
    dateOfBirth = models.DateField(verbose_name='تاريخ الميلاد', blank=True, null=True)
    genderID = models.ForeignKey(Gender, verbose_name='الجنس', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    phone = models.CharField(verbose_name='رقم الهاتف',max_length=100, blank=True, null=True)
    phoneOther = models.CharField(verbose_name='رقم هاتف آخر',max_length=100, blank=True, null=True)
    photo = models.ImageField(verbose_name='صورة شخصية', upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    terms = models.BooleanField(default=False, verbose_name="الشروط", blank=True, null=True)
    active = models.BooleanField(default=True, verbose_name="نشط", blank=True, null=True)
   
    def __str__(self):
        return self.userID.username 
        
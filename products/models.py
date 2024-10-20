from django.db import models
from basicinfo.models import Color, Size, TargetGroup, TypeUnit
from django.contrib.auth.models import User
from companys.models import Company

# Create your models here.

class ItemType(models.Model):
    name_ar = models.CharField(verbose_name='نوع الصنف عربي', max_length=100, blank=True, null=True)
    name_en = models.CharField(verbose_name='نوع الصنف إنجليزي', max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name_ar

class ItemGrop(models.Model):
    companyID = models.ForeignKey(Company, on_delete=models.PROTECT,blank=True)
    sequence = models.PositiveIntegerField(editable=False)  # الحقل التسلسلي
    itemTypeID = models.ForeignKey(ItemType, verbose_name='معرف نوع الصنف', on_delete=models.PROTECT, related_name='category_type', blank=True, null=True)
    name_ar = models.CharField(verbose_name='مجموعة الصنف عربي', max_length=100, blank=True, null=True)
    name_en = models.CharField(verbose_name='مجموعة الصنف إنجليزي', max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name_ar
    
class Items(models.Model):
    companyID = models.ForeignKey(Company, on_delete=models.PROTECT,blank=True)
    sequence = models.PositiveIntegerField(editable=False)  # الحقل التسلسلي
    name_ar = models.CharField(verbose_name='الصنف عربي', max_length=100, blank=True, null=True)
    name_en = models.CharField(verbose_name='الصنف إنجليزي', max_length=100, blank=True, null=True)
    itemGropID = models.ForeignKey(ItemGrop, verbose_name='معرف مجموعة الصنف', default=1, on_delete=models.PROTECT, related_name='category', blank=True, null=True)
    typeUnitID = models.ForeignKey(TypeUnit, verbose_name='وحدة القياس', default=1, on_delete=models.PROTECT, related_name='category', blank=True, null=True)
    targetGroupID = models.ForeignKey(TargetGroup,verbose_name='الفئة المستهدفة', on_delete=models.PROTECT, default=1, blank=True, null=True)
    itemCode = models.TextField(verbose_name='كود الصنف', blank=True, null=True)
    purchasingPrice = models.DecimalField(verbose_name='سعر الشراء', default=0, max_digits=10, decimal_places=2, blank=True, null=True)
    sellingPrice = models.DecimalField(verbose_name='سعر البيع', default=0, max_digits=10, decimal_places=2, blank=True, null=True)
    colorID = models.ForeignKey(Color,verbose_name='اللون',  on_delete=models.PROTECT, default=1, related_name='the_color', blank=True, null=True)
    sizeID = models.ForeignKey(Size,verbose_name='المقاس',  on_delete=models.PROTECT, default=1, related_name='size', blank=True, null=True)
    description = models.TextField(verbose_name='وصف الصنف', blank=True, null=True)
    photo = models.ImageField(verbose_name='صورة للصنف', upload_to='photo_item', blank=True, null=True)
    created_by = models.ForeignKey(User, verbose_name='المنشئ', related_name='created_by_itemsDetails', on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='تاريخ الإنشاء',auto_now_add=True, blank=True, null=True)
    updated_by = models.ForeignKey(User, verbose_name='المُعدِل', related_name='updated_by_itemsDetails', on_delete=models.PROTECT, blank=True, null=True)
    updated_at = models.DateTimeField(verbose_name='تاريخ التعديل', auto_now=True, blank=True, null=True)
    available = models.BooleanField(verbose_name='متاح', default=True, blank=True, null=True)
    notes = models.TextField(verbose_name='ملاحظات', blank=True, null=True)
    def __str__(self):
        return self.name_ar
    
    class Meta:
    #ترتيب العناصر حسب الآي دي
        ordering = ['name_ar']

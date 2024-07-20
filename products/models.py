from django.db import models
from datetime import datetime
from basicinfo.models import Color, Size
# Create your models here.

class CategoryType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Category(models.Model):
    categoryTypeID = models.ForeignKey(CategoryType, on_delete=models.CASCADE, related_name='category_type', blank=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Items(models.Model):
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', blank=True)
    purchasingPrice = models.DecimalField(verbose_name='سعر الشراء', default=0, max_digits=6, decimal_places=2)
    sellingPrice = models.DecimalField(verbose_name='سعر البيع', default=0, max_digits=6, decimal_places=2)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class ItemsDetails(models.Model):
    itemID = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name='item', blank=True, null=True)
    colorID = models.ForeignKey(Color, on_delete=models.CASCADE, default=1, related_name='the_color', blank=True, null=True)
    sizeID = models.ForeignKey(Size, on_delete=models.CASCADE, default=1, related_name='size', blank=True, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True, null=True)
    def __str__(self):
        return self.itemID



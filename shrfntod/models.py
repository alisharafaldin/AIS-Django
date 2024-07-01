from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager


# Create your models here.
class Album(models.Model):
  name = models.CharField(max_length=100)
  def __str__(self):
    return  self.name

class Posts(models.Model):
  date = models.DateField(verbose_name='تاريخ البوست', default=timezone.now() , blank=True, null=True)
  dateHijri = models.CharField(max_length=100)
  title = models.CharField(verbose_name='عنوان البوست', max_length=500)
  albumID = models.ForeignKey(Album , verbose_name='الألبوم', default=1, on_delete=models.CASCADE)
  content = models.TextField(verbose_name='متحوى البوست')
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  link = models.CharField(verbose_name='رابط البوست', max_length=500)
  tags = TaggableManager()
  created_py = models.ForeignKey(User, verbose_name='المُنشئ', related_name='created_py', on_delete=models.CASCADE)
  created_dt = models.DateTimeField(verbose_name='تاريخ الإنشاء',auto_now_add=True)
  updated_py = models.ForeignKey(User, verbose_name='المُعدل', related_name='updated_py', on_delete=models.CASCADE, blank=True, null=True)
  updated_dt = models.DateTimeField(verbose_name='تاريخ التعديل',auto_now_add=True)
  def __str__(self):
    return  self.title
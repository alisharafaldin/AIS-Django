from django.db.models.signals import pre_save, post_delete
from django.db import models
from django.dispatch import receiver
from .models import  ItemGrop, ItemDetails

@receiver(pre_save, sender=ItemGrop)
def set_itemGrop_sequence(sender, instance, **kwargs):
    if instance.sequence is None:
        # العثور على أكبر قيمة موجودة في `sequence` بالنسبة للشركة المعنية
        last_itemGrop = ItemGrop.objects.filter(companyID=instance.companyID).order_by('-sequence').first()
        if last_itemGrop:
            instance.sequence = last_itemGrop.sequence + 1
        else:
            instance.sequence = 1

@receiver(pre_save, sender=ItemDetails)
def set_itemDetails_sequence(sender, instance, **kwargs):
    if instance.sequence is None:
        # العثور على أكبر قيمة موجودة في `sequence` بالنسبة للشركة المعنية
        last_itemDetails = ItemDetails.objects.filter(companyID=instance.companyID).order_by('-sequence').first()
        if last_itemDetails:
            instance.sequence = last_itemDetails.sequence + 1
        else:
            instance.sequence = 1

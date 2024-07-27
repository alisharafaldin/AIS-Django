from django.db.models.signals import pre_save, post_delete
from django.db import models
from django.dispatch import receiver
from .models import Qayd

@receiver(pre_save, sender=Qayd)
def set_qayd_sequence(sender, instance, **kwargs):
    if instance.sequence is None:
        # العثور على أكبر قيمة موجودة في `sequence` بالنسبة للشركة المعنية
        last_qayd = Qayd.objects.filter(companyID=instance.companyID).order_by('-sequence').first()
        if last_qayd:
            instance.sequence = last_qayd.sequence + 1
        else:
            instance.sequence = 1

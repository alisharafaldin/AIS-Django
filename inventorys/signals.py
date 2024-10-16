import os
from django.db.models.signals import pre_save, post_delete
from django.db.models import Max
from django.dispatch import receiver
from .models import Inventory

# إضافة تسلسل بطريقة أكثر تنظيماً
def set_model_sequence(instance, field_name):
    """تعيين التسلسل للحقول الخاصة بالنموذج."""
    # الحصول على أقصى قيمة موجودة للـ sequence في الشركة المحددة
    max_sequence = instance.__class__.objects.filter(companyID=instance.companyID).aggregate(max_sequence=Max(field_name))['max_sequence']
    if max_sequence is None:
        instance.sequence = 1  # تعيين القيمة الافتراضية إذا لم تكن هناك قيم موجودة
    else:
        instance.sequence = max_sequence + 1

@receiver(pre_save, sender=Inventory)
def set_inventory_sequence(sender, instance, **kwargs):
    """تعيين تسلسل للمخازن."""
    if instance.pk is None:  # إذا كان هذا سجل جديد
        set_model_sequence(instance, 'sequence')

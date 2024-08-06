from django.db.models.signals import pre_save
from django.db.models import Max
from django.dispatch import receiver
from .models import Employee

@receiver(pre_save, sender=Employee)
def set_sequence(sender, instance, **kwargs):
    if instance.pk is None:  # إذا كان هذا سجل جديد
        # الحصول على أقصى قيمة موجودة للـ sequence في الشركة المحددة
        max_sequence = sender.objects.filter(companyID=instance.companyID).aggregate(Max('sequence'))['sequence__max']
        if max_sequence is None:
            instance.sequence = 1  # تعيين القيمة الافتراضية إذا لم تكن هناك قيم موجودة
        else:
            instance.sequence = max_sequence + 1

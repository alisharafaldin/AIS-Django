from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Qayd

@receiver(pre_save, sender=Qayd)
def set_qayd_sequence(sender, instance, **kwargs):
    if instance.sequence is None:
        last_qayd = Qayd.objects.filter(companyID=instance.companyID).order_by('sequence').last()
        if last_qayd:
            instance.sequence = last_qayd.sequence + 1
        else:
            instance.sequence = 1

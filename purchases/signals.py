import os
from django.db.models import Max
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete
from .models import Suppliers, Inventory, InvoicesPurchasesHead

@receiver(pre_save, sender=Suppliers)
def set_sequence(sender, instance, **kwargs):
    if instance.pk is None:  # إذا كان هذا سجل جديد
        # الحصول على أقصى قيمة موجودة للـ sequence في الشركة المحددة
        max_sequence = sender.objects.filter(companyID=instance.companyID).aggregate(Max('sequence'))['sequence__max']
        if max_sequence is None:
            instance.sequence = 1  # تعيين القيمة الافتراضية إذا لم تكن هناك قيم موجودة
        else:
            instance.sequence = max_sequence + 1

@receiver(pre_save, sender=Inventory)
def set_sequence(sender, instance, **kwargs):
    if instance.pk is None:  # إذا كان هذا سجل جديد
        # الحصول على أقصى قيمة موجودة للـ sequence في الشركة المحددة
        max_sequence = sender.objects.filter(companyID=instance.companyID).aggregate(Max('sequence'))['sequence__max']
        if max_sequence is None:
            instance.sequence = 1  # تعيين القيمة الافتراضية إذا لم تكن هناك قيم موجودة
        else:
            instance.sequence = max_sequence + 1

@receiver(pre_save, sender=InvoicesPurchasesHead)
def set_sequence(sender, instance, **kwargs):
    if instance.pk is None:  # إذا كان هذا سجل جديد
        # الحصول على أقصى قيمة موجودة للـ sequence في الشركة المحددة
        max_sequence = sender.objects.filter(companyID=instance.companyID).aggregate(Max('sequence'))['sequence__max']
        if max_sequence is None:
            instance.sequence = 1  # تعيين القيمة الافتراضية إذا لم تكن هناك قيم موجودة
        else:
            instance.sequence = max_sequence + 1



# -------------- دوال إذالة المرفقات من المشروع في حال التغيير أو الحذف -------------

# دالة عامة لحذف الملفات
def delete_old_file(instance, field_name):
    """حذف الملف إذا كان موجودًا وتفريغه أو تغييره"""
    # الحصول على اسم الحقل الديناميكيًا
    file_field = getattr(instance, field_name)
    if file_field and hasattr(file_field, 'path') and os.path.isfile(file_field.path):
        os.remove(file_field.path)

# الإشارة لحذف الملف عند حذف الكائن
def setup_delete_file_signal(model, field_name):
    @receiver(post_delete, sender=model)
    def delete_file_on_delete(sender, instance, **kwargs):
        """حذف الملف من النظام عند حذف الكائن"""
        delete_old_file(instance, field_name)

# الإشارة لحذف الملف عند تحديث أو تفريغ الحقل
def setup_change_file_signal(model, field_name):
    @receiver(pre_save, sender=model)
    def delete_file_on_change(sender, instance, **kwargs):
        """حذف الملف القديم عند تغييره أو تفريغه"""
        if not instance.pk:
            return False
        try:
            old_instance = sender.objects.get(pk=instance.pk)
        except sender.DoesNotExist:
            return False

        old_file = getattr(old_instance, field_name)
        new_file = getattr(instance, field_name)
        if old_file and old_file != new_file:
            delete_old_file(old_instance, field_name)

# تطبيق الإشارات على نموذج InvoicesPurchasesHead
setup_delete_file_signal(InvoicesPurchasesHead, 'attachments')
setup_change_file_signal(InvoicesPurchasesHead, 'attachments')



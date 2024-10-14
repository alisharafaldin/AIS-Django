import os
from django.db.models.signals import pre_save, post_delete
from django.db.models import Max
from django.dispatch import receiver
from .models import Customers, Inventory, InvoicesSalesHead

# # إضافة تسلسل للعملاء خاص بكل شركة
# @receiver(pre_save, sender=Customers)
# def set_sequence(sender, instance, **kwargs):
#     if instance.pk is None:  # إذا كان هذا سجل جديد
#         # الحصول على أقصى قيمة موجودة للـ sequence في الشركة المحددة
#         max_sequence = sender.objects.filter(companyID=instance.companyID).aggregate(Max('sequence'))['sequence__max']
#         if max_sequence is None:
#             instance.sequence = 1  # تعيين القيمة الافتراضية إذا لم تكن هناك قيم موجودة
#         else:
#             instance.sequence = max_sequence + 1

# # إضافة تسلسل للمخازن خاص
# @receiver(pre_save, sender=Inventory)
# def set_sequence(sender, instance, **kwargs):
#     if instance.pk is None:  # إذا كان هذا سجل جديد
#         # الحصول على أقصى قيمة موجودة للـ sequence في الشركة المحددة
#         max_sequence = sender.objects.filter(companyID=instance.companyID).aggregate(Max('sequence'))['sequence__max']
#         if max_sequence is None:
#             instance.sequence = 1  # تعيين القيمة الافتراضية إذا لم تكن هناك قيم موجودة
#         else:
#             instance.sequence = max_sequence + 1

# @receiver(pre_save, sender=InvoicesSalesHead)
# def set_sequence(sender, instance, **kwargs):
#     if instance.pk is None:  # إذا كان هذا سجل جديد
#         # الحصول على أقصى قيمة موجودة للـ sequence في الشركة المحددة
#         max_sequence = sender.objects.filter(companyID=instance.companyID).aggregate(Max('sequence'))['sequence__max']
#         if max_sequence is None:
#             instance.sequence = 1  # تعيين القيمة الافتراضية إذا لم تكن هناك قيم موجودة
#         else:
#             instance.sequence = max_sequence + 1


# إضافة تسلسل بطريقة أكثر تنظيماً
def set_model_sequence(instance, field_name):
    """تعيين التسلسل للحقول الخاصة بالنموذج."""
    # الحصول على أقصى قيمة موجودة للـ sequence في الشركة المحددة
    max_sequence = instance.__class__.objects.filter(companyID=instance.companyID).aggregate(max_sequence=Max(field_name))['max_sequence']
    if max_sequence is None:
        instance.sequence = 1  # تعيين القيمة الافتراضية إذا لم تكن هناك قيم موجودة
    else:
        instance.sequence = max_sequence + 1

@receiver(pre_save, sender=Customers)
def set_customers_sequence(sender, instance, **kwargs):
    """تعيين تسلسل للعملاء."""
    if instance.pk is None:  # إذا كان هذا سجل جديد
        set_model_sequence(instance, 'sequence')

@receiver(pre_save, sender=Inventory)
def set_inventory_sequence(sender, instance, **kwargs):
    """تعيين تسلسل للمخازن."""
    if instance.pk is None:  # إذا كان هذا سجل جديد
        set_model_sequence(instance, 'sequence')

@receiver(pre_save, sender=InvoicesSalesHead)
def set_invoices_sales_head_sequence(sender, instance, **kwargs):
    """تعيين تسلسل لفواتير المبيعات."""
    if instance.pk is None:  # إذا كان هذا سجل جديد
        set_model_sequence(instance, 'sequence')


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

# تطبيق الإشارات على نموذج InvoicesSalesHead
setup_delete_file_signal(InvoicesSalesHead, 'attachments')
setup_change_file_signal(InvoicesSalesHead, 'attachments')


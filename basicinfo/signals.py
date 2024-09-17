import os
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Cities, BasicInfo

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


# تطبيق الإشارات على نموذج Cities
setup_delete_file_signal(Cities, 'logo')
setup_change_file_signal(Cities, 'logo')

# تطبيق الإشارات على نموذج BasicInfo
setup_delete_file_signal(BasicInfo, 'photo')
setup_change_file_signal(BasicInfo, 'photo')

# تطبيق الإشارات على نموذج BasicInfo
setup_delete_file_signal(BasicInfo, 'attachments')
setup_change_file_signal(BasicInfo, 'attachments')


# طريقة أخرى مختصرة لكتابة نفس الدول أعلاه لتطبيق الإشارات للحذف وتغيير الملفات على أي نموذج وحقل
# def setup_file_signals(model, field_name):
#     @receiver(post_delete, sender=model)
#     def delete_file_on_model_delete(sender, instance, **kwargs):
#         """حذف الملف عند حذف الكائن."""
#         field = getattr(instance, field_name)
#         if field and os.path.isfile(field.path):
#             os.remove(field.path)

#     @receiver(pre_save, sender=model)
#     def delete_old_file_on_change(sender, instance, **kwargs):
#         """حذف الملف القديم عند تغيير الملف."""
#         if not instance.pk:
#             return  # لا حاجة لفعل شيء عند إنشاء الكائن الجديد
#         try:
#             old_file = getattr(sender.objects.get(pk=instance.pk), field_name)
#         except sender.DoesNotExist:
#             return
#         new_file = getattr(instance, field_name)
#         if old_file and old_file != new_file:
#             if os.path.isfile(old_file.path):
#                 os.remove(old_file.path)

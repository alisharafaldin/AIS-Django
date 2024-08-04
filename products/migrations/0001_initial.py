# Generated by Django 4.2.3 on 2024-08-03 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companys', '0001_initial'),
        ('basicinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ar', models.CharField(blank=True, max_length=100, null=True, verbose_name='نوع الصنف عربي')),
                ('name_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='نوع الصنف إنجليزي')),
            ],
        ),
        migrations.CreateModel(
            name='ItemGrop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveIntegerField(editable=False)),
                ('name_ar', models.CharField(blank=True, max_length=100, null=True, verbose_name='مجموعة الصنف عربي')),
                ('name_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='مجموعة الصنف إنجليزي')),
                ('companyID', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='companys.company')),
                ('itemTypeID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='category_type', to='products.itemtype', verbose_name='معرف نوع الصنف')),
            ],
        ),
        migrations.CreateModel(
            name='ItemDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveIntegerField(editable=False)),
                ('purchasingPrice', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='سعر الشراء')),
                ('sellingPrice', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='سعر البيع')),
                ('name_ar', models.CharField(blank=True, max_length=100, null=True, verbose_name='الصنف عربي')),
                ('name_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='الصنف إنجليزي')),
                ('description', models.TextField(blank=True, null=True, verbose_name='وصف الصنف')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='صورة للصنف')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الإنشاء')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='تاريخ التعديل')),
                ('available', models.BooleanField(blank=True, default=True, null=True, verbose_name='متاح')),
                ('colorID', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='the_color', to='basicinfo.color', verbose_name='اللون')),
                ('companyID', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='companys.company')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_by_itemsDetails', to=settings.AUTH_USER_MODEL, verbose_name='المنشئ')),
                ('itemGropID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='category', to='products.itemgrop', verbose_name='معرف مجموعة الصنف')),
                ('sizeID', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='size', to='basicinfo.size', verbose_name='المقاس')),
                ('targetGroupID', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.targetgroup', verbose_name='الفئة المستهدفة')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_by_itemsDetails', to=settings.AUTH_USER_MODEL, verbose_name='المُعدِل')),
            ],
        ),
    ]

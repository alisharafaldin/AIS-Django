# Generated by Django 4.2.3 on 2024-10-15 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basicinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='رقم الهاتف')),
                ('phoneOther', models.CharField(blank=True, max_length=100, null=True, verbose_name='رقم هاتف آخر')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='صورة شخصية')),
                ('terms', models.BooleanField(blank=True, default=False, null=True, verbose_name='الشروط')),
                ('active', models.BooleanField(blank=True, default=True, null=True, verbose_name='نشط')),
                ('nationalityID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.countries', verbose_name='الجنسية')),
                ('userID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

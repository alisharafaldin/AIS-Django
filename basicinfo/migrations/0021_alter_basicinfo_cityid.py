# Generated by Django 4.2.3 on 2024-09-10 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0020_alter_basicinfo_attachments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinfo',
            name='cityID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='city_basicInfo', to='basicinfo.cities', verbose_name='المدينة'),
        ),
    ]
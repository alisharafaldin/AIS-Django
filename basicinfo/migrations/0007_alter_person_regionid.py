# Generated by Django 4.2.3 on 2023-08-18 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0006_person_regionid_alter_region_countryid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='regionID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.region', verbose_name='المنطقة'),
        ),
    ]
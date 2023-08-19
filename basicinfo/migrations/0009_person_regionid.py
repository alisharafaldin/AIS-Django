# Generated by Django 4.2.3 on 2023-08-18 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0008_remove_person_regionid'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='regionID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.region', verbose_name='المنطقة'),
        ),
    ]

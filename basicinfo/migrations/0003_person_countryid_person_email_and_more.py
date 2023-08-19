# Generated by Django 4.2.3 on 2023-08-18 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0002_currency_workingstatus_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='countryID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='countryID', to='basicinfo.countries', verbose_name='الدولة'),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='البريد الإلكتروني'),
        ),
        migrations.AlterField(
            model_name='person',
            name='nationalityID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='nationalityID', to='basicinfo.countries', verbose_name='الجنسية'),
        ),
    ]

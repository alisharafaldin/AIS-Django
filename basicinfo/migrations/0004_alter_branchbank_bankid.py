# Generated by Django 4.2.3 on 2023-08-21 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0003_branchbank_bankid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchbank',
            name='bankID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.bank', verbose_name='معرف البنك'),
        ),
    ]

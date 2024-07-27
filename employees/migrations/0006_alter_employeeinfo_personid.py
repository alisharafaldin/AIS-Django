# Generated by Django 4.2.3 on 2024-07-25 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0007_color_size'),
        ('employees', '0005_alter_employeeinfo_companyid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeinfo',
            name='personID',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='basicinfo.person'),
        ),
    ]

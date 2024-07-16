# Generated by Django 4.2.3 on 2024-07-14 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_remove_empinfo_companyid_remove_empinfo_personid_and_more'),
        ('accounts', '0004_qayd_companyid_qayd_sequence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qayddetails',
            name='empID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='employees.employeeinfo', verbose_name='الموظف'),
        ),
    ]

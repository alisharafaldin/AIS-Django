# Generated by Django 4.2.3 on 2024-08-03 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hadena', '0001_initial'),
        ('employees', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qayddetails',
            name='cycleID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cycleID', to='hadena.cycle', verbose_name='الدورة'),
        ),
        migrations.AddField(
            model_name='qayddetails',
            name='empID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='employees.employeeinfo', verbose_name='الموظف'),
        ),
    ]

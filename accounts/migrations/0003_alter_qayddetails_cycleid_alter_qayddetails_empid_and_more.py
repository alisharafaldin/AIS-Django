# Generated by Django 4.2.3 on 2024-07-09 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0002_typetransaction'),
        ('hadena', '0001_initial'),
        ('employees', '0001_initial'),
        ('accounts', '0002_auto_20240709_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qayddetails',
            name='cycleID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cycleID', to='hadena.cycle', verbose_name='الدورة'),
        ),
        migrations.AlterField(
            model_name='qayddetails',
            name='empID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='employees.empinfo', verbose_name='الموظف'),
        ),
        migrations.AlterField(
            model_name='qayddetails',
            name='projectID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.project', verbose_name='المشروع'),
        ),
        migrations.AlterField(
            model_name='qayddetails',
            name='shareholdersID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='المساهم', to='hadena.shareholdersinfo', verbose_name='المساهم'),
        ),
    ]
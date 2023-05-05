# Generated by Django 4.1.4 on 2023-02-06 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_project_countryid_project_directsupervisor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='countryID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='employees.countries', verbose_name='الدولة'),
        ),
        migrations.CreateModel(
            name='states',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stateName_ar', models.CharField(max_length=50, verbose_name='إسم المدينة عربي')),
                ('stateName_en', models.CharField(max_length=50, verbose_name='إسم المدينة إنجليزي')),
                ('population', models.CharField(blank=True, max_length=50, null=True, verbose_name='عدد السكان')),
                ('regionID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees.region', verbose_name='المنطقة')),
            ],
        ),
    ]

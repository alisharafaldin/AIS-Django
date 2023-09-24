# Generated by Django 4.2.3 on 2023-09-24 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0004_delete_currency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cities',
            old_name='cityName_ar',
            new_name='name_ar',
        ),
        migrations.RenameField(
            model_name='cities',
            old_name='cityName_en',
            new_name='name_en',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='proName_ar',
            new_name='name_ar',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='proName_er',
            new_name='name_er',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='RegionName_ar',
            new_name='name_ar',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='RegionName_en',
            new_name='name_en',
        ),
        migrations.RenameField(
            model_name='states',
            old_name='stateName_ar',
            new_name='name_ar',
        ),
        migrations.RenameField(
            model_name='states',
            old_name='stateName_en',
            new_name='name_en',
        ),
        migrations.RenameField(
            model_name='subproject',
            old_name='subProName_ar',
            new_name='name_ar',
        ),
        migrations.RenameField(
            model_name='subproject',
            old_name='subProName_er',
            new_name='name_er',
        ),
    ]
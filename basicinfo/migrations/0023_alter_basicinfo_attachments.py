# Generated by Django 4.2.3 on 2024-09-14 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0022_businessscope_icone_businessscope_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinfo',
            name='attachments',
            field=models.FileField(blank=True, null=True, upload_to='attach_basicInfo', verbose_name='مرفقات'),
        ),
    ]
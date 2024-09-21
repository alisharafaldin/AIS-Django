# Generated by Django 4.2.3 on 2024-09-16 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0026_cities_attachments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cities',
            name='attachments',
        ),
        migrations.AddField(
            model_name='cities',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo_cities', verbose_name='شعار المدينة'),
        ),
        migrations.AlterField(
            model_name='businessscope',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo_businessScope', verbose_name='شعار المجال'),
        ),
    ]
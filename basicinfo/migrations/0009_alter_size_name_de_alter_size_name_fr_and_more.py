# Generated by Django 4.2.3 on 2024-08-12 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0008_alter_color_name_en'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='name_de',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='مقاس ألمانيا'),
        ),
        migrations.AlterField(
            model_name='size',
            name='name_fr',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='مقاس فرنسا'),
        ),
        migrations.AlterField(
            model_name='size',
            name='name_gr',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='مقاس المملكة المتحدة'),
        ),
        migrations.AlterField(
            model_name='size',
            name='name_it',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='مقاس إيطاليا'),
        ),
        migrations.AlterField(
            model_name='size',
            name='name_us',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='مقاس الولايات المتحدة'),
        ),
    ]
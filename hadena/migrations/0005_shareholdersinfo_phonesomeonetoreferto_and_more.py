# Generated by Django 4.2.3 on 2024-01-07 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hadena', '0004_remove_shareholdersinfo_marketerid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shareholdersinfo',
            name='phoneSomeoneToReferTo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='هاتف شخص للرجوع إليه'),
        ),
        migrations.AddField(
            model_name='shareholdersinfo',
            name='someoneToReferTo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='شخص للرجوع إليه'),
        ),
    ]
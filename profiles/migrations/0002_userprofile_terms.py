# Generated by Django 4.2.3 on 2024-08-13 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='terms',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='الشروط'),
        ),
    ]
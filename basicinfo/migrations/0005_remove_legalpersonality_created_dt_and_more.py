# Generated by Django 4.2.3 on 2024-05-03 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0004_alter_person_created_dt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='legalpersonality',
            name='created_dt',
        ),
        migrations.RemoveField(
            model_name='person',
            name='created_dt',
        ),
    ]

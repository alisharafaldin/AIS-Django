# Generated by Django 4.2.3 on 2024-08-06 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoicebody',
            old_name='itemsDetailstID',
            new_name='itemID',
        ),
        migrations.RenameField(
            model_name='suppliers',
            old_name='legalPersonsID',
            new_name='legalPersonID',
        ),
    ]

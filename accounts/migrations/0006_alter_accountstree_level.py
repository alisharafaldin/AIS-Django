# Generated by Django 4.2.3 on 2024-08-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_accountstree_companyid_alter_accountstree_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountstree',
            name='level',
            field=models.IntegerField(blank=True, null=True, verbose_name='مستوى الحساب'),
        ),
    ]
# Generated by Django 4.2.3 on 2024-07-24 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0005_alter_company_owner_alter_companyuser_userid_and_more'),
        ('employees', '0004_delete_empinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeinfo',
            name='companyID',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='companys.company'),
        ),
    ]

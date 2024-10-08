# Generated by Django 4.2.3 on 2024-08-23 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0002_rename_legalpersonid_company_legalpersonid'),
        ('accounts', '0004_remove_qayddetails_itemsdetailstid'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountstree',
            name='companyID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='companys.company'),
        ),
        migrations.AlterField(
            model_name='accountstree',
            name='level',
            field=models.IntegerField(editable=False),
        ),
    ]

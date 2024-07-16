# Generated by Django 4.2.3 on 2024-07-14 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0004_rename_notes_company_notes_alter_company_pobox_and_more'),
        ('accounts', '0003_alter_qayddetails_cycleid_alter_qayddetails_empid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qayd',
            name='companyID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='companys.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qayd',
            name='sequence',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
    ]

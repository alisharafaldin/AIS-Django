# Generated by Django 4.2.3 on 2023-08-18 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0004_alter_person_genderid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='bankID',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.bank', verbose_name='البنك'),
        ),
        migrations.AlterField(
            model_name='person',
            name='branchBankID',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.branchbank', verbose_name='فرع البنك'),
        ),
        migrations.AlterField(
            model_name='person',
            name='cityID',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.cities', verbose_name='المدينة'),
        ),
        migrations.AlterField(
            model_name='person',
            name='companyID',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.company', verbose_name='الشركة'),
        ),
        migrations.AlterField(
            model_name='person',
            name='countryID',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='countryID', to='basicinfo.countries', verbose_name='الدولة'),
        ),
        migrations.AlterField(
            model_name='person',
            name='nationalityID',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='nationalityID', to='basicinfo.countries', verbose_name='الجنسية'),
        ),
        migrations.AlterField(
            model_name='person',
            name='socialStatusID',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.socialstatus', verbose_name='الحالة الإجتماعية'),
        ),
        migrations.AlterField(
            model_name='person',
            name='stateID',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.states', verbose_name='الولاية'),
        ),
        migrations.AlterField(
            model_name='person',
            name='typeAccBankID',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.typeaccbank', verbose_name='نوع الحساب'),
        ),
        migrations.AlterField(
            model_name='person',
            name='typeID',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.typeid', verbose_name='نوع الهوية'),
        ),
        migrations.AlterField(
            model_name='person',
            name='workSpecialtyID',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.workspecialty', verbose_name='التخصص'),
        ),
        migrations.AlterField(
            model_name='person',
            name='workTradeID',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.worktrade', verbose_name='المهنة'),
        ),
    ]
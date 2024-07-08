# Generated by Django 4.2.3 on 2024-07-08 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0005_remove_legalpersonality_created_dt_and_more'),
        ('employees', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0022_alter_qayd_details'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qayd',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='qayddetails',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='qayd',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='qayds_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='qayd',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='التاريخ'),
        ),
        migrations.AlterField(
            model_name='qayd',
            name='details',
            field=models.ManyToManyField(blank=True, related_name='qayds', through='accounts.QaydDetails', to='accounts.accountstree'),
        ),
        migrations.AlterField(
            model_name='qayd',
            name='typeTransactionID',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.typetransaction', verbose_name='نوع العملية'),
        ),
        migrations.AlterField(
            model_name='qayd',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_qayds', to=settings.AUTH_USER_MODEL, verbose_name='المُعدِل'),
        ),
        migrations.AlterField(
            model_name='qayddetails',
            name='accountID',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.accountstree', verbose_name='الحساب'),
        ),
        migrations.AlterField(
            model_name='qayddetails',
            name='currencyID',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.countries', verbose_name='العملة'),
        ),
        migrations.AlterField(
            model_name='qayddetails',
            name='date_details',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='التاريخ'),
        ),
        migrations.AlterField(
            model_name='qayddetails',
            name='empID',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='employees.empinfo', verbose_name='الموظف'),
        ),
        migrations.AlterField(
            model_name='qayddetails',
            name='projectID',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.project', verbose_name='المشروع'),
        ),
        migrations.AlterField(
            model_name='qayddetails',
            name='qaydID',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='qayd_details', to='accounts.qayd'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.3 on 2024-09-07 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0013_alter_persons_languagesid_alter_persons_skillsid'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessScope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ar', models.CharField(max_length=100, verbose_name='مجال العمل عربي')),
                ('name_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='مجال العمل إنجليزي')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessScopeSpecialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ar', models.CharField(max_length=100, verbose_name='تخصص مجال العمل عربي')),
                ('name_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='تخصص مجال العمل إنجليزي')),
                ('businessScopeID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.businessscope', verbose_name='معرف مجال العمل')),
            ],
        ),
        migrations.AddField(
            model_name='legalpersons',
            name='businessScopeID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.businessscope', verbose_name='مجال العمل'),
        ),
        migrations.AddField(
            model_name='legalpersons',
            name='businessScopeSpecializationID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.businessscopespecialization', verbose_name='تخصص مجال العمل'),
        ),
    ]

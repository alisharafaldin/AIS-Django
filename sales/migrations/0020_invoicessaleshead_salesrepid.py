# Generated by Django 4.2.3 on 2024-08-21 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_rename_employeeinfo_employee'),
        ('sales', '0019_alter_invoicessaleshead_attachments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicessaleshead',
            name='salesRepID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='employees.employee', verbose_name='مندوب المبيعات'),
        ),
    ]

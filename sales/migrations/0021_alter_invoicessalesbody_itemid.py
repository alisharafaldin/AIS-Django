# Generated by Django 4.2.3 on 2024-08-23 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_items_options'),
        ('sales', '0020_invoicessaleshead_salesrepid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicessalesbody',
            name='itemID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sales_details', to='products.items', verbose_name='المنتج'),
        ),
    ]

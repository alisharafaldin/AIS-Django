# Generated by Django 4.2.3 on 2024-08-12 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0009_alter_size_name_de_alter_size_name_fr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='color',
            field=models.CharField(default='#FF0000', help_text='Enter the color in hex format, e.g., #FFFFFF', max_length=7),
        ),
    ]

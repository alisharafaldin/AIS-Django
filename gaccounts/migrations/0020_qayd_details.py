# Generated by Django 4.2.3 on 2023-07-24 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaccounts', '0019_remove_qayd_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='qayd',
            name='details',
            field=models.ManyToManyField(through='gaccounts.QaydDetails', to='gaccounts.accountstree'),
        ),
    ]

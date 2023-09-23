# Generated by Django 4.2.3 on 2023-09-22 12:58

import creditcards.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('is_finished', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_address', models.CharField(max_length=150)),
                ('ship_phone', models.CharField(max_length=50)),
                ('cart_number', creditcards.models.CardNumberField(max_length=25)),
                ('expire', creditcards.models.CardExpiryField()),
                ('security_code', creditcards.models.SecurityCodeField(max_length=4)),
                ('orderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.IntegerField()),
                ('orderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='order',
            name='details',
            field=models.ManyToManyField(through='orders.OrderDetails', to='products.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

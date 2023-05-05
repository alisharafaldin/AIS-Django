from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField

# Create your models here.

class Order(models.Model):
    # ربط بين الأوردر واليوزر
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    # لربط جدول مني تو مني
    details = models.ManyToManyField(Product, through='OrderDetails')
    is_finished = models.BooleanField()
    total = 0
    items_count = 0
    def __str__(self):
        return 'User: ' + self.userID.username + ' | Order id: ' + str(self.id)

class OrderDetails(models.Model):
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return 'User: ' + self.orderID.userID.username + '  | Product: ' + self.productID.name + ' | Order id: ' + str(self.orderID.id)

    class Meta:
        #ترتيب العناصر حسب الآي دي
        ordering = ['-id']

class Payment(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    ship_address = models.CharField(max_length=150)
    ship_phone = models.CharField(max_length=50)
    cart_number = CardNumberField()
    expire = CardExpiryField()
    security_code = SecurityCodeField()
    def __str__(self):
        return 'Order ID : ' + str(self.orderID.id)


from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from basicinfo.models import Person

# Create your models here.

class UserProfile(models.Model):
    userID = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user')
    personID = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='profile_person')


    def __str__(self):
        return self.userID.username 
        
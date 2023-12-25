from django.contrib.auth.models import AbstractUser, User
from django.db import models
import hashlib

class list_of_hosts(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.address} - {self.phone}'

class list_of_animals(models.Model):
    name = models.CharField(max_length=20)
    kind_of_animal = models.CharField(max_length=30)
    breed = models.CharField(max_length=20)
    age = models.IntegerField()
    host = models.ForeignKey('list_of_hosts', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class diseases(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

# class CustomerUser(AbstractUser):
#     surname = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     middle_name = models.CharField(max_length=100)
#     email = models.EmailField(unique = True)
#     password = models.CharField(max_length=128)
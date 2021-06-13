from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
import staff.models


class Cart(models.Model):
    STATUS = (
        (1, 'active'),
        (2, 'inactive'),
    )

    cart_type = models.CharField(max_length=100)
    status = models.IntegerField(max_length=10, choices=STATUS)


class User(AbstractUser):
    address = models.ForeignKey('staff.Address', on_delete=models.CASCADE, null=True)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)

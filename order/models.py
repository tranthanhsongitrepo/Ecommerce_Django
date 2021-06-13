from django.db import models

# Create your models here.
from django.forms import ModelForm



class Payment(models.Model):
    amount = models.FloatField(max_length=100)
    additional_fee = models.FloatField(max_length=100)


class CreditCard(models.Model):
    credit_number = models.BigIntegerField()
    customer = models.ForeignKey('user.User', on_delete=models.CASCADE)


class CreditCardPayment(Payment):
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE)


class OrderStatus(models.Model):
    status = models.CharField(max_length=100)


class Order(models.Model):
    sale_off = models.FloatField()
    payment = models.OneToOneField('Payment', on_delete=models.CASCADE)
    customer = models.ForeignKey('user.User', on_delete=models.CASCADE)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)


class OrderStatusLogs(models.Model):
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    business_staff = models.ForeignKey('staff.Staff', on_delete=models.CASCADE)


class Credit(Payment):
    creditNumber = models.BigIntegerField()


class Bill(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Shipment(models.Model):
    ship_date = models.DateTimeField(max_length=100)
    receive_date = models.DateTimeField(max_length=100)
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)


class ShipmentStatus(models.Model):
    status = models.CharField(max_length=100)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)


class DomesticShip(Shipment):
    distance = models.BigIntegerField()
    district = models.CharField(max_length=100)


class GlobalShip(Shipment):
    country = models.CharField(max_length=100)
    delivery_type = models.CharField(max_length=100)


class Notification(models.Model):
    content = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)

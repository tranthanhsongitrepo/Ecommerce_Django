from django.db import models


# Create your models here.

class Address(models.Model):
    fullAddress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.fullAddress + ', ' + self.city + ', ' + self.country


class Payment(models.Model):
    amount = models.CharField(max_length=100)
    additionalFee = models.CharField(max_length=100)


class Fullname(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Person(models.Model):
    sex = models.CharField(max_length=100)
    age = models.IntegerField()
    fullname = models.ForeignKey(Fullname, on_delete=models.CASCADE)


class Customer(Person):
    credits = models.IntegerField(max_length=100)


class CreditCard(models.Model):
    creditNumber = models.BigIntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class CreditCardPayment(Payment):
    creditCard = models.ForeignKey(CreditCard, on_delete=models.CASCADE)


class AccountStatus(models.Model):
    status = models.CharField(max_length=100)
    time = models.DateTimeField(max_length=100)


class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    accountStatus = models.OneToOneField(AccountStatus, on_delete=models.CASCADE)


class User(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Admin(User):
    company = models.CharField(max_length=100)


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    ad = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + str(self.ad)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BookStatus(models.Model):
    status = models.CharField(max_length=100)


class BookDescription(models.Model):
    font = models.IntegerField()
    paperSize = models.CharField(max_length=100)
    colorFont = models.CharField(max_length=100)
    bookStatus = models.OneToOneField(BookStatus, on_delete=models.CASCADE)


class Book(Product):
    bookDescription = models.ForeignKey(BookDescription, on_delete=models.CASCADE)


class Author(Person):
    organization = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class ProductImage(models.Model):
    path = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Storage(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    # chưa nối quan hệ trong bd class

    def __str__(self):
        return str(self.address)


class Item(models.Model):
    saleOff = models.FloatField()
    price = models.FloatField()


class ProductInStock(models.Model):
    stock = models.IntegerField()
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=100)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Cart(models.Model):
    cartType = models.CharField(max_length=100)


class Order(models.Model):
    saleOff = models.FloatField()
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class ItemInCart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Credit(Payment):
    creditNumber = models.BigIntegerField()


class Bill(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Shipment(models.Model):
    dateShip = models.DateTimeField(max_length=100)
    receiveDate = models.DateTimeField(max_length=100)
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)


class ShipmentStatus(models.Model):
    status = models.CharField(max_length=100)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)


class DomesticShip(Shipment):
    distance = models.BigIntegerField()
    district = models.CharField(max_length=100)


class GlobalShip(Shipment):
    country = models.CharField(max_length=100)
    typeDelivery = models.CharField(max_length=100)


class Notification(models.Model):
    content = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)

    ''''''


class Genre(models.Model):
    genre = models.CharField(max_length=100)


class BookGenre(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    bookDescription = models.ForeignKey(BookDescription, on_delete=models.CASCADE)


class Electronic(Product):
    desc = models.CharField(max_length=100)


class Appliance(Electronic):
    width = models.CharField(max_length=100)
    height = models.FloatField()
    length = models.FloatField()
    type_of_appliance = models.CharField(max_length=100)


class Mobile(Electronic):
    dimension = models.FloatField()
    device_type = models.CharField(max_length=100)


class ClothingType(models.Model):
    name = models.CharField(max_length=100)


class Clothing(Product):
    material = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    type_of_clothing = models.ForeignKey(ClothingType, on_delete=models.CASCADE)


class Staff(Person):
    workAddress = models.ForeignKey(Address, on_delete=models.CASCADE)


class StorageStaff(Staff):
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)


class OrderStatus(models.Model):
    status = models.CharField(max_length=100)


class OrderStatusLogs(models.Model):
    orderStatus = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)


class BusinessStaff(Staff):
    test = models.CharField(max_length=100)


class OrderStatusChangeLogs(models.Model):
    businessStaff = models.ForeignKey(BusinessStaff, on_delete=models.CASCADE)
    orderStatusLogs = models.ForeignKey(
        OrderStatusLogs, on_delete=models.CASCADE)

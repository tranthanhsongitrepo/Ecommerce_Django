from django.db import models
from django.utils.safestring import mark_safe

from user.models import User


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    ad = models.OneToOneField('staff.Address', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + str(self.ad)


class Product(models.Model):
    TYPE = (
        ('1', 'Quần Áo'),
        ('2', 'Sách'),
        ('3', 'Điện Tử')
    )
    STATUS = (
        ('True', 'Đang Kinh Doanh'),
        ('False', 'Ngừng Kinh Doanh'),
    )

    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    type = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format('/static' + self.image.url))
        else:
            return ""
    # def category(self):
    #     if self.TYPE


class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductInStock(models.Model):
    stock = models.IntegerField()
    storage = models.ForeignKey('staff.Storage', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Item(models.Model):
    sale_off = models.FloatField()
    price = models.FloatField()
    product = models.OneToOneField('product.Product', on_delete=models.CASCADE)


class ItemInCart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey('user.Cart', on_delete=models.CASCADE)
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()


# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=100)


class BookStatus(models.Model):
    status = models.CharField(max_length=100)


class Author(models.Model):
    sex = models.CharField(max_length=100)
    age = models.IntegerField()
    fullname = models.ForeignKey('staff.Fullname', on_delete=models.CASCADE)
    organization = models.CharField(max_length=100)


class Book(Product):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 2

    bookDescription = models.ForeignKey(BookStatus, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class BookGenre(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    book_description = models.ForeignKey(BookStatus, on_delete=models.CASCADE)


class Electronic(Product):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 3

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

    def __str__(self):
        return self.name


class Clothing(Product):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 1

    material = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    type_of_clothing = models.ForeignKey(ClothingType, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=100)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    sentiment = models.IntegerField(null=True)

from django.db import models
from user.models import UserModel

class Category(models.Model):
    class Meta:
        db_table = "category"

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

class UserOrder(models.Model):
    class Meta:
        db_table = "user_order"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    total_amount = models.IntegerField()
    quantity = models.IntegerField()
    discount_rate = models.IntegerField()
    final_price = models.IntegerField()
    time = models.DateTimeField()


class OrderStatus(models.Model):
    class Meta:
        db_table = "order_status"

    order_status = models.CharField(max_length=128)

class Product(models.Model):
    class Meta:
        db_table = "product"

    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.CharField(max_length=128)
    desc = models.CharField(max_length=128)
    price = models.CharField(max_length=128)
    stock = models.IntegerField()
from django.contrib import admin
from .models import Category, UserOrder, OrderStatus,Product

# Register your models here.
admin.site.register(Category)
admin.site.register(UserOrder)
admin.site.register(OrderStatus)
admin.site.register(Product)
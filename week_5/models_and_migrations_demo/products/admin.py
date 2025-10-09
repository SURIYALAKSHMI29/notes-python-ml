from django.contrib import admin

# Register your models here.
from .models import Product, Order, OrderItem, Customer

# this allows to manipulate them from admin dashboard
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)
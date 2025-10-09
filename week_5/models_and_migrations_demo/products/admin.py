from django.contrib import admin

# Register your models here.
from .models import Product, Order, OrderItem, Customer

# this allows to manipulate them from admin dashboard
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "qty_on_hand")  # Columns in list view
    search_fields = ("name",)  # Adds a search box
    list_filter = ("qty_on_hand",)  # Filter sidebar
    ordering = ("name",)  # Default sorting

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)
from django.db import models

# Create your models here
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    qty_on_hand = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.id}: {self.name} costs ${self.price} per unit, Available: {self.qty_on_hand}"
    
class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.name} - {self.phone}"
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="orders", default="Guest")
    total_amount = models.FloatField(default=0)
    purchase_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.pk}: {self.customer.name} - ${self.total_amount} at {self.purchase_date}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="product_name")
    quantity = models.IntegerField()
    price_per_item = models.FloatField()
    amount = models.FloatField()
    
    def __str__(self):
        return f"{self.order.pk}:Purchased {self.product.name} - {self.quantity} quantity(s) for a grand sum of {self.amount}"
    
    
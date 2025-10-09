from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Product, Order, Customer, OrderItem

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "products/index.html", {"products": products})

def product(request, product_id):
    product = Product.objects.get(pk=product_id)   # pk -> Primary key; generic way
    # product = Product.objects.get(id=product_id)
    
    customers = Customer.objects.filter(
        orders__order_items__product=product
    ).distinct()
    # orders__order_items__product -> traverses the ForeignKey relationships:
    # Customer → Order → OrderItem → Product
    
    return render(request, "products/product.html", {"product": product,  "customers": customers})

def orders(request):
    return render(request, "products/orders.html", {"orders": Order.objects.all()})

def place_order(request):
    if request.method == "POST":
        customer_id = request.POST.get("customer_id")
        if not customer_id:
            messages.error(request, "Please select a customer before placing the order")
            return HttpResponseRedirect(reverse("place_order"))
        
        customer = Customer.objects.get(pk=customer_id)
        
        order = Order.objects.create(customer=customer)
        total = 0
        
        for product_id, quantity in request.POST.items():
            if(product_id == "csrfmiddlewaretoken" or product_id == "customer_id"):
                continue
            
            product = Product.objects.get(pk=int(product_id))
            amt = product.price * int(quantity)
            OrderItem.objects.create(
                order=order,
                product=product, 
                quantity=quantity, 
                price_per_item=product.price, 
                amount=amt
            )
            total += amt
        
        order.total_amount = total
        order.save()
        
        return HttpResponseRedirect(reverse("orders"), {"success": "Order placed successfully."})

    products = Product.objects.all()
    customers = Customer.objects.all()
    return render(request, "products/place_order.html", {"products": products, "customers": customers})


def order(request, order_id):
    order = Order.objects.get(pk=order_id)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, "products/order.html", {"order": order, "order_items": order_items})
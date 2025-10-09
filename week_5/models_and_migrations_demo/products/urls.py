from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Syntax
    #     path('url-pattern/', view_function, name='url_name')
    
    # "" -> empty string, default URL of the app ".../products"
    # views.index -> A view function to call when this URL is visited
    # name = "index" -> name for this url, so we can refer to it somewhere else
    
    path("<int:product_id>", views.product, name="product"),
    path("orders", views.orders, name="orders"),
    path("order/<int:order_id>", views.order, name="order"),
    path("place_order", views.place_order, name="place_order"),
]

from django.contrib import admin

# Register your models here.
from .models import Category, Customer, Product, Cart, CartProduct, Order 

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Order)
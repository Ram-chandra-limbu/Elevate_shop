
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user= models.OneToOneField(User, on_delete= models.CASCADE)
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    joined_on = models.DateTimeField(auto_now_add=True)



class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.title
  

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    selling_price = models.PositiveBigIntegerField()
    image = models.ImageField(default='default.jpg',upload_to='product_images/')
    description = models.TextField()
    warrenty = models.CharField(max_length=50)
    return_policy = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
    
class Cart(models.Model):
    user=models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name  

class CartProduct(models.Model):
    cart= models.ForeignKey(Cart, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    rate= models.PositiveIntegerField()
    quality= models.PositiveBigIntegerField()
    sub_total= models.PositiveBigIntegerField()

    def __str__(self):
        return self.cart

ORDER_STATUS = (
    ('order Revived', "order recived"),
    ("orderprossing", "Order Prossing"),
    ("on the way", "on the way"),
    ("Order complete", "Order complete"),
    )

class Order(models.Model):
    cart= models.OneToOneField(Cart, on_delete= models.CASCADE)
    orderd_by = models.CharField( max_length=255)
    shopping_address = models.CharField(max_length=200)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=10)
    subtotal= models.PositiveBigIntegerField()
    discount= models.PositiveBigIntegerField()
    total= models.PositiveBigIntegerField()
    order_status= models.CharField(max_length=250, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
        return self.cart

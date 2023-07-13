from django.urls import path
from .views import *

app_name = 'product'
urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('about/', About.as_view(), name='About'),
    path('contact/', Contact.as_view(), name='Contact'),
    path('allproducts/', allproductView.as_view(), name='allproducts'),
    path('product/<slug:slug>', singleProduct.as_view(), name='singleProduct' ),
    # path('add-to-card/<int:pk>/', AddToCardView.as_view(), name="addtocard")
    
]



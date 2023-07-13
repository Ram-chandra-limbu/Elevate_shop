from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class Home(TemplateView):
    template_name = 'Home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product= Product.objects.all()
        context["product"] = product
        return context

class About(TemplateView): 
    template_name = 'About.html'

class Contact(TemplateView):
    template_name = 'Contact.html'

class allproductView(TemplateView):
    template_name = 'allproduct.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        context["categories"]= category 
        return context
    
class singleProduct(TemplateView):
    template_name = 'singleProduct.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs['slug']
        product = Product.objects.get(slug=url_slug)
        context["product"]= product  
        return context
    
# class AddToCartView(TemplateView):
#     template_name = 'addtocart.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         product_id=self.kwargs[product_id]
#         product_obj = Product.object.get(id=product_id)
#         print(product_obj)

#     cart_id = self.request.session.get(card_id, None)
#     if card_id:
#         print(cart_id)
#     else:
#         cart.obj = Cart.objects.create(total=0)
#         self.request.session[card_id] = cart.obj.id
#         cartproduct=CartProduct.objects.create(
#             cart = cart_obj,
#             Product= product_obj;
#             rate = product.obj.selling_price,
#             quality= 1,
#             sub_total= product_obj.selling_price,
#         )


    





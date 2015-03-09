from django.shortcuts import render, render_to_response
from core.models import *
from core.forms import *
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# view imports
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import FormView
from django.views.generic import DeleteView
from django.views.generic import TemplateView
from carton.cart import Cart
# Create your views here.

def add(request):
    cart = Cart(request.session)
    product = Item.objects.get(id=request.GET.get('id'))
    others = {'size':Size.objects.get(id=request.GET.get('size')).size, 
    'color':Colour.objects.get(id=request.GET.get('colorid')).colour,
     'seller':Seller.objects.get(id=request.GET.get('sellerid')).name, 
     'price':request.GET.get('price')}
    cart.add(product, others=others)
    return HttpResponse(cart.count)

def show(request):
    return render(request, 'cart/cart.html')

def clear(request):
	cart = Cart(request.session)
	cart.clear()
	return HttpResponse("ok")

def remove(request, pk):
    cart = Cart(request.session)
    try:
        cart.remove(Item.objects.get(id=pk))
    except:
        messages.error(request, "This item is already deleted from cart")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    messages.success(request, "Item removed from the cart");
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def checkout(request):
    return render_to_response('cart/delivery_address.html',{ 'form':DeliveryAddressForm() }, context_instance=RequestContext(request))

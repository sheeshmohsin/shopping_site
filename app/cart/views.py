from django.shortcuts import render, render_to_response
from core.models import *
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponse
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
    cart.add(product, price=product.price)
    return HttpResponse(len(cart.items))

def show(request):
    return render(request, 'cart.html')

from django.shortcuts import render, render_to_response
from core.models import *
from core.forms import *
from django.core import serializers
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.pagination import PaginationSerializer
from django.template import RequestContext
from django.db.models import Q
# view imports
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import FormView
from django.views.generic import DeleteView
from django.views.generic import TemplateView

# Create your views here.

def home(request):
    filter_criteria = (Q(fk_type__category="Mens") | Q(fk_type__category="Boys")) & Q(new_arrival=True)
    new_arrival_male = Item.objects.filter(filter_criteria)
    
    filter_criteria = (Q(fk_type__category="Womens") | Q(fk_type__category="Girls")) & Q(new_arrival=True)
    new_arrival_female = Item.objects.filter(filter_criteria)
    return render_to_response('home.html', {'final':new_arrival_male, 'final1':new_arrival_female}
        , context_instance=RequestContext(request))

# class HomeView(TemplateView):
#     template_name = 'home.html'

def catalog(request, pk):
    category = Category.objects.get(id=pk)
    subcategories = Category.objects.filter(parent=category)
    result = Item.objects.filter(fk_type__category=category)
    paginator = Paginator(result, 9)

    page = request.GET.get('page')

    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)

    return render_to_response('catalog.html', {'subcategories':subcategories, 'finals':result},
     context_instance=RequestContext(request))

def item(request, pk):
    item = Item.objects.get(id=pk)
    f = Q(seller=item.price_set.all()[0].fk_seller) | Q(color=item.price_set.all()[0].fk_color)
    images = item.itemimage_set.filter(f)
    return render_to_response('item.html', {'item':item, 'images':images, 'reviewform':ReviewForm}, context_instance=RequestContext(request))

def feedback(request):
    return render_to_response('feedback.html', context_instance=RequestContext(request))

def checkpin(request):
    pincode = request.POST['pincode']
    try:
        city = Pincode.objects.get(pincode=pincode)
        return HttpResponse("ok")
    except ObjectDoesNotExist:
        return HttpResponse("not ok")



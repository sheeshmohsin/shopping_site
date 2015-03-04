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
from django.contrib.auth.decorators import login_required
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

def item(request, pk, color_pk, seller_pk):
    item = Item.objects.get(id=pk)
    images = item.itemimage_set.filter(color_id=color_pk)
    price = item.price_set.get(Q(fk_seller__id=seller_pk) & Q(fk_color__id=color_pk))
    return render_to_response('item.html', {'item':item, 'images':images,
    'price':price, 'reviewform':ReviewForm, 'reviews':item.reviews_set.all()[:5]}, context_instance=RequestContext(request))

def feedback(request):
    return render_to_response('feedback.html', context_instance=RequestContext(request))

def checkpin(request):
    pincode = request.POST['pincode']
    try:
        city = Pincode.objects.get(pincode=pincode)
        return HttpResponse("ok")
    except ObjectDoesNotExist:
        return HttpResponse("not ok")

@login_required
def review(request, pk):
    if request.method=="POST":
        form = ReviewForm(request.POST)
        f = form.save(commit=False)
        f.user = request.user
        f.item = Item.objects.get(id=pk)
        f.save()
        return HttpResponse("ok")
    else:
        return HttpResponse("not ok")


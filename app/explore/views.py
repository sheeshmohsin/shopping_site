from django.shortcuts import render, render_to_response
from core.models import *
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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


# def item(request, pk):
#     item = Item.objects.get(id=pk)
#     return render_to_response('item.html', {'item':item}, context_instance=RequestContext(request))

# def catalog(request, pk):
#     category = Main.objects.get(id=pk)
#     subcategories = category.dresses_type_set.all()
#     final = Item.objects.filter(fk_type__fk_main__category=category.category)
#     paginator = Paginator(final, 3)

#     page = request.GET.get('page')
#     try:
#         finals = paginator.page(page)
#     except PageNotAnInteger:
#         finals = paginator.page(1)
#     except EmptyPage:
#         finals = paginator.page(paginator.num_pages)
#     return render_to_response('catalog.html', {'subcategories':subcategories, 'category': category, 'finals':finals,}, context_instance=RequestContext(request))

# def feedback(request):
#     return render_to_response('feedback.html', context_instance=RequestContext(request))



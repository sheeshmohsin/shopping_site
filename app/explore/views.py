from django.shortcuts import render, render_to_response
from core.models import *
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.db.models import Q
# view imports
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import FormView
from django.views.generic import DeleteView
from django.views.generic import TemplateView

# Create your views here.

def home(request):
    categories = Main.objects.all()
    f = Q(fk_type__fk_main__category="Mens") | Q(fk_type__fk_main__category="Boys")
    final = Item.objects.filter(f).filter(new_arrival=True)
    
    g = Q(fk_type__fk_main__category="Womens") | Q(fk_type__fk_main__category="Girls")
    final1 = Item.objects.filter(g).filter(new_arrival=True)
    
    return render_to_response('home.html', {'categories':categories, 'final':final, 'final1':final1})

class HomeView(TemplateView):
    template_name = 'home.html'


def item(request, pk):
    item = Item.objects.get(id=pk)
    return render_to_response('item.html', {'item':item}, context_instance=RequestContext(request))

def catalog(request, pk):
    category = Main.objects.get(id=pk)
    subcategories = category.dresses_type_set.all()
    final = Item.objects.filter(fk_type__fk_main__category=category.category)
    paginator = Paginator(final, 3)

    page = request.GET.get('page')
    try:
        finals = paginator.page(page)
    except PageNotAnInteger:
        finals = paginator.page(1)
    except EmptyPage:
        finals = paginator.page(paginator.num_pages)
    return render_to_response('catalog.html', {'subcategories':subcategories, 'category': category, 'finals':finals,}, context_instance=RequestContext(request))

def feedback(request):
    return render_to_response('feedback.html', context_instance=RequestContext(request))



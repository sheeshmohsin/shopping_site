from django.shortcuts import render, render_to_response
from core.models import *
from django.core.context_processors import csrf
from django.template import RequestContext
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
	return render_to_response('home.html', context_instance=RequestContext(request))

class HomeView(TemplateView):
	template_name = 'home.html'


def item(request):
	return render_to_response('item.html', context_instance=RequestContext(request))

def catalog(request, pk):
	category = Main.objects.get(id=pk)
	subcategories = category.dresses_type_set.all()
	return render_to_response('catalog.html', {'subcategories':subcategories}, context_instance=RequestContext(request))

def feedback(request):
	return render_to_response('feedback.html', context_instance=RequestContext(request))
	
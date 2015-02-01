from django.shortcuts import render, render_to_response
from core.models import *

# Create your views here.

def home(request):
	categories = Main.objects.all()
	return render_to_response('home.html', {'categories':categories})

def item(request):
	return render_to_response('item.html')

def catalog(request, pk):
	categories = Main.objects.all()
	category = Main.objects.get(id=pk)
	subcategories = category.dresses_type_set.all()
	return render_to_response('catalog.html', {'subcategories':subcategories, 'categories':categories})

def feedback(request):
	return render_to_response('feedback.html')
	
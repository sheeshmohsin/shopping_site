from django.shortcuts import render, render_to_response
from core.models import *
# Create your views here.
def home(request):
	categories = Main.objects.all()
	return render_to_response('home.html', {'categories':categories})

def item(request):
	return render_to_response('item.html')
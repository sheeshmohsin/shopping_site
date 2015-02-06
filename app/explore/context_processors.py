from core.models import *

def category_list(request):
	return { 'categories': Main.objects.all() }

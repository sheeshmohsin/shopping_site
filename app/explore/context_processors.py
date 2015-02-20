from core.models import *

def category_list(request):
	return { 'categories': Category.objects.filter(parent_id__isnull=True) }

from core.models import *
from carton.cart import Cart

def category_list(request):
	return { 'categories': Category.objects.filter(parent_id__isnull=True) }

def cart_item(request):
	cart = Cart(request.session)
	return {'lencart': cart.count}
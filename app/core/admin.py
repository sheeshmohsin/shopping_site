from django.contrib import admin
from core.models import Main, Size, Colour, Dresses_type, Seller, Item

# Register your models here.
admin.site.register(Main)
admin.site.register(Size)
admin.site.register(Colour)
admin.site.register(Dresses_type)
admin.site.register(Seller)
admin.site.register(Item)

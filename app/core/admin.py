from django.contrib import admin
from core.models import Category, Size, Colour, Seller, Item, Price, Feedback

# Register your models here.
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Colour)
admin.site.register(Seller)
admin.site.register(Item)
admin.site.register(Price)
admin.site.register(Feedback)

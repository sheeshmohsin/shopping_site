from django.db import models
from core.utils import get_upload_file_path
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Main(models.Model):
    category = models.CharField(_('Category'), max_length=50)

    def __unicode__(self):
        return self.category

class Dresses_type(models.Model):
    subcategory = models.CharField(_('Subcategory'), max_length=50)
    fk_main = models.ForeignKey(Main)

    def __unicode__(self):
        return self.subcategory

class Colour(models.Model):
    colour = models.CharField(_('Colour'), max_length=50)

class Size(models.Model):
    size = models.CharField(_('Size'), max_length=50)

class Seller(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    address = models.CharField(_('Address'), max_length=50)
    email = models.EmailField(_('Email Address'), max_length=50)
    contactno = models.IntegerField(_('Contact No.'), max_length=10)

class Item(models.Model):  
    created = models.CharField(_('Created'), max_length=50)
    item_name = models.CharField(_('Item'), max_length=50)
    description = models.CharField(_('Description'), max_length=50)
    fk_color = models.ForeignKey(Colour)
    fk_size = models.ForeignKey(Size)
    price = models.CharField(_('Price'), max_length=50)
    discount = models.CharField(_('Discount'), max_length=50)
    picture1 = models.ImageField(_('Image1'), upload_to=get_upload_file_path)
    picture2 = models.ImageField(_('Image2'), upload_to=get_upload_file_path)
    picture3 = models.ImageField(_('Image3'), upload_to=get_upload_file_path)
    picture4 = models.ImageField(_('Image3'), upload_to=get_upload_file_path)
    instock = models.CharField(_('Instock'), max_length=50)
    cod = models.CharField(_('COD'), max_length=50)
    fk_seller = models.ForeignKey(Seller)
    fk_type = models.ForeignKey(Dresses_type)



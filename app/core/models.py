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
    main = models.ForeignKey(Main)

    def __unicode__(self):
        return self.subcategory

class Colour(models.Model):
    colour = models.CharField(_(Colour), max_length=50)

class Size(models.Model):
    size = models.CharField(_(Size), max_length=50)

class Item(models.Model):
    item_name = models.CharField(_(Item), max_length=50)
    color = models.ForeignKey(Colour)
    size = models.ForeignKey(Size)
    price = models.CharField(_(Price), max_length=50)
    picture = models.ImageField(_('Image'), upload_to=get_upload_file_path)
    type = models.ForeignKey(Dresses_type)

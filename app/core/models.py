from django.db import models
from core.utils import get_upload_file_path
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Category(models.Model):
    category = models.CharField(_('Category'), max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
    is_active = models.BooleanField(_("Active"), default=True)
    related_categories = models.ManyToManyField('self', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Category'

    def __unicode__(self):
        return self.category

class Colour(models.Model):
    colour = models.CharField(_('Colour'), max_length=50)

    class Meta:
        verbose_name_plural = 'Colour'

    def __unicode__(self):
        return self.colour

class Size(models.Model):
    size = models.CharField(_('Size'), max_length=6)

    class Meta:
        verbose_name_plural = 'Size'

    def __unicode__(self):
        return self.size

class Seller(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    address = models.TextField(_('Address'), max_length=50)
    email = models.EmailField(_('Email Address'), max_length=20)
    contactno = models.CharField(_('Contact No.'), max_length=10)

    class Meta:
        verbose_name_plural = 'Seller'

    def __unicode__(self):
        return self.name

class Item(models.Model):
    new_arrival = models.BooleanField(_('New Arrival'))  
    created = models.DateField(_('Created'), max_length=50)
    item_name = models.CharField(_('Item'), max_length=50)
    description = models.TextField(_('Description'), max_length=50)
    fk_color = models.ManyToManyField(Colour)
    fk_size = models.ManyToManyField(Size)
    items_in_stock = models.DecimalField(_("Number in stock"),  max_digits=18, decimal_places=6, default='0')
    total_sold = models.DecimalField(_("Total sold"),  max_digits=18, decimal_places=6, default='0')
    instock = models.BooleanField(_('Instock'), max_length=50)
    fk_seller = models.ManyToManyField(Seller)
    fk_type = models.ManyToManyField(Category)
    related_items = models.ManyToManyField('self', blank=True, null=True, verbose_name=_('Related Items'))
    also_purchased = models.ManyToManyField('self', blank=True, null=True, verbose_name=_('Previously Purchased'))

    class Meta:
        verbose_name_plural = 'Item'

    def __unicode__(self):
        return self.item_name

class Price(models.Model):
    item = models.ForeignKey(Item)
    price = models.CharField(_('Price'), max_length=9)
    discount = models.CharField(_('Discount'), max_length=5)
    cod = models.BooleanField(_('COD'), max_length=50)
    fk_seller = models.ForeignKey(Seller)
    fk_color = models.ForeignKey(Colour)
    fk_size = models.ForeignKey(Size)

    class Meta:
        verbose_name_plural = 'Price'

    def __unicode__(self):
        return self.price

class Feedback(models.Model):
    CATEGORY_CHOICE = (
        ('Feedback', 'feedback'),
        ('Suggestion', 'suggestion'),
        ('Complain', 'complain'),
        ('Other', 'other'),
    )
    name = models.CharField(_('Name'), max_length=50)
    category = models.CharField(_('Category'), choices=CATEGORY_CHOICE, max_length=25)
    description = models.TextField(_('Description'), max_length=200)

    class Meta:
        verbose_name_plural = 'Feedback'

    def __unicode__(self):
        return self.name

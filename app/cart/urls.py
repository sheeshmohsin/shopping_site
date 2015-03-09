from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^add/$', 'cart.views.add'),
    url(r'^clear/$', 'cart.views.clear'),
    url(r'^show/$', 'cart.views.show'),
    url(r'^remove/(?P<pk>\d+)/$', 'cart.views.remove'),
    url(r'^checkout/$', 'cart.views.checkout'),
)

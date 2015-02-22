from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from explore import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'explore.views.home'),
    # url(r'^$', views.HomeView.as_view()),
    # url(r'^item/(?P<pk>\d+)/$', 'explore.views.item'),
    # url(r'^feedback/$', 'explore.views.feedback'),
    url(r'^main/', include('explore.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),	
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

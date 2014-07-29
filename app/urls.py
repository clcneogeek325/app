from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^personal/', include('apps.personal.urls')),
    url(r'^', include('apps.home.urls')),
    url(r'^productos/', include('apps.producto.urls')),
    url(r'^ws/', include('apps.webServices.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

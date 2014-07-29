from django.conf.urls import patterns, url, include


urlpatterns = patterns('apps.home.views',
	url(r'^$', 'view_index', name='home'),
	)

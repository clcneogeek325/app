from django.conf.urls import patterns, url, include


urlpatterns = patterns('apps.webServices.views',
	(r'^ws/Productos/$', 'wsProductos'),
	)

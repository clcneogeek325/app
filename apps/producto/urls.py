from django.conf.urls import patterns, url, include


urlpatterns = patterns('apps.producto.views',
	url(r'^$', 'view_lista', name='productos'),
	url(r'^add/$', 'view_add', name='agregar_producto'),
	url(r'^edit/(?P<id>.*)/$', 'view_edit', name='editar_producto'),
	url(r'^del/(?P<id>.*)/$', 'view_del', name='eliminar_producto'),
	

	)

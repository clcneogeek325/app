from django.conf.urls import patterns, url, include


urlpatterns = patterns('apps.personal.views',
	url(r'^$', 'view_index', name='personal'),
	url(r'^login/$', 'view_login', name='vista_login'),
	url(r'^logout/$', 'view_logout', name='vista_logout'),
	url(r'^add/user/$', 'view_add_user', name='vista_agregar_usuario'),
	url(r'^del/user/(?P<id>.*)/$', 'view_del_user', name='vista_del_usuario'),
	url(r'^edit/user/(?P<id>.*)/password/', 'view_edit_passwd', name='vista_edit_passwd'),
	url(r'^edit/user/(?P<id>.*)/$', 'view_edit_user', name='vista_edit_usuario'),
	)

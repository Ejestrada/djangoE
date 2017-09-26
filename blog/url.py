from django.conf.urls import include, url
from . import views

urlpatterns = [
<<<<<<< HEAD
 url(r'^$', views.listar_pub,name='listar_pub'),
    url(r'^postea/(?P<pk>[0-9]+)/$', views.detalle_pub,name='postea'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
=======
url(r'^$', views.listar_pub,name='listar_pub' ),
url(r'^postea/(?P<pk>[0-9]+)/$', views.detalle_pub,name='detalle_pub'),
url(r'^post/new/$', views.post_new, name='post_new'),
url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
>>>>>>> 54824ed86cea78e288af450baaf3fa34baba44e0


]

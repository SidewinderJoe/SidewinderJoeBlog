from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.posts, name='posts'),
	url(r'^(?P<slug>[-\w]+)/$', views.entry, name='entry'),
    #url(r'^/posts/test$',views.entry),#
]
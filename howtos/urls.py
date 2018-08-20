from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.howtos, name='howtos'),
	url(r'^(?P<slug>[-\w]+)/$', views.entry, name='entry'),
]
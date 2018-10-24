# coding:utf8

from django.conf.urls import url
from .views import about_view, AboutView, AboutAdminView


urlpatterns = [
	# url(r'^$', about_view, name="index"),
	url(r'^$', AboutView.as_view(), name="index"),
	url(r'^(?P<post_secret_key>\w+)/$', AboutAdminView.as_view(), name="about_post_secret"),
]


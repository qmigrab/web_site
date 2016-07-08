from django.conf.urls import url
from blog.views import archive, index


urlpatterns = [
	url(r'^$', index),
	url(r'^(?P<blog_id>\d+)/$', archive),
]

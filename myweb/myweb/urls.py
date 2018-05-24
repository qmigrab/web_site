"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
	url(r'^', include('home.urls', namespace="yme_home")),
	url(r'^blog/', include('blog.urls', namespace="yme_blog")),
	url(r'^foto/', include('foto.urls', namespace="yme_foto")),
	url(r'^about/', include('about.urls', namespace="yme_about")),
	url(r'^label/', include('labels.urls', namespace="yme_label")),

	url(r'^admin/', admin.site.urls),
	url(r'ckeditor/', include('ckeditor_uploader.urls'))
]

if settings.DEBUG:
#	urlpatterns += [url(r'media/(?P<path>.*)$',
#						'django.views.static.serve',
#						{'document_root': settings.MEDIA_ROOT}), ]
	from django.conf.urls.static import static
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

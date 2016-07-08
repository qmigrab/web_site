from django.conf.urls import url
from .views import apply_view

urlpatterns = [
	url(r'^', apply_view, name="apply_view"),
]
from django.shortcuts import render
from django.views.generic import TemplateView
import os


# Create your views here.
class CHomeView(TemplateView):
	template_name = "home.html"

home_view = CHomeView.as_view()

from django.shortcuts import render
from labels.models import YmeLabel
from random import shuffle


# Create your views here.
def about_view(request):
	labels = list(YmeLabel.objects.current())
	shuffle(labels)
	return render(request, "about.html", context={"labels_list": labels})
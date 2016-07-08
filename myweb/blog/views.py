from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogsPost


# Create your views here.
def index(request):
	posts = BlogsPost.objects.all()
	t = loader.get_template('bloglist.html')
	c = Context({'posts': posts})
	return HttpResponse(t.render(c))


def archive(request, blog_id):
	# posts = BlogsPost.objects.all()
	p = BlogsPost.objects.get(pk=blog_id)
	t = loader.get_template('archive.html')
	# c = Context({'posts': posts})
	c = Context({'p': p})
	return HttpResponse(t.render(c))


from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse

from .models import CApply
from .forms import CApplyForm


# Create your views here.
class CApplyFormView(CreateView):
	model = CApply
	form_class = CApplyForm

	template_name = "apply_form.html"

	def get_success_url(self, instance=None):
		return reverse('apply_view')

apply_view = CApplyFormView.as_view()
from django.forms import ModelForm

from .models import CApply


class CApplyForm(ModelForm):

	class Meta:
		model = CApply
		fields = ('name', 'email', 'content')

	def save(self, commit=True):
		_apply = super(CApplyForm, self).save(commit=commit)
		return _apply
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class CApply(models.Model):
	name = models.CharField(_('Applicant'), max_length=60)
	email = models.EmailField(_('Email'), max_length=60)
	content = models.TextField(_('Content'))
	send_time = models.DateTimeField(_('Send'), auto_now_add=True)

	def __unicode__(self):
		return u'%s, %s' % (self.name, self.email)

	def clean(self):
		self.name = self.name.strip().title()
		self.email = self.email.strip().lower()
		self.content = self.content.strip()


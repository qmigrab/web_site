# coding:utf8

from django.conf import settings
from appconf import AppConf


class PostAppConf(AppConf):
	PAGINATE_BY = 2

	class Meta:
		prefix = "post"

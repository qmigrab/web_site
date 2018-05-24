# coding:utf8

import os
from django.conf import settings
from appconf import AppConf
from ConfigParser import ConfigParser

# basedir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(
#                            os.path.dirname(__file__)))))

class PostAppConf(AppConf):
#    PAGINATE_BY = ALL_CONFIG.get("POSTAPPCONF", "paginate")

    class Meta:
        prefix = "post"

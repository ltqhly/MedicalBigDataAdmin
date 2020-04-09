# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig as DJAppConfig
from django.utils.translation import ugettext_lazy as _


class AppConfig(DJAppConfig):
    """
    Set the app name to display in the background
    """
    name = 'DMD'
    verbose_name = _('01.DMD')

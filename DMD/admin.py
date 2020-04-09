# -*- coding:utf-8 -*-
import logging

from datetime import datetime
from datetime import date
from django.utils import timezone
from django.contrib import admin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext_lazy as _
from import_export.admin import ImportExportActionModelAdmin
from import_export.formats import base_formats
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionModelAdmin

import easy

from .models import *

try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text

logger = logging.getLogger(__name__)

from .resources import *


@admin.register(DMDActivityType)
class DMDActivityTypeAdmin(ImportExportActionModelAdmin):
    resource_class = DMDActivityTypeResource
    formats = [
        base_formats.CSV,
    ]
    fieldsets = (
        (
            None,
            {'fields': (
                'src_activity_type_code',
                'activity_type_nm_cn',
            )}

        ),
    )

    list_display = [
        'id',
        'src_activity_type_code',
        'activity_type_nm_cn',
    ]

    ordering = [
        'id',
    ]


@admin.register(DMDCity)
class DMDCityAdmin(ImportExportActionModelAdmin):
    resource_class = DMDCityResource
    formats = [
        base_formats.CSV,
    ]
    fieldsets = (
        (
            None,
            {'fields': (
                "city_cd",
                "city_e_name",
                "city_c_name",
                "city_tier",
                "province_cd",
                "valid_flg",
            )}

        ),
    )

    list_display = [
        'id',
        "city_cd",
        "city_e_name",
        "city_c_name",
        "city_tier",
        "province_cd",
        "valid_flg"
    ]

    ordering = [
        'id',
    ]



@admin.register(DMDCoachvvaL2Capability)
class DMDCoachvvaL2CapabilityAdmin(ImportExportActionModelAdmin):
    resource_class = DMDCoachvvaL2CapabilityResource
    formats = [
        base_formats.CSV,
    ]
    fieldsets = (
        (
            None,
            {'fields': (
                "l2_capability_cd",
                "l2_capability_c_name",
                "l2_capability_e_name",
                "l2_capability_orderidx",
                "l2_capability_type"
            )}

        ),
    )

    list_display = [
        'id',
        "l2_capability_cd",
        "l2_capability_c_name",
        "l2_capability_e_name",
        "l2_capability_orderidx",
        "l2_capability_type"
    ]

    ordering = [
        'id',
    ]

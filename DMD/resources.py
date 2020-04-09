# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.contrib import admin
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from import_export import resources
from import_export.fields import Field

from .models import *


class DMDActivityTypeResource(resources.ModelResource):
    class Meta:
        model = DMDActivityType
        import_id_fields = [
            'src_activity_type_code',
        ]
        fields = (
            'src_activity_type_code',
            'activity_type_nm_cn',
        )
        export_order = [
            'src_activity_type_code',
            'activity_type_nm_cn',
        ]
        skip_unchanged = True

    def import_data(self, dataset, dry_run=False, raise_errors=False, use_transactions=None, collect_failed_rows=False,
                    **kwargs):
        return super(DMDActivityTypeResource, self).import_data(dataset, dry_run, raise_errors, use_transactions,
                                                                collect_failed_rows, **kwargs)


class DMDCityResource(resources.ModelResource):
    class Meta:
        model = DMDCity
        import_id_fields = [
            "city_cd",
        ]
        fields = (
            "city_cd",
            "city_e_name",
            "city_c_name",
            "city_tier",
            "province_cd",
            "valid_flg",
        )
        export_order = [
            "city_cd",
            "city_e_name",
            "city_c_name",
            "city_tier",
            "province_cd",
            "valid_flg",
        ]
        skip_unchanged = True

    def import_data(self, dataset, dry_run=False, raise_errors=False, use_transactions=None, collect_failed_rows=False,
                    **kwargs):
        return super(DMDCityResource, self).import_data(dataset, dry_run, raise_errors, use_transactions,
                                                        collect_failed_rows, **kwargs)


class DMDCoachvvaL2CapabilityResource(resources.ModelResource):
    class Meta:
        model = DMDCoachvvaL2Capability
        import_id_fields = [
            "l2_capability_cd",
        ]
        fields = (
            "l2_capability_cd",
            "l2_capability_c_name",
            "l2_capability_e_name",
            "l2_capability_orderidx",
            "l2_capability_type"
        )
        export_order = [
            "l2_capability_cd",
            "l2_capability_c_name",
            "l2_capability_e_name",
            "l2_capability_orderidx",
            "l2_capability_type"
        ]
        skip_unchanged = True

    def import_data(self, dataset, dry_run=False, raise_errors=False, use_transactions=None, collect_failed_rows=False,
                    **kwargs):
        return super(DMDCoachvvaL2CapabilityResource, self).import_data(dataset, dry_run, raise_errors,
                                                                        use_transactions,
                                                                        collect_failed_rows, **kwargs)

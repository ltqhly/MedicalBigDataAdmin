from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from . import utils
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class DMDActivityType(models.Model):
    """

    """
    id = models.CharField(primary_key=True, db_index=True, max_length=60, default=utils.get_uid, editable=False)
    src_activity_type_code = models.CharField(verbose_name=_("DMDActivityType.src activity type code"), max_length=40,
                                              blank=False, null=False,
                                              default="")
    activity_type_nm_cn = models.CharField(verbose_name=_("DMDActivityType.activity type nm cn"), max_length=40,
                                           blank=False,
                                           null=False, default="")
    updated = models.DateTimeField(verbose_name=_("DMDActivityType.updated"), auto_now=True)
    created = models.DateTimeField(verbose_name=_("DMDActivityType.created"), auto_now_add=True)

    class Meta:
        verbose_name = _("DMDActivityType")
        verbose_name_plural = _("DMDActivityType")

    def __str__(self):
        return u"{}".format(self.id)


@python_2_unicode_compatible
class DMDCity(models.Model):
    """
    DMD_City
    """
    id = models.CharField(primary_key=True, db_index=True, max_length=60, default=utils.get_uid, editable=False)
    city_cd = models.CharField(verbose_name=_("DMDCity.city cd"), max_length=40,
                               blank=False, null=False,
                               default="")
    city_e_name = models.CharField(verbose_name=_("DMDCity.city e name"), max_length=40,
                                   blank=False,
                                   null=False, default="")
    city_c_name = models.CharField(verbose_name=_("DMDCity.city c name"), max_length=40,
                                   blank=False,
                                   null=False, default="")
    city_tier = models.CharField(verbose_name=_("DMDCity.city tier"), max_length=40,
                                 blank=False,
                                 null=False, default="")
    province_cd = models.CharField(verbose_name=_("DMDCity.province cd"), max_length=40,
                                   blank=False,
                                   null=False, default="")
    valid_flg = models.CharField(verbose_name=_("DMDCity.valid flg"), max_length=40,
                                 blank=False,
                                 null=False, default="")
    updated = models.DateTimeField(verbose_name=_("DMDCity.updated"), auto_now=True)
    created = models.DateTimeField(verbose_name=_("DMDCity.created"), auto_now_add=True)

    class Meta:
        verbose_name = _("DMDCity")
        verbose_name_plural = _("DMDCity")

    def __str__(self):
        return u"{}".format(self.id)


@python_2_unicode_compatible
class DMDCoachvvaL2Capability(models.Model):
    """
    DMD_Coachvva_L2Capability
    """
    id = models.CharField(primary_key=True, db_index=True, max_length=60, default=utils.get_uid, editable=False)
    l2_capability_cd = models.CharField(verbose_name=_("DMDCoachvvaL2Capability.l2 capability cd"), max_length=100,
                                        blank=False, null=False,
                                        default="")
    l2_capability_c_name = models.CharField(verbose_name=_("DMDCoachvvaL2Capability.l2 capability c name"),
                                            max_length=100,
                                            blank=False,
                                            null=False, default="")
    l2_capability_e_name = models.CharField(verbose_name=_("DMDCoachvvaL2Capability.l2 capability e name"),
                                            max_length=100,
                                            blank=False,
                                            null=False, default="")
    l2_capability_orderidx = models.CharField(verbose_name=_("DMDCoachvvaL2Capability.l2 capability orderidx"),
                                              max_length=100,
                                              blank=False,
                                              null=False, default="")
    l2_capability_type = models.CharField(verbose_name=_("DMDCoachvvaL2Capability.l2 capability type"), max_length=100,
                                          blank=False,
                                          null=False, default="")
    updated = models.DateTimeField(verbose_name=_("DMDCoachvvaL2Capability.updated"), auto_now=True)
    created = models.DateTimeField(verbose_name=_("DMDCoachvvaL2Capability.created"), auto_now_add=True)

    class Meta:
        verbose_name = _("DMDCoachvvaL2Capability")
        verbose_name_plural = _("DMDCoachvvaL2Capability")

    def __str__(self):
        return u"{}".format(self.id)

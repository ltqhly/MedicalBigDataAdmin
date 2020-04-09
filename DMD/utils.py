# -*- coding:utf-8 -*-
import uuid
import logging

logger = logging.getLogger(__name__)


def get_uid():
    return uuid.uuid4().hex

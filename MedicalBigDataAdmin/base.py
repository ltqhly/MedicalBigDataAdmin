#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import re
import base64
import json
import datetime
import traceback
import platform
from collections import defaultdict

# 通常你不应该从django引入任何代码, 但ImproperlyConfigured是个例外
from django.core.exceptions import ImproperlyConfigured

__all__ = [
    'PWD',
    'PROJECT_DIR',
    'BASE_DIR',
    'APP',
    'LOG_FILE',
    'API_LOG_FILE',
    'API__OFFLINE_LOG_FILE',
    'API_LOG_DIR',
    'is_prod',
    'is_test',
    'is_dev',
    'is_ab',
    'is_demo',
    'get_version',
    'get_full_version',
]

PWD = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(PWD)
BASE_DIR = os.path.dirname(PROJECT_DIR)
APP = os.path.basename(PROJECT_DIR)
LOG_FILE = os.path.abspath(os.path.join(BASE_DIR, "%s.log" % (APP,)))
API_LOG_DIR = os.path.abspath(os.path.join(BASE_DIR, "api_log"))
API_LOG_FILE = os.path.abspath(os.path.join(API_LOG_DIR, "api.log"))
API__OFFLINE_LOG_FILE = os.path.abspath(os.path.join(API_LOG_DIR, "api_offline.log"))
VERSION_FILE = os.path.join(BASE_DIR, "version")

# DEFAULT_ENVIRONMENT = "prod"
# DEFAULT_ENVIRONMENT = "test"
DEFAULT_ENVIRONMENT = "dev"
DEFAULT_VERSION = "1.0.0"
PY_VERSION = platform.python_version()[:3]
os.environ.setdefault("PROJECT_ENVIRONMENT", DEFAULT_ENVIRONMENT)
os.environ.setdefault("PROJECT_VERSION", DEFAULT_VERSION)

sys.path.insert(0, os.path.join(BASE_DIR, "libs"))
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
sys.path.append("/usr/lib/python{}/dist-packages".format(PY_VERSION))
sys.path.append("/usr/local/lib/python{}/dist-packages".format(PY_VERSION))
sys.path.append("/Library/Python/{}/site-packages".format(PY_VERSION))


def get_environment(default=DEFAULT_ENVIRONMENT):
    try:
        env = get_env_variable("PROJECT_ENVIRONMENT", default)
        # print u"PROJECT_ENVIRONMENT:{} default:{}".format(env, default)
        return str(env)
    except ImproperlyConfigured as e:
        traceback.print_exc()
        return default


def get_env_variable(var_name, default=None):
    try:
        return os.environ.get(var_name, default)
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


ENVIRONMENT = get_environment()


def is_prod():
    return ENVIRONMENT in ["p", "pro", "prod", "production", ]


def is_test():
    return ENVIRONMENT in ["t", "test", ]


def is_dev():
    return ENVIRONMENT in ["d", "dev", ]


def is_ab():
    return ENVIRONMENT in ["a", "ab", ]


def is_demo():
    return ENVIRONMENT in ["demo", ]


_version = None


def get_version(default=DEFAULT_VERSION):
    global _version
    if _version:
        return _version
    if os.path.isfile(VERSION_FILE):
        _version = open(VERSION_FILE, 'rb').read()
        _version = _version.strip()
    if not _version:
        _version = get_env_variable("PROJECT_VERSION", default)
    return _version


def get_full_version(default=DEFAULT_VERSION):
    v = get_version(default)
    env = ENVIRONMENT.upper()
    return u"{version} {env}".format(version=v, env=env)


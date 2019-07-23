#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
from functools import wraps
import inspect

def initializer(func):
    """
    Automatically assigns the parameters.
    >>> class process:
    ...     @initializer
    ...     def __init__(self, cmd, reachable=False, user='root'):
    ...         pass
    >>> p = process('halt', True)
    >>> p.cmd, p.reachable, p.user
    ('halt', True, 'root')
    """
    names, varargs, keywords, defaults = inspect.getargspec(func)
    @wraps(func)
    def wrapper(self, *args, **kargs):
        for name, arg in list(zip(names[1:], args)) + list(kargs.items()):
            setattr(self, name, arg)
        for name, default in zip(reversed(names), reversed(defaults)):
            if not hasattr(self, name):
                setattr(self, name, default)
        func(self, *args, **kargs)
    return wrapper

class Config(object):
    APP_TITLE = 'Sample Flask-Restful-API-Vue-D3 Application'
    APP_VERSION = 'v0.1'
    APP_DESCRIPTION = '''put App Description Here'''
    API_VERSION = 0.1
    API_TITLE = 'API Entry Points'
    API_DEFAULT = 'METHODS OF API'
    API_DEFAULT_LABEL = 'CLICK TO EXPAND'
    API_DESCRIPTION = 'DESCRIPTIONS OF API'
    BIND_IP = 'localhost'
    BIND_PORT = 8555
    ERRORS = {}
    ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
    LOCAL_RESPONSE_DIR = os.path.abspath(os.path.dirname(__file__)) + '/local_response'
    INDEX_URL = '/index'
    API_NAME = 'apiModule'
    API_URL = '/apiModule'
    @initializer
    def __init__(self, APP_TITLE, APP_VERSION, APP_DESCRIPTION, API_DEFAULT_LABEL, BIND_IP, BIND_PORT, ERRORS, ROOT_DIR, LOCAL_RESPONSE_DIR):
        pass


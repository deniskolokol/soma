# -*- coding: utf-8 -*-

import re
import time
import random
import logging
import collections
from string import ascii_lowercase, digits


CONSOLE = logging.getLogger("commands")


class RecordDict(dict):
    """
    Dictionary that acts like a class with keys accessed as attributes.
    `inst['foo']` and `inst.foo` is the same.
    """
    def __init__(self, **kwargs):
        super(RecordDict, self).__init__(**kwargs)
        self.__dict__ = self

    def exclude(self, *args):
        for key in args:
            del self[key]
        return self

    @classmethod
    def from_list(cls, container, key, val):
        kwargs = dict((s[key], s[val]) for s in container)
        return cls(**kwargs)


def rand_string(size):
    """Generates quazi-unique sequence from random digits and letters."""
    return ''.join(random.choice(ascii_lowercase+digits) for x in range(size))


def rand_digits(size):
    """Generates quazi-unique sequence from random digits."""
    return ''.join(random.choice(digits) for x in range(size))


def timeit(method):
    """Profiling decorator, measures function runing time."""
    def timeit_wrapper(*args, **kwargs):
        time_started = time.time()
        result = method(*args, **kwargs)
        time_ended = time.time()
        time_sec = time_ended - time_started
        CONSOLE.debug('%s\t%2.2fmin\t%2.8fs\t%sms' % (
            method.__name__,
            time_sec / 60,
            time_sec,
            time_sec * 1000))
        return result
    return timeit_wrapper


def deep_update(source, overrides):
    """
    Updates a nested dictionary or similar mapping.
    Modifies `source` in place.
    """
    for key, value in overrides.iteritems():
        if isinstance(value, collections.Mapping) and value:
            returned = deep_update(source.get(key, {}), value)
            source[key] = returned
        else:
            source[key] = overrides[key]
    return source


def split_text(text, **kwargs):
    """
    Splits text by either spaces and \n, or by kwargs['pattern'].
    """
    pattern = kwargs.get("pattern", None)
    if pattern is None:
        pattern = r'\s+|\n+'
    return [x.strip() for x in re.split(pattern, text) if x != '']


def extract_hashtags(text):
    return re.findall(r"#(\w+)", text)


def admin_method_attrs(**outer_kwargs):
    """
    Wrap an admin method with passed arguments as attributes and values
    (for common admin manipulation such as setting short_description, etc.)
    """
    def method_decorator(func):
        for kw, arg in outer_kwargs.items():
            setattr(func, kw, arg)
        return func
    return method_decorator


def shorten_string(val, num=100):
    if val:
        if len(val) > num:
            return val[:num] + "..."
    return val

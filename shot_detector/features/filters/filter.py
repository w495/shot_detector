# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

import logging

import six

from .base_nested_filter import BaseNestedFilter


class Filter(BaseNestedFilter):
    """
        Basic feature filter
    """
    __logger = logging.getLogger(__name__)

    def __init__(self, **kwargs):
        super(Filter, self).__init__(**kwargs)
        for attr, value in six.iteritems(kwargs):
            setattr(self, attr, value)

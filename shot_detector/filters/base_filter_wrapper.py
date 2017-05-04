# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

import logging
from functools import wraps

from shot_detector.utils.log_meta import LogMeta


class BaseFilterWrapper(LogMeta):
    __logger = logging.getLogger(__name__)
    __update_kwargs_func_name = (
        '__init__',
        '__call__',
        'filter_objects',
        'filter_features',
        'filter_feature_item',
    )
    __info_log_func_name = (
        # 'filter_features',
        # 'filter_objects',
    )

    @classmethod
    def log_as_info(mcs, class_name, func, func_name):
        if not hasattr(func, 'call_number_dict'):
            func.call_number_dict = {}
        if not func.call_number_dict.get(class_name):
            func.call_number_dict[class_name] = 0

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            mcs.__logger.debug('{} {} ({})'.format(
                func_name,
                type(self).__name__,
                func.call_number_dict.get(class_name)
            ))
            res = func(self, *args, **kwargs)
            func.call_number_dict[class_name] += 1
            return res

        return wrapper

    # noinspection PyUnusedLocal
    @classmethod
    def update_kwargs(mcs, _class_name, func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            updated_kwargs = self.handle_options(kwargs)
            res = func(self, *args, **updated_kwargs)
            return res

        return wrapper

    # noinspection PyUnusedLocal
    def __new__(mcs, class_name=None, bases=None, attr_dict=None, **_):
        for func_name in mcs.__update_kwargs_func_name:
            func = attr_dict.get(func_name)
            if func:
                attr_dict[func_name] = mcs.update_kwargs(
                    class_name,
                    func
                )
        for func_name in mcs.__info_log_func_name:
            func = attr_dict.get(func_name)
            if func:
                attr_dict[func_name] = mcs.log_as_info(
                    class_name,
                    func,
                    func_name
                )

        return super(BaseFilterWrapper, mcs).__new__(mcs, class_name,
                                                     bases, attr_dict)

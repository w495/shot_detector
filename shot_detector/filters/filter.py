# -*- coding: utf8 -*-
"""
    This is part of shot detector.
    Produced by w495 at 2017.05.04 04:18:27
"""


from __future__ import absolute_import, division, print_function

import collections
import logging
import operator

import six
from past.utils import old_div

from .base_nested_filter import BaseNestedFilter


class Filter(BaseNestedFilter):
    """
        Basic feature filter
    """
    __logger = logging.getLogger(__name__)

    def __init__(self, filter=None, **kwargs):
        super(Filter, self).__init__(**kwargs)

        if filter:
            for attr, value in six.iteritems(vars(filter)):
                setattr(self, attr, value)

        for attr, value in six.iteritems(kwargs):
            setattr(self, attr, value)

    def sequential(self, other):
        """

        :param other:
        :return:
        """
        from .filter_cast_features import FilterCastFeatures

        #
        # if (    isinstance(other, types.BuiltinFunctionType)
        #         or (
        #             type(other).__name__  == 'type'
        #             and other.__name__ in ('int', 'float')
        #         )
        # ):

        if not isinstance(other, Filter):
            other = FilterCastFeatures(
                cast=other,
            )
        return Filter(
            sequential_filters=[
                self, other
            ],
        )

    def apply_operator_left(self, other, op):
        """
        
        :param other: 
        :param op: 
        :return: 
        """
        return self.apply_operator(other, op, is_right=False)

    def apply_operator_right(self, other, op):
        """
        
        :param other: 
        :param op: 
        :return: 
        """
        return self.apply_operator(other, op, is_right=True)

    def apply_operator(self, other, op, is_right=False):
        """
        
        :param other: 
        :param op: 
        :param is_right: 
        :return: 
        """

        from .filter_operator import FilterOperator

        debug_dict = dict(
            action=dict(
                a_name=type(self).__name__,
                b_name=type(other).__name__,
                op_name=type(op).__name__,
            ),
            options=self._options
        )

        if not isinstance(other, Filter):
            other = self.scalar_to_filter(
                value=other,
            )

        return FilterOperator(
            parallel_filters=[self, other],
            operator=op,
            is_right=is_right,
            __debug_dict=debug_dict
        )

    def to_filter(self, value):
        """
        
        :param value: 
        :return: 
        """
        if isinstance(value, collections.Iterable):
            return self.seq_to_filter(value)
        return self.scalar_to_filter(value)

    @staticmethod
    def seq_to_filter(value):
        """
        
        :param value: 
        :return: 
        """
        from .filter_cast_seq_value import FilterCastSeqValue
        return FilterCastSeqValue(seq=value)

    @staticmethod
    def scalar_to_filter(value):
        """
        
        :param value: 
        :return: 
        """
        from .filter_cast_scalar_value import FilterCastScalarValue
        return FilterCastScalarValue(value=value)

    def i(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        return self.intersect(*args, **kwargs)

    def intersect(self, other, threshold=0):
        """

        :param other:
        :param threshold:
        :return:
        """
        from .filter_intersection import FilterIntersection

        return FilterIntersection(
            parallel_filters=[self, other],
            threshold=threshold
        )

    def __add__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator_left(
            other,
            operator.add
        )

    def __radd__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator_right(
            other,
            operator.add
        )

    def __sub__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator_left(other, operator.sub)

    def __rsub__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator_right(other, operator.sub)

    def __mul__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator_left(other, operator.mul)

    def __rmul__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator_right(other, operator.mul)

    def __truediv__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator_left(other, operator.truediv)

    def __rtruediv__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator_right(other, operator.truediv)

    def __div__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator_left(other, old_div)

    def __rdiv__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator_right(other, operator.floordiv)

    def __floordiv__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator_left(other, operator.floordiv)

    def __rfloordiv__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator_left(other, operator.floordiv)

    def __pow__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator(other, operator.pow)

    def __rpow__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator(other, operator.pow)

    def __contains__(self, item):
        """
        :param Filter item:
        :return:
        """
        return self.intersect(item)

    def __or__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.sequential(other)

    def __ror__(self, other):
        """
        :param Filter other:
        :return:
        """

        return self.sequential(other)

    def join(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator(
            other,
            Filter.tuple_op
        )

    @classmethod
    def tuple(cls, first, second):
        """
        :param Filter first:
        :param Filter second:
        :return:
        """
        return first.join(second)

    @classmethod
    def tuple_op(cls, a, b):
        """
        
        :param a: 
        :param b: 
        :return: 
        """
        return a, b

    def __eq__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator(other, operator.eq)

    def __ne__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator(other, operator.ne)

    def __le__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator(other, operator.le)

    def __ge__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator(other, operator.ge)

    def __lt__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator(other, operator.lt)

    def __gt__(self, other):
        """
        :param Filter other:
        :return:
        """
        return self.apply_operator(other, operator.gt)


    @staticmethod
    def para(cls, *args, **kwargs):
        filter = cls(para=True)
        return filter


    @staticmethod
    def bulk(reducer, filters=None, *args):
        from .bulk_filter import BulkFilter
        if filters is None:
            filters = list()
        filters = list(filters)
        filters += args

        filter = BulkFilter(
            reducer=reducer,
            parallel_filters=filters
        )
        return filter

    @classmethod
    def sum(cls, filters=None, *args):
        filter = cls.bulk(sum, filters, *args)
        return filter

    @classmethod
    def min(cls, filters=None, *args):
        filter = cls.bulk(min, filters, *args)
        return filter

    @classmethod
    def max(cls, filters=None, *args):
        filter = cls.bulk(max,  filters, *args)
        return filter

    @classmethod
    def sub(cls, filters=None, *args):
        filter = cls.bulk(operator.sub,  filters, *args)
        return filter


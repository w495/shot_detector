# -*- coding: utf8 -*-
"""
    This is part of shot detector.
    Produced by w495 at 2017.05.04 04:18:27
"""

from __future__ import absolute_import, division, print_function

from shot_detector.utils import Qtext


class PlotOptions(object):
    """
        ...
    """

    __slots__ = [
        'fmt',
        'style',
        'label',
        'color',
        'width',
        'marker',
    ]

    def __init__(self,
                 *_,
                 label=None,
                 label_fmt=None,
                 fmt=None,
                 style=None,
                 color=None,
                 width=None,
                 marker=None):
        """
        
        :param str fmt: 
        :param str or tuple style:
        :param str color: 
        :param float width: 
        :param str marker: 
        :param str or Qtext or Qtex label: 
        :param dict label_format: 
        """

        self.fmt = fmt
        if not self.fmt:
            self.fmt = str()
        self.style = style
        self.width = width
        self.color = color
        self.marker = marker

        self.label = None
        if label:
            self.label = str(label)
        if label and label_fmt:
            qtext = Qtext(label, **label_fmt)
            self.label = str(qtext)

    def __repr__(self):
        return self.label

    def __hash__(self):
        return hash(self.label)
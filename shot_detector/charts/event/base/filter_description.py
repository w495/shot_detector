# -*- coding: utf8 -*-
"""
    This is part of shot detector.
    Produced by w495 at 2017.05.04 04:18:27
"""

from __future__ import absolute_import, division, print_function

import uuid

from shot_detector.charts.plot import PlotOptions


class FilterDescription(object):
    """
        ...
    """

    def __init__(self,
                 name=None,
                 formula=None,
                 plot_options=None,
                 offset=None):
        """
        
        :param str or Qtext or Qtex name: 
        :param Filter formula: 
        :param PlotOptions plot_options: 
        :param float offset: 
        """



        self.formula = formula

        self.plot_options = plot_options
        if not plot_options:
            self.plot_options = PlotOptions()

        self.name = str(name)
        if not name:
            self.name = str(uuid.uuid4())

        self.offset = offset
        if not offset:
            self.offset = 0

    def __repr__(self):
        return "<Filter: {name}>".format(name=self.name)

    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        return self.name == other.name
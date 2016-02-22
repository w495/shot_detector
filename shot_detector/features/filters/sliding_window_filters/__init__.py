# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

from .alpha_beta_swfilter import AlphaBetaSWFilter
from .base_combination_swfilter import BaseCombinationSWFilter
from .base_swfilter import BaseSWFilter
from .bspline_swfilter import BsplineSWFilter
from .dct_coef_swfilter import DCTCoefSWFilter
from .dct_linear_regressor_swfilter import DCTLinearRegressorSWFilter
from .dct_regressor_swfilter import DCTRegressorSWFilter
from .decision_tree_regressor_swfilter import DecisionTreeRegressorSWFilter
from .deviation_difference_swfilter import DeviationDifferenceSWFilter
from .deviation_swfilter import DeviationSWFilter
from .difference_swfilter import DifferenceSWFilter
from .extrema_swfilter import ExtremaSWFilter
from .hist_simple_swfilter import HistSimpleSWFilter
from .level_swfilter import LevelSWFilter
from .max_swfilter import MaxSWFilter
from .mean_swfilter import MeanSWFilter
from .median_swfilter import MedianSWFilter
from .min_swfilter import MinSWFilter
from .scale_swfilter import ScaleSWFilter
from .shift_swfilter import ShiftSWFilter
from .std_swfilter import StdSWFilter
from .std_error_swfilter import StdErrorSWFilter
from .zscore_swfilter import ZScoreSWFilter
from .zscore_zero_swfilter import ZScoreZeroSWFilter
from .pearson_correlation_swfilter import PearsonCorrelationSWFilter

from .min_std_mean_swfilter import MinStdMeanSWFilter



from .wiener_swfilter import WienerSWFilter
from .savitzky_golay_swfilter import SavitzkyGolaySWFilter

from .nikitin_swfilter import NikitinSWFilter

from .detrend_swfilter import DetrendSWFilter

from .scipy_stat_swfilter import SciPyStatSWFilter
from .kurtosis_swfilter import KurtosisSWFilter
from .skewness_swfilter import SkewnessSWFilter
from .variance_swfilter import VarianceSWFilter



from .normal_test_swfilter import NormalTestSWFilter
from .independent_studentt_test_swfilter import TTestIndSWFilter
from .dependent_student_t_test_swfilter import IndependentStudentTtestSWFilter
from .wilcoxon_rank_sum_swfilter import WilcoxonRankSumSWFilter



from .debug_grid_swfilter import DebugGridSWFilter
from .debug_swfilter import DebugSWFilter







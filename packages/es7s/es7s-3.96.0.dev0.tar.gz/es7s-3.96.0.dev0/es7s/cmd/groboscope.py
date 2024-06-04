# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2024 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------

from ._adaptive_input import _AdaptiveInputAction
from ._base import _BaseAction


class action(_AdaptiveInputAction, _BaseAction):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

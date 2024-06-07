import logging

import pandas as pd

from cumulative.transforms.transform import Transform

log = logging.getLogger(__name__)


class ScaleWarning(UserWarning):
    pass


class ExceptionScaler(Exception):
    pass


class Apply(Transform):
    def transform_row(self, row, src, func=None):

        s = pd.Series(row[f"{src}.y"], index=row[f"{src}.x"], copy=True)
        s = func(s)

        attrs = {
            "x": s.index.values,
            "y": s.values,
        }

        return pd.Series(attrs)

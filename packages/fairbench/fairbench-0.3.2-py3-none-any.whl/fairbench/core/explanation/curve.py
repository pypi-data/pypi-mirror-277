import numpy as np
from scipy import interpolate


class ExplanationCurve:
    def __init__(self, x, y, name="Curve"):
        assert isinstance(x, np.ndarray)
        assert isinstance(y, np.ndarray)
        self.x = x
        self.y = y
        self.name = name
        assert x.shape == y.shape

    def togrid(self, grid):
        new_x = np.linspace(self.x.min(), self.x.max(), num=grid)
        approx = interpolate.interp1d(x=self.x, y=self.y)
        return ExplanationCurve(new_x, approx(new_x))

    @property
    def points(self):
        return self.x.shape[0]

    def __str__(self):
        return f"{self.name} ({self.points} points)"

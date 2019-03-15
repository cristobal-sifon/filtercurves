from astropy.io import ascii, fits
import numpy as np
import os

from . import __path__


class Filter:

    def __init__(self, name):
        self.name = name
        self.path = os.path.join(__path__, name)
        self.wave, self.curve = self._load()

    def _load(self):
        return np.loadtxt(self.path, usecols=[0,1], unpack=True)


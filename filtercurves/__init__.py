import os

from .core import *


__path__ = os.path.split(__file__)[0]
__version__ = '0.0.1b'

available = sorted(os.listdir(os.path.join(__path__, 'data')))


from typing import Union
from utilityx.data.source.source import Source

class Predictor:
    def __init__(self, source:Source):
        self._source = source
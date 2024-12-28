"""Needed classes for implementing the Iterable interface for different types of objects."""

import os.path

# TODO: It's very likely that the same Iterable implementation doesn't fit
# for the 3 needed types. It is valid to implement 3 different classes implementing
# the same interface and use an object from different implementations when needed.


class Iterable():
    """Skeleton for an Iterable implementation."""
    def next(self):
        while True:
            self._nextId=self._nextId+1
            contador=("000000000"+str(self._nextId))[-8:]
            path='./datos/'+contador
            if not os.path.isfile(path):
                if contador =='00200000':
                    self.netId=0
                    contador='00000000'
                break
        return contador

    def __init__(self):
        self._nextId = 0



"""Needed classes to implement and serve the RSet type."""

from typing import Optional
import pickle
import os.path
from remotetypes.customset import StringSet
from remotetypes.iterable import Iterable

class RemoteSet():
    """Implementation of the remote interface RSet."""

    def __init__(self, identifier) -> None:
        """Initialise a RemoteSet with an empty StringSet."""
        self.id_ = identifier
        self._storage_ = StringSet(identifier)
        self.iter=("000000000"+str(self.id_))[-8:]
        self.retorno=False
        self.fecha=0.0
        self._iteratio = Iterable()
        self.path='./datos/'+self.iter
        if os.path.isfile(self.path):
            self.loadtofile()
            self.fecha=os.path.getmtime(self.path)

    def savetofile(self):
        print ('Save a set to a file with id ',self.iter)
        fechact=float(-1)
        if os.path.isfile(self.path):
            fechact=os.path.getmtime(self.path)
        if fechact > self.fecha:
            self.iter=self._iteratio.next()
        with open('./datos/'+self.iter, 'wb') as f:
            pickle.dump(set(self._storage_), f)

    def loadtofile(self):
        with open('./datos/'+self.iter, 'rb') as f:
            loaded_set = pickle.load(f)
        print(loaded_set)
        for i in loaded_set:
            self._storage_.add(i)

    def identifier(self):
        """Return the identifier of the object."""
        return self.id_

    def remove(self, item: str):
        """Remove an item from the StringSet if added. Else, raise a remote exception."""
        if self.contains(item) == True:
            try:
                self._storage_.remove(item)
            except:
                print("Error remove")    

    def length(self):
        """Return the number of elements in the StringSet."""
        return len(self._storage_)

    def contains(self, item: str):
        """Check the pertenence of an item to the StringSet."""
        return item in self._storage_

    def hash(self):
        """Calculate a hash from the content of the internal StringSet."""
        contents = list(self._storage_)
        contents.sort()
        return hash(repr(contents))

    def iter(self):
        """Create an iterable object."""

    def add(self, item: str):
        """Add a new string to the StringSet."""
        if item =='88888888':
            self.retorno=True
        else:
            self._storage_.add(item)

    def pop(self):
        """Remove and return an element from the storage."""
        if self.retorno is True:
            self.retorno=False
            return str(self._storage_)
        if self.length() == 0:
            return
        try:
            return self._storage_.pop()
        except:
            print("Error pop")

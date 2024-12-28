"""Needed classes to implement and serve the RList type."""
from typing import Optional
import pickle
from remotetypes.customset import StringList
import os.path
from remotetypes.iterable import Iterable

class RemoteList():
    """Skelenton for the RList implementation."""
    """ Falta getItem y append"""

    def __init__(self, identifier):
        """Initialise a RemoteSet with an empty StringList."""
        self.id_ = identifier
        self._storage_ = StringList(identifier)
        self.iter=("000000000"+str(self.id_))[-8:]
        self.path='./datos/'+self.iter
        self.fecha=0.0
        self._iteratio = Iterable()
        if os.path.isfile(self.path):
            self.loadtofile()
            self.fecha=os.path.getmtime(self.path)

    def savetofile(self):
        print ('Save a list to a file with id ',self.iter)
        fechact=float(-1)
        if os.path.isfile(self.path):
            fechact=os.path.getmtime(self.path)
        if fechact > self.fecha:
            self.iter=self._iteratio.next()
        with open('./datos/'+self.iter, 'wb') as f:
            pickle.dump(list(self._storage_), f)

    def loadtofile(self):
        with open('./datos/'+self.iter, 'rb') as f:
            loaded_set = pickle.load(f)
        print(loaded_set)
        for i in loaded_set:
            self._storage_.append(i)

    def identifier(self):
        """Return the identifier of the object."""
        return self.id_

    def remove(self, item: str):
        """Remove an item from the StringList if added. Else, raise a remote exception."""
        if self.contains(item) == True:
            try:
                self._storage_.remove(item)
            except:
                print("Error remove")

    def getItem(self, item: int):
        """getItem and return an element from the storage."""
        try:
            return self._storage_.getItem(item)
        except:
            print("Error getItem")


    def length(self):
        """Return the number of elements in the StringList."""
        return len(self._storage_)

    def contains(self, item: str):
        """Check the pertenence of an item to the StringList."""
        return item in self._storage_

    def hash(self):
        """Calculate a hash from the content of the internal StringList."""
        contents = list(self._storage_)
        contents.sort()
        return hash(repr(contents))

    def iter(self):
        """Create an iterable object."""

    def append(self, item: str):
        """Add a new string to the StringList."""
        self._storage_.append(item)

    def pop(self, item: int):
        """Remove and return an element with item from the storage."""
        if item == 88888888:
            return str(self._storage_)
        if item < self.length():
            try:
                return self._storage_.pop(item)
            except:
                print("Error pop")


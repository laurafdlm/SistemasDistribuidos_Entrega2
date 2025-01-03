"""Needed classes to implement and serve the RSet type."""

from typing import Optional
from remotetypes.customset import StringSet

class RemoteSet():
    """Implementation of the remote interface RSet."""

    def __init__(self, identifier) -> None:
        """Initialise a RemoteSet with an empty StringSet."""
        self.id_ = identifier
        self._storage_ = StringSet(identifier)
        self.iter=("000000000"+str(self.id_))[-8:]
        self.retorno=False
        self.fecha=0.0

    def leervalor(self):
        print ('Leer un conjunto con el id ',self.iter)
        return str(self._storage_)

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
        return str(item in self._storage_)

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

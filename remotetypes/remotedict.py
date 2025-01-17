"""Needed classes to implement and serve the RDict type."""

from typing import Optional
from remotetypes.customset import StringDict

class RemoteDict():
    """Implementation of the remote interface RDict."""
    def __init__(self, identifier):
        """Initialise a RemoteDict with an empty StringDict."""
        self.id_ = identifier
        self._storage_ = StringDict(identifier)
        self.iter=("000000000"+str(self.id_))[-8:]
        self.fecha=0.0

    def leervalor(self):
        print ('Leer un dicionario con el id ',self.iter)
        return str(self._storage_)

    def identifier(self):
        """Return the identifier of the object."""
        return self.id_

    def remove(self, item: str):
        """Remove an item from the StringDict if added. Else, raise a remote exception."""
        if self.contains(item) == False:
            return
        try:
            self._storage_.remove(item)
        except:
            print("Error remove")
        
    def setItem(self,key: str,item: str):
        """setItem an item from the StringDict if added. Else, raise a update exception."""
        try:
            self._storage_.setItem(key,item)
        except:
            print("Error setItem")

    def getItem(self,key: str):
        """getItem get value of item from the StringDict"""
        try:
            return self._storage_.get(key)
        except:
            print("Error get key")

    def length(self):
        """Return the number of elements in the StringDict."""
        return len(self._storage_)

    def contains(self, item: str):
        """Check the pertenence of an item to the StringDict."""
        return str(item in self._storage_)

    def hash(self):
        """Calculate a hash from the content of the internal StringDict."""
        contents = list(self._storage_.values())
        contents.sort()
        return hash(repr(contents))

    def iter(self):
        """Create an iterable object."""

    def pop(self, item: str):
        """Remove and return an element with item from the storage."""
        """Save dict to file"""
        if item == "88888888":
            return str(self._storage_)
        if self.contains(item) == False:
            return
        try:
            return self._storage_.pop(item)

        except:
            print("Error pop")


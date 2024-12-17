"""Needed classes to implement and serve the RList type."""
from typing import Optional
import pickle
import Ice
import RemoteTypes as rt  # noqa: F401; pylint: disable=import-error
from remotetypes.customset import StringList
import os.path
from remotetypes.iterable import Iterable

class RemoteList(rt.RList):
    """Skelenton for the RList implementation."""
    """ Falta getItem y append"""

    def __init__(self, identifier) -> None:
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

    def identifier(self, current: Optional[Ice.Current] = None) -> str:
        """Return the identifier of the object."""
        return self.id_

    def remove(self, item: str, current: Optional[Ice.Current] = None) -> None:
        """Remove an item from the StringList if added. Else, raise a remote exception."""
        if self.contains(item) == True:
            try:
                self._storage_.remove(item)
            except KeyError as error:
                raise rt.KeyError(item) from error

    def getItem(self, item: int, current: Optional[Ice.Current] = None) -> str:
        """getItem and return an element from the storage."""
        try:
            return self._storage_.getItem(item)
        except KeyError as error:
            raise rt.KeyError(item) from error


    def length(self, current: Optional[Ice.Current] = None) -> int:
        """Return the number of elements in the StringList."""
        return len(self._storage_)

    def contains(self, item: str, current: Optional[Ice.Current] = None) -> bool:
        """Check the pertenence of an item to the StringList."""
        return item in self._storage_

    def hash(self, current: Optional[Ice.Current] = None) -> int:
        """Calculate a hash from the content of the internal StringList."""
        contents = list(self._storage_)
        contents.sort()
        return hash(repr(contents))

    def iter(self, current: Optional[Ice.Current] = None) -> rt.IterablePrx:
        """Create an iterable object."""

    def append(self, item: str, current: Optional[Ice.Current] = None) -> None:
        """Add a new string to the StringList."""
        self._storage_.append(item)

    def pop(self, item: int,current: Optional[Ice.Current] = None) -> str:
        """Remove and return an element with item from the storage."""
        if item == 99999999:
            self.savetofile()
            return self.iter
        if item == 88888888:
            return str(self._storage_)
        if item < self.length():
            try:
                return self._storage_.pop(item)
            except KeyError as exc:
                raise rt.KeyError() from exc


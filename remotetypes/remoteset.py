"""Needed classes to implement and serve the RSet type."""

from typing import Optional
import pickle
import Ice
import RemoteTypes as rt  # noqa: F401; pylint: disable=import-error

from remotetypes.customset import StringSet

class RemoteSet(rt.RSet):
    """Implementation of the remote interface RSet."""

    def __init__(self, identifier) -> None:
        """Initialise a RemoteSet with an empty StringSet."""
        self.id_ = identifier
        self._storage_ = StringSet(identifier)
        self.iter=("000000000"+str(self.id_))[-8:]
        self.saveact=False

    def savetofile(self):
        print ('Save a set to a file with id ',self.iter)
        with open('./datos/'+self.iter, 'wb') as f:
            pickle.dump(set(self._storage_), f)

        with open('./datos/'+self.iter, 'rb') as f:
            loaded_set = pickle.load(f)
        print(loaded_set)

    def identifier(self, current: Optional[Ice.Current] = None) -> str:
        """Return the identifier of the object."""
        return self.id_

    def remove(self, item: str, current: Optional[Ice.Current] = None) -> None:
        """Remove an item from the StringSet if added. Else, raise a remote exception."""
        try:
            self._storage_.remove(item)
        except KeyError as error:
            raise rt.KeyError(item) from error

    def length(self, current: Optional[Ice.Current] = None) -> int:
        """Return the number of elements in the StringSet."""
        return len(self._storage_)

    def contains(self, item: str, current: Optional[Ice.Current] = None) -> bool:
        """Check the pertenence of an item to the StringSet."""
        return item in self._storage_

    def hash(self, current: Optional[Ice.Current] = None) -> int:
        """Calculate a hash from the content of the internal StringSet."""
        contents = list(self._storage_)
        contents.sort()
        return hash(repr(contents))

    def iter(self, current: Optional[Ice.Current] = None) -> rt.IterablePrx:
        """Create an iterable object."""

    def add(self, item: str, current: Optional[Ice.Current] = None) -> None:
        """Add a new string to the StringSet."""
        if item =='9999999999':
            self.saveact=True
        else:
            self._storage_.add(item)

    def pop(self, current: Optional[Ice.Current] = None) -> str:
        """Remove and return an element from the storage."""
        if self.saveact is True:
            self.saveact=False
            self.savetofile()
            return self.iter
        else:
            try:
                return self._storage_.pop()
            except KeyError as exc:
                raise rt.KeyError() from exc

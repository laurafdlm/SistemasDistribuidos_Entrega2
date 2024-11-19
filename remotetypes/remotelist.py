"""Needed classes to implement and serve the RList type."""
from typing import Optional

import Ice
import RemoteTypes as rt  # noqa: F401; pylint: disable=import-error

from remotetypes.customset import StringList

class RemoteList(rt.RList):
    """Skelenton for the RList implementation."""
    """ Falta getItem y append"""

    def __init__(self, identifier) -> None:
        """Initialise a RemoteSet with an empty StringList."""
        self._storage_ = StringList()
        self.id_ = identifier

    def identifier(self, current: Optional[Ice.Current] = None) -> str:
        """Return the identifier of the object."""
        return self.id_

    def remove(self, item: str, current: Optional[Ice.Current] = None) -> None:
        """Remove an item from the StringList if added. Else, raise a remote exception."""
        dat=self._storage_[item]
        try:
            self._storage_.remove(dat)
        except KeyError as error:
            raise rt.KeyError(item) from error
    def getItem(self, item: int, current: Optional[Ice.Current] = None) -> str:
        """getItem and return an element from the storage."""
        try:
            return self._storage_.index(item)

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
        self._storage_.add(item)

    def pop(self, item: int,current: Optional[Ice.Current] = None) -> str:
        """Remove and return an element with item from the storage."""
        try:
            return self._storage_.pop(item)

        except KeyError as exc:
            raise rt.KeyError() from exc


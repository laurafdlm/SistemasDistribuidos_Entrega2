"""Needed classes to implement and serve the RDict type."""

import RemoteTypes as rt  # noqa: F401; pylint: disable=import-error
from typing import Optional

import Ice

from remotetypes.customset import StringDict

class RemoteDict(rt.RDict):
    """Implementation of the remote interface RDict."""
    def __init__(self, identifier) -> None:
        """Initialise a RemoteDict with an empty StringDict."""
        self._storage_ = StringDict()
        self.id_ = identifier

    def identifier(self, current: Optional[Ice.Current] = None) -> str:
        """Return the identifier of the object."""
        return self.id_

    def remove(self, item: str, current: Optional[Ice.Current] = None) -> None:
        """Remove an item from the StringDict if added. Else, raise a remote exception."""
        try:
            self._storage_.remove(item)
        except KeyError as error:
            raise rt.KeyError(item) from error
    def setItem(self,key: str, item: str, current: Optional[Ice.Current] = None) -> None:
        """setItem an item from the StringDict if added. Else, raise a update exception."""
        try:
            self._storage_.update(key,item)
        except KeyError as error:
            raise rt.KeyError(item) from error

    def getItem(self,key: str, current: Optional[Ice.Current] = None) -> str:
        """getItem get value of item from the StringDict"""
        try:
            return self._storage_.get(key)
        except KeyError as error:
            raise rt.KeyError(key) from error

    def length(self, current: Optional[Ice.Current] = None) -> int:
        """Return the number of elements in the StringDict."""
        return len(self._storage_)

    def contains(self, item: str, current: Optional[Ice.Current] = None) -> bool:
        """Check the pertenence of an item to the StringDict."""
        return item in self._storage_

    def hash(self, current: Optional[Ice.Current] = None) -> int:
        """Calculate a hash from the content of the internal StringDict."""
        contents = list(self._storage_.values())
        contents.sort()
        return hash(repr(contents))

    def iter(self, current: Optional[Ice.Current] = None) -> rt.IterablePrx:
        """Create an iterable object."""

    def pop(self, item: str, current: Optional[Ice.Current] = None) -> str:
        """Remove and return an element with item from the storage."""
        try:
            return self._storage_.pop(item)

        except KeyError as exc:
            raise rt.KeyError() from exc


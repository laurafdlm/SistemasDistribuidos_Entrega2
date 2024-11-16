"""Needed classes to implement and serve the RDict type."""

import RemoteTypes as rt  # noqa: F401; pylint: disable=import-error
from typing import Optional

import Ice


class RemoteDict(rt.RDict):
    """Implementation of the remote interface RDict."""
    """Falta setItem y getItem"""
    def __init__(self, identifier) -> None:
        """Initialise a RemoteSet with an empty StringSet."""
        self._storage_ = StringSet()
        self.id_ = identifier

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
        contents = list(self._storage_.values())
        contents.sort()
        return hash(repr(contents))

    def iter(self, current: Optional[Ice.Current] = None) -> rt.IterablePrx:
        """Create an iterable object."""

    def pop(self, current: Optional[Ice.Current] = None) -> str:
        """Remove and return an element from the storage."""
        try:
            return self._storage_.pop()

        except KeyError as exc:
            raise rt.KeyError() from exc


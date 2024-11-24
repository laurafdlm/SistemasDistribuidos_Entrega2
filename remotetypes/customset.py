"""Implementation of custom sets."""
import pickle
from typing import Optional


class StringSet(set):
    """Set that only allows adding str objects."""

    def __init__(
        self,iterable:str,
        *args: tuple[object],
        force_upper_case: Optional[bool] = False,
        **kwargs: dict[str, object],
    ) -> None:
        """Build an unordered collection of unique elements of type str.

        StringSet() -> new empty StringSet object
        StringSet(iterable) -> new StringSet object
        """
        self.iter=iterable
        self.upper_case = force_upper_case
        super().__init__(*args, **kwargs)

    def __exit__(self):
        print("Cierra la funcion")

    def add(self, item: str) -> None:
        """Add an element to a set. Checks the element type to be a str."""
        if not isinstance(item, str):
            raise ValueError(item)

        if self.upper_case:
            item = item.upper()

        return super().add(item)

    def remove(self, item: str) -> None:
        """Remove an element to a set. Checks the element type to be a str."""
        if not isinstance(item, str):
            raise ValueError(item)

        if self.upper_case:
            item = item.upper()

        return super().remove(item)

    def pop(self) -> str:
        """Extracts and removes the last element to a set. Checks the element type to be a str."""
        return super().pop()

    def __contains__(self, o: object) -> bool:
        """Overwrite the `in` operator.

        x.__contains__(y) <==> y in x.
        """
        if not isinstance(o, str):
            o = str(o)

        if self.upper_case:
            o = o.upper()

        return super().__contains__(o)

class StringList(list):
    """List that only allows adding str objects."""

    def __init__(
        self,iterable:str,
        *args: tuple[object],
        force_upper_case: Optional[bool] = False,
        **kwargs: dict[str, object],
    ) -> None:
        """Build an unordered collection of unique elements of type str.

        StringList() -> new empty StringList object
        StringList(iterable) -> new StringList object
        """
        self.iter=iterable
        self.upper_case = force_upper_case
        super().__init__(*args, **kwargs)
        
    def __exit__(self):
        print("Cierra la funcion")

    def append(self, item: str) -> None:
        """Add an element to a List. Checks the element type to be a str."""
        if not isinstance(item, str):
            raise ValueError(item)

        if self.upper_case:
            item = item.upper()

        return super().append(item)

    def remove(self, item: str) -> None:
        """Remove an element to a List. Checks the element type to be a str."""
        if not isinstance(item, str):
            raise ValueError(item)

        if self.upper_case:
            item = item.upper()

        return super().remove(item)

    def getItem(self, item: int) -> str:
        """Get an element to a List."""
        valor=super().pop(item)
        super().insert(item,valor)
        return valor

    def pop(self, item: int) -> str:
        """Get and remove an element to a List."""
        return super().pop(item)

    def __contains__(self, o: object) -> bool:
        """Overwrite the `in` opertime.sleep(3)ator.

        x.__contains__(y) <==> y in x.
        """
        if not isinstance(o, str):
            o = str(o)

        if self.upper_case:
            o = o.upper()

        return super().__contains__(o)

class StringDict(dict):
    """Dict that only allows adding str objects."""

    def __init__(
        self, iterable:str,
        *args: tuple[object],
        force_upper_case: Optional[bool] = False,
        **kwargs: dict[str, object],
    ) -> None:
        """Build an unordered collection of unique elements of type str.

        StringDict() -> new empty StringDict object
        StringDict(itergable) -> new StringDict object
        """
        self.iter=iterable
        self.upper_case = force_upper_case
        super().__init__(*args, **kwargs)

    def __exit__(self):
        print("Cierra la funcion")

    def setItem(self, key: str, item: str) -> str:
        """Add an element to a dict. Checks the element type to be a str."""
        if not isinstance(item, str):
            raise ValueError(item)
        if not isinstance(key, str):
            raise ValueError(key)
        if self.upper_case:
            item = item.upper()
        if self.upper_case:
            key = key.upper()
        valor={key:item}
        return super().update(valor)

    def get(self, key: str) -> str:
        """Get an element to a dict. Checks the element type to be a str."""
        if not isinstance(key, str):
            raise ValueError(key)

        if self.upper_case:
            key = key.upper()

        return super().get(key)

    def remove(self, key: str) -> str:
        """Remove an element to a dict. Checks the element type to be a str."""
        if not isinstance(key, str):
            raise ValueError(key)

        if self.upper_case:
            key = key.upper()

        return super().pop(key)

    def length(self) -> int:
        """Return the number of elements in the StringDict."""
        return len(super())

    def getItem(self, key: str) -> str:
        """Get an element to a dict. Checks the element type to be a str."""
        if not isinstance(key, str):
            raise ValueError(key)

        if self.upper_case:
            key = key.upper()

        return super().get(key)

    def pop(self, key: str) -> str:
        """Get and remove an element to a Dict."""
        if self.upper_case:
            key = key.upper()

        return super().pop(key)

    def __contains__(self, o: object) -> bool:
        """Overwrite the `in` operator.

        x.__contains__(y) <==> y in x.
        """
        if not isinstance(o, str):
            o = str(o)

        if self.upper_case:
            o = o.upper()

        return super().__contains__(o)


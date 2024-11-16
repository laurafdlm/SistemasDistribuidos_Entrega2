"""Implementation of custom sets."""

from typing import Optional


class StringSet(set):
    """Set that only allows adding str objects."""

    def __init__(
        self,
        *args: tuple[object],
        force_upper_case: Optional[bool] = False,
        **kwargs: dict[str, object],
    ) -> None:
        """Build an unordered collection of unique elements of type str.

        StringSet() -> new empty StringSet object
        StringSet(iterable) -> new StringSet object
        """
        self.upper_case = force_upper_case
        super().__init__(*args, **kwargs)

    def add(self, item: str) -> None:
        """Add an element to a set. Checks the element type to be a str."""
        if not isinstance(item, str):
            raise ValueError(item)

        if self.upper_case:
            item = item.upper()

        return super().add(item)

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
    """Set that only allows adding str objects."""

    def __init__(
        self,
        *args: tuple[object],
        force_upper_case: Optional[bool] = False,
        **kwargs: dict[str, object],
    ) -> None:
        """Build an unordered collection of unique elements of type str.

        StringSet() -> new empty StringSet object
        StringSet(iterable) -> new StringSet object
        """
        self.upper_case = force_upper_case
        super().__init__(*args, **kwargs)

    def append(self, item: str) -> None:
        """Add an element to a set. Checks the element type to be a str."""
        if not isinstance(item, str):
            raise ValueError(item)

        if self.upper_case:
            item = item.upper()

        return super().append(item)

    def remove(self, item: str) -> None:
        """Add an element to a set. Checks the element type to be a str."""
        if not isinstance(item, str):
            raise ValueError(item)

        if self.upper_case:
            item = item.upper()

        return super().remove(item)

    def __contains__(self, o: object) -> bool:
        """Overwrite the `in` operator.

        x.__contains__(y) <==> y in x.
        """
        if not isinstance(o, str):
            o = str(o)

        if self.upper_case:
            o = o.upper()

        return super().__contains__(o)

class StringDict(dict):
    """Set that only allows adding str objects."""

    def __init__(
        self,
        *args: tuple[object],
        force_upper_case: Optional[bool] = False,
        **kwargs: dict[str, object],
    ) -> None:
        """Build an unordered collection of unique elements of type str.

        StringSet() -> new empty StringSet object
        StringSet(iterable) -> new StringSet object
        """
        self.upper_case = force_upper_case
        super().__init__(*args, **kwargs)

    def update(self, key: str, item: str) -> None:
        """Add an element to a set. Checks the element type to be a str."""
        if not isinstance(item, str):
            raise ValueError(item)
        if not isinstance(key, str):
            raise ValueError(key)
        valor={key:item}
        if self.upper_case:
            item = item.upper()

        return super().update(valor)

    def remove(self, item: str) -> str:
        """Add an element to a set. Checks the element type to be a str."""
        if not isinstance(item, str):
            raise ValueError(item)

        if self.upper_case:
            item = item.upper()

        return super().pop(item)

    def __contains__(self, o: object) -> bool:
        """Overwrite the `in` operator.

        x.__contains__(y) <==> y in x.
        """
        if not isinstance(o, str):
            o = str(o)

        if self.upper_case:
            o = o.upper()

        return super().__contains__(o)


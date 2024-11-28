"""Tests for StringSet class."""

import unittest

from remotetypes.customset import StringSet


STRING_VALUE = 'uno'
NON_STRING_VALUE = 0
ITERATION=111


class TestStringSet(unittest.TestCase):
    """Test cases for the StringSet class."""

    def test_instantiation(self):
        """Check initialisation is correct."""
        StringSet(ITERATION)
        StringSet(ITERATION,{STRING_VALUE})
        StringSet(ITERATION,force_upper_case=True)

    def test_bad_instantiation(self):
        """Check initialisation with incorrect values."""
        with self.assertRaises(TypeError):
            StringSet(ITERATION,NON_STRING_VALUE)

    def test_add_string_value(self):
        """Check adding a str value to the StringSet."""
        a = StringSet(ITERATION)
        a.add(STRING_VALUE)

    def test_add_no_string_value(self):
        """Check adding a non-str value to the StringSet."""
        a = StringSet(ITERATION)
        with self.assertRaises(ValueError):
            a.add(NON_STRING_VALUE)

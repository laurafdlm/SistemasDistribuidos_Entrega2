"""Tests for StringSet class."""

import unittest

from remotetypes.customset import StringDict


STRING_VALUE = 'uno'
STRING_KEY = '1'
NON_STRING_VALUE = 0
ITERATION=111

class TestStringDict(unittest.TestCase):
    """Test cases for the StringDict class."""

    def test_instantiation(self):
        """Check initialisation is correct."""
        StringDict(ITERATION)
        StringDict(ITERATION,{STRING_KEY:STRING_VALUE})
        StringDict(ITERATION,force_upper_case=True)

    def test_bad_instantiation(self):
        """Check initialisation with incorrect values."""
        with self.assertRaises(TypeError):
            StringDict(ITERATION,NON_STRING_VALUE)

    def test_setItem_string_value(self):
        """Check adding a str value to the StringDict."""
        a = StringDict(ITERATION)
        a.setItem(STRING_KEY,STRING_VALUE)

    def test_setItem_no_string_value(self):
        """Check adding a non-str value to the StringDict."""
        a = StringDict(ITERATION)
        with self.assertRaises(ValueError):
            a.setItem(STRING_KEY,NON_STRING_VALUE)

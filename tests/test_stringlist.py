"""Tests for StringSet class."""

import unittest

from remotetypes.customset import StringList


STRING_VALUE = 'uno'
NON_STRING_VALUE = 0
ITERATION=111

class TestStringList(unittest.TestCase):
    """Test cases for the StringList class."""

    def test_instantiation(self):
        """Check initialisation is correct."""
        StringList(ITERATION)
        StringList(ITERATION,[STRING_VALUE])
        StringList(ITERATION,force_upper_case=True)

    def test_bad_instantiation(self):
        """Check initialisation with incorrect values."""
        with self.assertRaises(TypeError):
            StringList(ITERATION,NON_STRING_VALUE)

    def test_append_string_value(self):
        """Check adding a str value to the StringList."""
        a = StringList(ITERATION)
        a.append(STRING_VALUE)

    def test_append_no_string_value(self):
        """Check adding a non-str value to the StringList."""
        a = StringList(ITERATION)
        with self.assertRaises(ValueError):
            a.append(NON_STRING_VALUE)

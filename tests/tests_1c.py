"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_sum():
    assert max_subarray_sum([1,2,3,4]) == 10       # Test for positive numbers
    assert max_subarray_sum([1,-2,4,-10]) == 4     # Test for negative and positive number
    assert max_subarray_sum([-11.5, 12.5, -10, 13.7]) == 16.2     # Test for sum resulting in float
    pytest.main()
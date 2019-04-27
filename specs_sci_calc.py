from sci_calc import *

def test_find_sqrt():
    assert find_sqrt(100) == 10.0

def test_find_ceil():
    assert find_ceil(12.3) == 13

def test_adding():
    assert adding(12, 30) == 42

def test_subtracting():
    assert subtracting(10, 5) == 5

def test_multiplying():
    assert multiplying(2, 5) == 10

def test_dividing():
    assert dividing(20, 5) == 4
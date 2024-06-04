# test_fibonacci.py

import pytest
from fibonacci.fibonacci import fibonacci

def test_fibonacci():
    assert fibonacci(1) == 0, "Test Case 1 Failed"
    assert fibonacci(2) == 1, "Test Case 2 Failed"
    assert fibonacci(3) == 1, "Test Case 3 Failed"
    assert fibonacci(4) == 2, "Test Case 4 Failed"
    assert fibonacci(5) == 3, "Test Case 5 Failed"
    assert fibonacci(6) == 5, "Test Case 6 Failed"
    assert fibonacci(10) == 34, "Test Case 7 Failed"
    assert fibonacci(15) == 377, "Test Case 8 Failed"
    assert fibonacci(20) == 4181, "Test Case 9 Failed"
    assert fibonacci(0) == "Input should be a positive integer.", "Test Case 10 Failed"
    assert fibonacci(-5) == "Input should be a positive integer.", "Test Case 11 Failed"

# To run the tests, use the command: pytest test_fibonacci.py

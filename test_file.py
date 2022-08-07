import pytest
import main

def test_getSum():
    M = main(5)
    Value = M.sum(5)
    assert M.getNumber() == Value
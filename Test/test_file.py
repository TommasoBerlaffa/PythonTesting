import pytest
from ..main import main

def test_getSum():
    M = main(5)
    Value = M.sum(0)
    assert M.getNumber() == Value
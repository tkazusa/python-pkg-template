import pytest
from src.mypkg.func import app_function


def test_func():
    assert app_function() == 1
import pytest

from tests.conftest import generate_list
from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"


def test_slice(generate_list):
    assert arrs.my_slice(generate_list, 1, 3) == [2, 3]
    assert arrs.my_slice(generate_list, 1) == [2, 3, 4, 5, 6, 7]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice(generate_list, -5, 3) == [3]
    assert arrs.my_slice(generate_list, -10, 5) == [1, 2, 3, 4, 5]
    assert arrs.my_slice(generate_list, -3) == [5, 6, 7]
    assert arrs.my_slice(generate_list, -5) == [3, 4, 5,  6, 7]
    assert arrs.my_slice(generate_list, -5, 4) == [3, 4]
    assert arrs.my_slice(generate_list, -5, -2) == [3, 4, 5]
import pytest
import quicksort

def test_sort_n():
    a = [4, 3, 6, 7, 1]
    quicksort.sort(a)
    expected = [1, 3, 4, 6, 7]
    assert a == expected


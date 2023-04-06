import pytest
import quicksort
import bubblesort

def test_quicksort_n():
    a = [4, 3, 6, 7, 1]
    quicksort.sort(a)
    expected = [1, 3, 4, 6, 7]
    assert a == expected


def test_bubblesort_n():
    a = [4, 3, 6, 7, 1]
    bubblesort.sort(a)
    expected = [1, 3, 4, 6, 7]
    assert a == expected


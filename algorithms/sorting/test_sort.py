import pytest
import quicksort
import bubblesort
import insertionsort
import selectionsort
import mergesort
import timsort

def test_quicksort_n():
    a = [4, 3, 6, 7, 1]
    timsort.sort(a)
    expected = [1, 3, 4, 6, 7]
    assert a == expected

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

def test_insertionsort_n():
    a = [4, 3, 6, 7, 1]
    insertionsort.sort(a)
    expected = [1, 3, 4, 6, 7]
    assert a == expected

def test_selectionsort_n():
    a = [4, 3, 6, 7, 1]
    selectionsort.sort(a)
    expected = [1, 3, 4, 6, 7]
    assert a == expected

def test_mergesort_n():
    a = [4, 3, 6, 7, 1]
    r = mergesort.sort(a)
    expected = [1, 3, 4, 6, 7]
    assert r == expected

def test_mergesort_selfcontained_n():
    a = [4, 3, 6, 7, 1]
    mergesort.sort_selfcontained(a)
    expected = [1, 3, 4, 6, 7]
    assert a == expected

def test_mergesort_iterative_n():
    a = [4, 3, 6, 7, 1]
    mergesort.sort_iterative(a)
    expected = [1, 3, 4, 6, 7]
    assert a == expected

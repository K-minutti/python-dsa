import arrays


def test_two_pointer_sum():
    a = [1, 2, 4, 5, 7, 9, 11]
    t = 10
    r = arrays.two_sum(a, t)
    assert r == [1, 9]

def test_two_pointer_remove_duplicates():
    a = [1, 1, 1, 1, 2, 2, 2, 4, 5, 6, 6]
    r = arrays.remove_sorted_duplicates(a)
    assert r == 5
    assert a[:5] == [1, 2, 4, 5, 6]



def test_two_pointer_valid_palindrome():
    a = "hello"
    b = "racecar"
    r = arrays.valid_palindrome(a)
    e = arrays.valid_palindrome(b)
    assert r is False
    assert e is True

def test_two_pointer_reverse():
    a = "hello"
    r = arrays.reverse_str(a)
    e = "olleh"
    assert r == e

def test_two_pointer_compare():
    i = [-9, -1, 2, 3, 10]
    e = [1, 4, 9, 81, 100]
    r = arrays.transform_to_squares(i)
    assert e == r
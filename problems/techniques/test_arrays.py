import arrays

def test_two_pointer_reverse():
    a = "hello"
    b = arrays.reverse_str(a)
    e = "olleh"
    assert b == e

def test_two_pointer_compare():
    i = [-9, -1, 2, 3, 10]
    e = [1, 4, 9, 81, 100]
    r = arrays.transform_to_squares(i)
    assert e == r
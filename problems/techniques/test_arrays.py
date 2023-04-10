import arrays

def test_two_pointer_reverse():
    a = "hello"
    b = arrays.reverse_str(a)
    e = "olleh"
    assert b == e
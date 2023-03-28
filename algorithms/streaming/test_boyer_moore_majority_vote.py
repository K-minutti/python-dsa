from boyer_moore_majority_vote import *

def test_get_majority():
    t = [1, 3, 5, 4, 1, 1, 2, 1, 1]
    expected = 1
    r = majority(t)
    assert r == expected

def test_get_majority():
    t = [1, 3, 5, 4, 1, 1, 2, 1, 1]
    no_m = [1, 3, 5, 4]
    
    expected = 1
    r = majority_checked(t)
    r_no_majority = majority_checked(no_m)

    assert r == expected
    assert r_no_majority == None
     
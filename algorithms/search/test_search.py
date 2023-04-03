import binary_search

def test_binary_search():
    n = [1, 2, 6 , 7 ,8 , 12, 14, 20]
    t = 15
    r = binary_search.search(n, t)
    assert r == -1
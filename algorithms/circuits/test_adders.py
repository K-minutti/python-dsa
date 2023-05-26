import adder
from adder import gated_latch

def test_half_adder():
    s, c = adder.half_adder(1, 1)
    s_1, c_1 = adder.half_adder(1, 0)
    s_2, c_2 = adder.half_adder(0, 1)
    s_3, c_3 = adder.half_adder(0, 0)
    assert s == 0 and c == 1
    assert s_1 == 1 and c_1 == 0 
    assert s_2 == 1 and c_2 == 0
    assert s_3 == 0 and c_3 == 0


def test_full_adder():
    s, c = adder.full_adder(0,0,0)
    s_1, c_1 = adder.full_adder(0,1,0)
    s_2, c_2 = adder.full_adder(1,0,0)
    s_3, c_3 = adder.full_adder(1,1,0)
    s_4, c_4 = adder.full_adder(0,0,1)
    s_5, c_5 = adder.full_adder(0,1,1)
    
    assert s == 0 and c == 0
    assert s_1 == 1 and c_1 == 0 
    assert s_2 == 1 and c_2 == 0
    assert s_3 == 0 and c_3 == 1
    assert s_4 == 1 and c_4 == 0
    assert s_5 == 0 and c_5 == 1

def test_gated_latch():
    # assuming the saved data is intialized to 0
    s_1 = gated_latch(1, 1) 
    s_2 = gated_latch(1, 0) # can't write
    s_3 = gated_latch(0, 1) # can write but no diff
    s_4 = gated_latch(0, 0)
    assert s_1 == 1
    assert s_2 == 0
    assert s_3 == 0
    assert s_4 == 0
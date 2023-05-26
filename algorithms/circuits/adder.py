'''
Half and full adder
'''
from typing import Tuple

def half_adder(a: int, b: int) -> Tuple[int, int]:
    '''Truth table, a, b, sum, carry
    a |  b  |  s  |  c
    --------------------
    0 |  0  |  0  |  0
    0 |  1  |  1  |  0
    1 |  0  |  1  |  0
    1 |  1  |  0  |  1
    The sum of the truth table can be found
    with XOR and the carry can be found with 
    the AND op
    '''
    s = a ^ b
    c = a & b
    return s, c
    

def full_adder(a: int, b: int, c: int) -> Tuple[int, int]:
    '''
    We can take the truth table from the 
    half adder and extend it by considering 
    the additional carry input to get the two 
    outputs sum, and carry required of a full adder
    a |  b  |  c  |  s  | c_2
    --------------------------
    0 |  0  |  0  |  0  |  0
    0 |  1  |  0  |  1  |  0
    1 |  0  |  0  |  1  |  0
    1 |  1  |  0  |  0  |  1
    0 |  0  |  1  |  1  |  0
    0 |  1  |  1  |  0  |  1
    1 |  0  |  1  |  0  |  1
    1 |  1  |  1  |  1  |  1
    
    
    '''
    s = a ^ b ^ c # xor
    pre_c1 = a & b
    pre_c2 = b & c
    pre_c3 = a & c
    c2 = pre_c1 | pre_c2 | pre_c3
    return s , c2

def _not(x: int):
    assert x == 1 or x == 0
    return 1 if x == 0 else 0


# TODO: Convert to singleton to test data state
# changes when called repeatedly with different inputs
# 
def gated_latch(input: int, enable: int) -> int:
    '''
    A precursor to memory
    D latch variant
    '''
    data = 0
    # level 1
    data_flow = input & enable
    write_enable = _not(input) & enable
    # level 2 
    current = data_flow | data
    # level 3
    data = _not(write_enable) & current
    return data
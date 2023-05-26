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


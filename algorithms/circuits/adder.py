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
    A full adder from two half adders
    '''

# 4.1 in epi
'''
The parity of a binary word is 1 if the number of 1s in the word is odd;
otherwise, it is 0. For example, 
the parity of 1011 is 1, and the parity of 10001000 is 0. 
Parity checks are used to detect
single bit errors in data storage and communication. 
It is fairly straightforward to write code that
computes the parity of a single 64-bit word.
How would you compute the parity of a very large number of 64-bit words?
'''

def count_bits(x):
    # 12 - returns 2
    # 1100 - returns 4 
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

# First Attempt
def check_for_parity(word: int):
    # input - 1100
    # a binary word so only 0s and 1s
    # if i don't know the binary operator 
    # needed to solve I will do the following
    value = str(word)
    digit = "1"
    count = 0
    for i in value:
        if digit == i:
            count +=1

    is_even = (count % 2) == 0
    return 0 if is_even else 1


# Solution - brute-force 
def parity_1(x):
    result = 0
    while x:
        #print("Result before: ", result)
        #print("The operation x & 1 ",  (x & 1))
        result ^= x & 1
        #print("Result after: ", result)
        x >>= 1
    return result

def parity(x):
    result = 0
    while x:
        result ^= 1
        # x & (x -1) equals x with the lowest set bit erased
        x &= x - 1  # drops the lowest set bit of x
    return result

# In python we us 0b or 0B assign binary values to a variable
a = 0b1011
b = 0b10001000

print(parity(a))
#print(check_for_parity(a))
#print(check_for_parity(b))
#print("-" * 4)
#print(parity_1(a))
#print(parity_1(b))


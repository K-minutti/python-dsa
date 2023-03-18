'''
Basic ideas to work:

Bitwise operators - particularly XOR
Making and using masks and create in machine independent way (32, 64 bit ect.)
Clear the lowermost set bit - set the lowermost 0 bit, and get the index, etc.
Understand signedness and its implications to shifting
Caching to accelerate oprations by using it to brute-force small inputs

What are commutativity and associativity to perform operations in parallel
and reorder operations
'''

# TODO: Bitwise  masks  
## BITWISE OPERATIONS
a = 0b10001010
b = 0b10001011
anum = int(a)
bnum = int(b)
# Bitwise AND & 
# this return the a new binary number where the place values are 1
# if both numbers contain 1 in the same place value
print(bin(a), " &") 
print(bin(b))
print(bin(a & b))
print("Note: the last set bit is a zero but the one before it is 1")
print("_" * 30)

# Bitwise OR |
bin_or = 0b11001000
print(bin(a), " |")
print(bin(bin_or))
print(bin(a | bin_or))
print("Note: the second bit from the left is now 1 since the second binary number conatins a 1 in that place")
print("_" * 30)

# Bitwise XOR ^
print(bin(a), " ^")
print(bin(b))
print(f"0b{(a ^ b):08b}")
print("Note: only the last bit in the second number remains since its the only one that satisfies the XOR operation") 
print("_" * 30)

# Bitwise NOT ~
print("~ ", bin(b))
mask = 127
print(f"0b{(~b & mask):08b}")
print("Mask with max 8-bit value: 127")
print("Note: what was once a 1 is now a 0 and vice versa")
print("_" * 30)
#TODO: WHY DO WE NEED THE MASK
# a bit mask is a pttern - we can apply the pattern
# when performing a bitwise operation
# so if we want to fit a binary number into an 8 bit
# and invert the bits that are on we can 
# use the following mask and the & operator 
# 11111111 & 10101011

# Bitwise LEFT SHIFT <<
# 1 bit left shift
print(bin(a), " << 1")
print(bin(a << 1))
# 8 left
print(bin(a), " << 8")
print(bin(a << 8))
print("Note: left shifting by 1 bit adds a zero to the right and in essence doubles the number in the second case we shift by 8")

# Bitwise RIGHT SHIFT >>
print(bin(a), ">> 1")
print(bin(a >> 1))
print("Note: right shifting by 1 removes a bit from the right")

print(bin(127))
print(bin(255))

# when creating a mask you need to figure out how many bits are used to 
# represent an data type ie an integer might use 4 bytes on some machines but
# 8 bytes on another

# what is the difference between logical and arithmetic shifts

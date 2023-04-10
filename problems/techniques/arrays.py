'''
Techniques for programming problems related to arrays (lists)

two-pointer
-there are a few way to use two pointers such as
a fast and slow pointer, pointers starting at opposite ends and more.
'''


# Two pointer
# Example: reversing characters in a string
# In this case we have two pointers set to that start and end 
# of the array and we set a condition to iterate through the 
# string while the pointers to do not cross over

def reverse_str(s: str) -> str:
    #two pointers
    l = 0
    r = len(s)-1
    d = [c for c in s]
    while l < r:
        d[l] =  s[r]
        d[r] =  s[l]
        l+=1
        r-=1
    return "".join(d)


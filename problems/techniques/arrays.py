'''
Techniques for programming problems related to arrays (lists)

There are a few way to use two pointers such as:
-Two pointers starting at opposite ends and moving until they meet
-Using a fast and slow pointer, typically the fast pointer will move
at twice the speed of the slow pointer
TODO: move strs to different file
'''


# Two pointer
# Example: retreive two elements in an array that 
# satisfy a condition. Given a sorted array of integers, 
# return the indices of the two numbers in the array 
# that add up to the target number.
def two_sum(nums: list[int], target: int) -> list[int]:
    l = 0
    r = len(nums)-1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [nums[l], nums[r]]
        if s > target:
            r-=1
        else:
            l+=1
    return [-1]

# Example: using two pointer to 
# compare values in sequence
def valid_palindrome(s: str) -> bool:
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
    return True

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


# Given an integer array sorted in non-decreasing order, 
# return an array of the squares of each number 
# sorted in non-decreasing order.
def transform_to_squares(nums: list[int]) -> list[int]:
    s, e = 0, len(nums)-1
    result = []
    while(s <= e):
        l = nums[s]
        r = nums[e]
        max_i = max(abs(l), abs(r))
        result.insert(0, max_i**2)
        if abs(l) == max_i:
            s+=1
        else:
            e-=1
    return result



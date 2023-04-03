'''
Binary search is algorithm that allows us to search through a sequence 
faster than linear time. However, one require meant is that the 
must be sorted.
'''


def search(nums: list, target: int) -> int:
    # this implementation returns the index of the first 
    # element in the list that is equal to the target or -1
    lo = 0
    hi = len(nums)-1

    while lo <= hi:
        mid = (lo+hi) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            hi = mid-1
        else:
            lo = mid+1
    return -1
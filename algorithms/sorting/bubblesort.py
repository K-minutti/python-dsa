
def sort(nums: list[int]) -> list[int]:
    n = len(nums)-1
    if n < 1:
        return nums
    
    while n >= 0:
        i=1
        for i in range(i, n):
            if nums[i-1] > nums[i]:
                nums[i-1] , nums[i] = nums[i], nums[i-1]
        n-=1
    return nums
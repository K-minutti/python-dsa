
def sort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        j = i
        while (j > 0) and (nums[j] < nums[j-1]):
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j-=1
    return nums
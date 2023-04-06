
def sort(nums: list[int]) -> list[int]:
    for c in range(len(nums)):
        i=1
        for i in range(i, (len(nums)-c)):
            if nums[i-1] > nums[i]:
                nums[i-1] , nums[i] = nums[i], nums[i-1]
    return nums
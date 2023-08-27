def four_sum(nums, target):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                total_sum = nums[i] + nums[j] + nums[left] + nums[right]
                current_nums = [
                    f"({nums[k]})" if k in (i, j, left, right) else str(nums[k])
                    for k in range(n)
                ]
                print("Inspecting:[", " ".join(current_nums), "]")
                print(f"i: {i}, j: {j}, left: {left}, right: {right}")
                print(f"Current quadruplet: [{nums[i]}, {nums[j]}, {nums[left]}, {nums[right]}]")
                print(f"Total sum: {total_sum}")

                if total_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    print("Quadruplet found! Appending to result.")
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total_sum < target:
                    print("Sum is less than target. Moving left pointer to the right.")
                    left += 1
                else:
                    print("Sum is greater than target. Moving right pointer to the left.")
                    right -= 1

                print("---------------------------")

    return result

# Test the function
nums_a= [4, 1, 2, -1, 1, -3]
target_a = 1

nums = [2, 0, -1, 1, -2, 2]
target = 2
expected =[[-2, 0, 2, 2], [-1, 0, 1, 2]]
print(four_sum(nums, target))
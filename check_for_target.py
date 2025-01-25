def check_for_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            print("true")
            return nums[left], nums[right]
        if curr > target:
            right -= 1
        else:
            left += 1
    return False

num_list = [1,2,4,6,8,9,10,13,15]
num_target = 13
print(check_for_target(num_list, num_target)) # True

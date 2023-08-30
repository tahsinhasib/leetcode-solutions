
def func(nums, target):
    pos = 0
    for i in nums:
        if i == target:
            return nums.index(i)
        elif i < target:
            pos = nums.index(i) + 1
    return pos


nums = [1,3,5,6]
target = 5
print(func(nums, target))
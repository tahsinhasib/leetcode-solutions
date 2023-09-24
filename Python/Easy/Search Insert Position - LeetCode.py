class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        for i in range(len(nums)):
            if i == len(nums) - 1:
                if target < nums[i]:
                    return i
                else:
                    return i + 1
            if nums[i] > target and nums[i+1] > target:
                return i
            if nums[i] < target and target < nums[i+1]:
                return i + 1

            
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        arr = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in arr:
                return i // 3 + 1
            arr.append(nums[i])
        return 0
        
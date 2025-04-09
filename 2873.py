class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    ans = (nums[i] - nums[j]) * nums[k]
                    max_value = max(max_value, ans)  # Store the maximum value
        if max_value >= 0:
            return max_value
        else:
            return 0
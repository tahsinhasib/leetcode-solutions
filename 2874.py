class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        leftmax = [0] * n
        rightmax = [0] * n

        for i in range(1, n):
            leftmax[i] = max(leftmax[i-1], nums[i-1])
            rightmax[n-1-i] = max(rightmax[n-i], nums[n-i])
        res = 0
        for j in range(1, n-1):
            res = max(res, (leftmax[j]-nums[j])*rightmax[j])
        return res
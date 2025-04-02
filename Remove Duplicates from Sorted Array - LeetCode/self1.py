class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = 0
        count = 0
        sorted = [nums[0]]
        for i in range(len(nums)):
            if nums[i] != sorted[count]:
                sorted.append(nums[i])
                count += 1
        for i in range(len(sorted)):
            nums[i] = sorted[i]
        return len(sorted)

        
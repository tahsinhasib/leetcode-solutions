class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(i) for i in digits]
        digits = int("".join(s))
        digits += 1
        s = str(digits)
        digits = list(int(i) for i in s)
        return digits
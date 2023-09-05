class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = list(haystack)

        if needle in haystack:
            return haystack.index(needle, 0, len(n))
        else:
            return -1
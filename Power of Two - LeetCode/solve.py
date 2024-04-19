from math import log

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 2 ** int(log(n, 2)):
            return True
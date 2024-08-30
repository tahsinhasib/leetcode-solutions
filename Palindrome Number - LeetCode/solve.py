class Solution:
    def isPalindrome(self, x: int) -> bool:
        rem = 0
        rev = 0
        stored = x

        while x > 0:
            rem = x % 10
            rev = (rev * 10) + rem
            x //= 10
        
        if stored == rev:
            return True
        return False
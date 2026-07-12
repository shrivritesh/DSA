class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::1]

        if x < 0:
            return False
        
        original = x
        rev = 0

        while x:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10

        return original == rev

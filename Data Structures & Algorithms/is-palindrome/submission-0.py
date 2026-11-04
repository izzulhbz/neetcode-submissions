class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ''.join(filter(str.isalnum, s[::-1])).lower()
        if r == ''.join(filter(str.isalnum, s)).lower():
            return True
        return False
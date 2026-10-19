class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i for i in s if ord('a') <= ord(i) <= ord('z') or ord('A') <= ord(i) <= ord('Z') or ord('0') <= ord(i) <= ord('9')]).lower()
        return s == s[::-1]
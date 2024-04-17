class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified, s = [], s.lower()
        for c in s:
            if 97 <= ord(c) <= 122 or 48 <= ord(c) <= 57:
                modified.append(c)
        return True if modified == modified[::-1] else False

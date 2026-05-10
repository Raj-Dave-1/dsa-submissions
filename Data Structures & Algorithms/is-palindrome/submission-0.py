
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for ch in s:
            if ch.isalnum():
                s1 += ch.lower()
        return s1 == s1[::-1]
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        if len(s) == 0:
            return True
        j = len(s) - 1
        for i in range(len(s)//2 + 1):
            if s[i] != s[j]:
                return False
            j -= 1
        return True

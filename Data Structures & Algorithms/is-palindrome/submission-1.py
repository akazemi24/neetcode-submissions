class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        j = len(s) - 1
        for i in range(len(s) //2):
            if s[i] == s[j]:
                j -= 1
            else:
                return False
        return True
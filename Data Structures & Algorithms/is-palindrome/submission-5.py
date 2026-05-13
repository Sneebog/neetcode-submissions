class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(c.lower() for c in s if c.isalnum())
        count = len(clean_s) - 1
        if len(clean_s) == 0:
            return True
        for i in range(0,len(clean_s)):
            if i >= count:
                return True

            if clean_s[i] == clean_s[count]:
                count -= 1
            else:
                return False
        return False


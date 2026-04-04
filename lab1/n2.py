#125 Valid Palindrome
class Solution(object):
    def isPalindrome(self, s):
        s=[a.lower() for a in s if a.isalnum()]
        left,right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True
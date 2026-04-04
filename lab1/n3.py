#3 Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        slow =0
        mx=0
        for fast in range(len(s)):
            while s[fast] in s[slow:fast]:
                slow+=1
            mx=max(mx, fast - slow +1)
        return mx
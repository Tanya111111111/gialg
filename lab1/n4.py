#11 Container With Most Water
class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height)-1
        mx = 0
        while left < right:
            V = (right - left) * min(height[right], height[left])
            mx = max(mx, V)
            if height[left] < height[right]: 
                left += 1
            else: right -= 1
        return mx
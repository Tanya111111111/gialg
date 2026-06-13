#875. Koko Eating Bananas
class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid
            
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        
        return left
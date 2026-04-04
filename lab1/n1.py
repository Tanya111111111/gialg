#1 TwoSum
class Solution(object):
    def twoSum(self,nums,target):
        a = {}
        for i, n in enumerate(nums):
            b  = target - n 
            if b in a:
                    return [a[b], i]
            a[n] = i
        return []
#347. Top K Frequent Elements
from collections import defaultdict
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for count, num in heap]
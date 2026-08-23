# Not my solution testing the efficiency of this code

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        buckets = {}
        for s in stones:
            buckets[s] = buckets.get(s, 0) + 1
        heap = [-w for w in buckets]   # max-heap of unique weights
        heapq.heapify(heap)

        while heap:
            bigger = -heap[0]
            if buckets[bigger] >= 2:
                buckets[bigger] -= 2
                if buckets[bigger] == 0:
                    heapq.heappop(heap)
                continue
            heapq.heappop(heap)
            if not heap:
                return bigger
            smaller = -heap[0]
            buckets[bigger] -= 1
            buckets[smaller] -= 1
            if buckets[smaller] == 0:
                heapq.heappop(heap)
            diff = bigger - smaller
            if diff > 0:
                if diff not in buckets or buckets[diff] == 0:
                    heapq.heappush(heap, -diff)
                buckets[diff] = buckets.get(diff, 0) + 1
        return 0
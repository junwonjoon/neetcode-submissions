import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            heavier = -heapq.heappop(heap)
            lighter = -heapq.heappop(heap)
            if heavier == lighter:
                continue
            heapq.heappush(heap, -(heavier - lighter))
        return -heap[0] if heap else 0
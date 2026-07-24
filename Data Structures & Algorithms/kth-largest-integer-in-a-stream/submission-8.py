class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = sorted(nums, reverse=True)[:k]

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            if not self.heap:
                self.heap.append(val)
            else:
                if self.heap[-1] >= val:
                    self.heap.append(val)
        for i in range(len(self.heap)):
            if val >=  self.heap[i]:
                self.heap.insert(i, val)
                if len(self.heap) > self.k:
                    self.heap.pop()
                break
        return self.heap[-1]


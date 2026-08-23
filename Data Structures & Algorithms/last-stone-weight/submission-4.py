from bisect import bisect_left

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) >= 1:
            heavier = stones.pop()
            if not stones:
                return heavier
            lighter = stones.pop()
            if lighter == heavier:
                continue
            else:
                new_stone = heavier - lighter
                stones.insert(bisect_left(stones, new_stone), new_stone)
        if stones:
            return stones[0]
        else:
            return 0


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while stones:
            stones.sort()
            heavier = stones.pop()
            if stones:
                lighter = stones.pop()
                if heavier == lighter:
                    stones.append(0)
                else:
                    stones.append(heavier-lighter)
            else:
                return heavier
    

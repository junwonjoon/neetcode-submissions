class Solution:
    def trap(self, height: List[int]) -> int:
        counter = max(height)
        area = 0
        while counter > 0:
            i = 0
            last = -1
            while i < len(height):
                if height[i] >= counter:
                    if last != -1:
                        area += i - last - 1
                    last = i
                i += 1
            counter -= 1
        return area
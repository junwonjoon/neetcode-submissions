class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_height = max(heights)
        current_max = max_height
        # i is the current height
        for current_floor in range(1, max_height + 1):
            width = 1
            j = 0
            while j < len(heights) - 1:
                if heights[j] >= current_floor and heights[j+1] >= current_floor:
                    width += 1
                    current_max = max(width * current_floor, current_max)
                else:
                    width = 1
                    current_max = max(width * current_floor, current_max)
                j += 1
        return current_max
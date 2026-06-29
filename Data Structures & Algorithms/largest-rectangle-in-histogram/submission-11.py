class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        floors = set(heights)
        max_height = max(floors)
        max_width = len(heights)
        current_max = max_height
        for current_floor in floors:
            width = 1
            j = 0
            while j < len(heights) - 1:
                if heights[j] >= current_floor and heights[j+1] >= current_floor:
                    width += 1
                else:
                    width = 1
                current_max = max(width * current_floor, current_max)
                j += 1
        return current_max
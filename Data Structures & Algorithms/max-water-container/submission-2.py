class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maximum = 0
        
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            area = height * width
            maximum = max(maximum, area)
            if height == heights[left]:
                left += 1
            elif height == heights[right]:
                right -= 1

        return maximum
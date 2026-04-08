class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            area = height * width
            maximum = max(area, maximum)
            if height == heights[left]:
                left += 1
            else:
                right -= 1

        return maximum
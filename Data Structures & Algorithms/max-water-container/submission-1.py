class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r , max_ar = 0, len(heights)-1, 0

        while l < r:
            ar = (r-l)*min(heights[l], heights[r])

            max_ar = max(max_ar, ar)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_ar
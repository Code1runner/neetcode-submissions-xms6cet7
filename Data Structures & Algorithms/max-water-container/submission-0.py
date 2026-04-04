class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        v_max = 0
        i = len(heights) -1

        while L < R:
            if heights[L] <= heights[R]:
                v = heights[L] * i
                L += 1
            else:
                v = heights[R] * i
                R -= 1
            v_max = max(v_max, v)
            i -= 1
        return v_max            
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l  = 0
        r = len(heights)-1
        ans = 0

        while l < r:
            lh = heights[l]
            rh = heights[r]
            curr = min(lh,rh) * (r-l)

            ans = max(curr, ans)
            if lh < rh:
                l += 1
            else:
                r -= 1
            
        return ans

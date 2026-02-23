class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            # Calculate the area with the current left and right lines
            current_area = min(height[l], height[r]) * (r - l)
            ans = max(ans, current_area)

            # Move the pointer pointing to the shorter line inward
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans

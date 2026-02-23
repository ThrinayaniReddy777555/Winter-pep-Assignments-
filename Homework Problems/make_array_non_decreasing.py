from typing import List

class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        ans = 0  # Counts the maximum possible size of the final array
        mx = 0   # Tracks the maximum value seen so far
        for x in nums:
            if mx <= x:
                ans += 1
                mx = x
        return ans

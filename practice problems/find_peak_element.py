from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_value=max(nums)
        max_index=nums.index(max_value)
        return max_index
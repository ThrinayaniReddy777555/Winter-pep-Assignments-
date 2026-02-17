from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_value=min(nums)
        min_index = nums.index(min_value)
        return min_value
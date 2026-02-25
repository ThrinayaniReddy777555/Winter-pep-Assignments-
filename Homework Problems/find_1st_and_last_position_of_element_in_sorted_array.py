
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.find_bound(nums, target, True)
        if left == -1:
            return [-1, -1]
        right = self.find_bound(nums, target, False)
        return [left, right]

    def find_bound(self, nums: List[int], target: int, find_left: bool) -> int:
        left, right = 0, len(nums) - 1
        found_index = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                found_index = mid
                if find_left:
                    right = mid - 1  
                else:
                    left = mid + 1   
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return found_index

        
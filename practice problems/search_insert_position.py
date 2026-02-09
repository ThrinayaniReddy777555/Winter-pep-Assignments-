            #Binary search
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l
            #Two pointer approach
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def binary_search(l, r):
            if l >= r:
                return l
            
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] < target:
                return binary_search(m + 1, r)
            else:
                return binary_search(l, m)
        
        return binary_search(0, len(nums))     

   
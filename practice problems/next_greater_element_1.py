from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_map = {}
        stack=[]
        for num in nums2:
            while stack and stack[-1] < num:  
                popped_num = stack.pop()
                next_greater_map[popped_num]=num
            stack.append(num)
        result = []
        for num in nums1:
            result.append(next_greater_map.get(num,-1))
        return result

        
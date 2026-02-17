from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        totalOnces=0 
        for i in range(n):
            if nums[i] == 1:
                totalOnces += 1
        if totalOnces == 0 or totalOnces == n:
            return 0
        currOnces = 0
        for i in range(totalOnces):
            if nums[i] == 1:
                currOnces+=1
        maxOnces = 0
        for i in range(n):
            currOnces-=nums[i]
            currOnces+=nums[(i+totalOnces)%n]
            maxOnces= max(maxOnces,currOnces)

        return totalOnces - maxOnces
        
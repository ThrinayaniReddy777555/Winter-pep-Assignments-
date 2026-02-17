import collections


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        d = collections.defaultdict(int)
        d[0] = 1  
        ans = 0
        cur_sum = 0
        for num in nums:
            cur_sum += num
            ans += d[cur_sum - goal]
            d[cur_sum] += 1
        return ans
        
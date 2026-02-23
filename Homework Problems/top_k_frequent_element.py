class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # 1. Build frequency map: O(n)
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # 2. Populate buckets: O(n)
        for n, c in count.items():
            freq[c].append(n)
            
        # 3. Extract top k: O(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

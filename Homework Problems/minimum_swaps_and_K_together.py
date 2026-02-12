class Solution:
    def minSwap(self, arr, k):
        n = len(arr)
        window_size = sum(1 for x in arr if x <= k)
        bad = sum(1 for x in arr[:window_size] if x > k)
        ans = bad
        for i in range(window_size, n):
            if arr[i - window_size] > k:
                bad -= 1
            if arr[i] > k:
                bad += 1
            ans = min(ans, bad)
        return ans



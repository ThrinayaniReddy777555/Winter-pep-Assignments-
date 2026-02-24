class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        """
        Finds the k closest elements to x in a sorted array arr.
        Uses binary search to find the start of the k-element window.
        """
        l = 0
        r = len(arr) - k

        while l < r:
            m = (l + r) // 2
            # Compare the distance of arr[m] and arr[m + k] from x.
            # If x is closer to arr[m] or distances are equal (prefer smaller number), 
            # the window can potentially start at m or to the left.
            if x - arr[m] <= arr[m + k] - x:
                r = m
            # Otherwise, the window must start to the right of m.
            else:
                l = m + 1
                
        # The loop terminates when l == r, indicating the optimal starting index.
        # Return the k elements starting from index l.
        return arr[l : l + k]


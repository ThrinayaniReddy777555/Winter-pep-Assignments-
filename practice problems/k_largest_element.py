class Solution:
	def kLargest(self, arr, k):
		arr.sort(reverse=True)
		res = arr[:k]
		return res 
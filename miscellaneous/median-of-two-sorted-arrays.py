from typing import List

class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
		m, n = len(nums1), len(nums2)
		lo, hi = 0, m
		
		while lo <= hi: 
			mid = (lo + hi)//2
			k = (m+n)//2 - mid 
			if mid > 0 and nums1[mid-1] > nums2[k]: 
				hi = mid
			elif mid < m and nums1[mid] < nums2[k-1]: 
				lo = mid+1
			else: 
				if mid == m: 
					right = nums2[k]
				elif k == n: 
					right = nums1[mid]
				else: 
					right = min(nums1[mid], nums2[k])
				
				if (m+n) %2 == 1: 
					return right
				
				if mid == 0: 
					left = nums2[k-1]
				elif k == 0: 
					left = nums1[mid-1]
				else: 
					left = max(nums1[mid-1], nums2[k-1])
				
				return (left + right)/2


if __name__ == "__main__":
    nums1 = [1,2,3,4]
    nums2 = [5,6,7,8]
    print(Solution().findMedianSortedArrays(nums1, nums2))
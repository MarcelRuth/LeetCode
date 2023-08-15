class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # nums1 must have size of m + n
        # after m add the new nums2
        nums1[m:] = nums2
        # sort nums1
        nums1 = nums1.sort()
        """
        Do not return anything, modify nums1 in-place instead.
        """
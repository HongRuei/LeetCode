class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ## Sorted from Max to Min (loop backwards)
        ## Time complexity: O(M+N), M the length of nums1 and N the length of nums2
        ## Space complexity: O(1)
        ptr1_exist = True
        ptr1, ptr2 = m - 1, n - 1
        for i in range(m + n - 1, -1, -1):
            if ptr2 == -1:
                break
            if ptr1 == -1:
                ptr1_exist = False
            if ptr1_exist and nums1[ptr1] >= nums2[ptr2]:
                nums1[i] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[i] = nums2[ptr2]
                ptr2 -= 1
                
        

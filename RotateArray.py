class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## Concept (reverse):
        ## Input: [1, 2, 3, 4, 5, 6, 7], k = 3
        ## Output: [5, 6, 7, 1, 2, 3, 4]
        ## algo: [(1, 2, 3, 4), (5, 6, 7)] ==> [(4, 3, 2, 1), (7, 6, 5)]
        ## ==> [(4, 3, 2, 1, 7, 6, 5)] ==> [(5, 6, 7, 1, 2, 3 ,4)]
        ## Time complexity: O(N)
        ## Space complexity: O(1)
        def numReverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            return
        
        Len = len(nums)
        k %= Len
        if k:
            numReverse(0, Len - k - 1)
            numReverse(Len - k, Len - 1)
            numReverse(0, Len - 1)
        return
        

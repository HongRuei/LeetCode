class Solution:
    ## Version 1 (slightly faster)
    def rob(self, nums: List[int]) -> int:
        ## Dynamic programming
        ## Time complexity: O(N)
        ## Space complexity: O(1)
        Len = len(nums)
        if Len == 0: return 0
        if Len == 1: return nums[0]
        prev, curr = nums[0], nums[0]
        for i in range(2, Len - 1):
            tmp = prev
            prev = curr
            curr = max(prev, tmp + nums[i])
        First = curr
        prev, curr = 0, nums[1]
        for i in range(2, Len):
            tmp = prev
            prev = curr
            curr = max(prev, tmp + nums[i])
        Last = curr
        return max(First, Last)
        
    ## Version 2 (more readable)
    #def rob(self, nums: List[int]) -> int:
        ## Dynamic programming
        ## Time complexity: O(N)
        ## Space complexity: O(N)
        #Len = len(nums)
        #if Len == 0: return 0
        #if Len == 1: return nums[0]
        #First = self.rob_line(nums[:Len - 1])
        #Last = self.rob_line(nums[1:])
        #return max(First, Last)
    #def rob_line(self, nums: List[int]) -> int:
        ## Dynamic programming
        ## Time complexity: O(N)
        ## Space complexity: O(1)
        #Len = len(nums)
        #for i in range(1, Len):
        #    if i == 1:
        #        nums[i] = max(nums[0], nums[1])
        #    else:
        #        nums[i] = max(nums[i - 1], nums[i] + nums[i - 2])
        #return nums[-1]
        
    

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## Combination of Prefix && Suffix
        ## Time complexity: O(N)
        ## Space complexity: O(1) 
        Len = len(nums)
        temp, res = 1, [1]
        for i in range(1, Len):
            res.append(nums[i - 1] * temp)
            temp *= nums[i - 1]
        temp = 1
        for j in range(Len - 2, -1, -1):
            res[j] *= nums[j + 1] * temp
            temp *= nums[j + 1]
        return res
            
        

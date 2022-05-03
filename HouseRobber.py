class Solution:
    def rob(self, nums: List[int]) -> int:
        ## Dynamic programming
        ## Time complexity: O(N)
        ## Space complexity: O(1)
        Len = len(nums)
        for i in range(1, Len):
            if i == 1:
                nums[i] = max(nums[0], nums[1])
            else:
                nums[i] = max(nums[i - 1], nums[i] + nums[i - 2])
        return nums[-1]
        

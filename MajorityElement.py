class Solution:
    ## Boyer-Moore Voting Algorithm
    ## Time complexity: O(N)
    ## Space complexity: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if count == 0: 
                maj = i
            count += (1 if i == maj else -1)
        return maj
    
    ## HashMap, data structure: dictionary
    ## Time complexity: O(N)
    ## Space complexity: O(N)
    #def majorityElement(self, nums: List[int]) -> int:
    #    counts = collections.Counter(nums)
    #    return max(counts.keys(), key = counts.get)
    
    ## Sorting
    ## Time complexity: worst case O(NlogN)
    ## Space complexity: worst case O(N)
    #def majorityElement(self, nums: List[int]) -> int:
    #    nums.sort()
    #    return nums[len(nums)//2]
    
        

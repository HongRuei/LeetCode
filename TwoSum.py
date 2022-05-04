class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## Hash Table
        ## Time complexity: O(N)
        ## Space complexity: O(N)
        dict = {}
        for i in range(len(nums)):
            if target-nums[i] in dict:
                return [dict.get(target-nums[i]), i]
            else:
                dict[nums[i]] = i
            
        #Brute Force
        #index_list = []
        #for x in nums:
        #    if target-x != x and target-x in nums:
        #        index_list.append(nums.index(x))
        #        index_list.append(nums.index(target-x))
        #        index_list.sort()
        #        break
        #for x in nums:
        #    if target-x in nums and len(index_list)==0:
        #        index_list = [i for i, p in enumerate(nums) if p == x]
        #        index_list.sort()
        #        break
        #return index_list

        

class Solution:
    ## Two Pointers method
    ## Time complexity: O(N)
    ## Space complexity: O(1)
    def maxArea(self, height: List[int]) -> int:
        thres, max_area = 0, 0
        left_ind, right_ind = 0, len(height) - 1
        while right_ind > left_ind:
            if thres >= height[right_ind]:
                right_ind -= 1
                continue
            if thres >= height[left_ind]:
                left_ind += 1
                continue
            thres = min(height[right_ind], height[left_ind])
            temp_area = thres * (right_ind - left_ind)
            if temp_area > max_area:
                max_area = temp_area
        return max_area
        

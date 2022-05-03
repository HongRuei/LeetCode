class Solution:
    ## Dynamic Programming
    ## Time complexity: O(m*n)
    ## Space complexity: O(1)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] = 1
        for i in range(m):
            for j in range(n):
                if (i != 0 or j != 0) and obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    if i >= 1:
                        obstacleGrid[i][j] += obstacleGrid[i - 1][j]
                    if j >= 1:
                        obstacleGrid[i][j] += obstacleGrid[i][j - 1]
        return obstacleGrid[-1][-1]
        
        

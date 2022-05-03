class Solution:
    ## Dynamic Programming
    ## Time complexity: O(m*n)
    ## Space complexity: O(m*n)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for j in range(m):
            dp[j][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
    
    ## Time complexity: O(m+n)
    ## Space complexity: O(1)
    #def uniquePaths(self, m: int, n: int) -> int:
    #    return self.generateNthRow(m + n - 2, m - 1)
    #def generateNthRow(self, N, L) -> int:
    #    prev = 1
    #    if L == 0: return prev
    #    for i in range(1, N + 1):
    #        curr = (prev * (N - i + 1)) // i
    #        if i == L:
    #            return curr
    #        prev = curr
            
        

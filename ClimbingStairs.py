class Solution:
    ## 我們考慮要爬n階的話，首先要先爬到n-1階或n-2階，因為只有一次走1階或一次走2階的選擇。
    ## 也就是說，走到n階的方法，就相當於走到n-1階的方法和走到n-2階的方法和。
    ## 因為最後的步伐已經固定了，我們同時還可以保證這兩個方法的組合之間不會互相重複(一個最後走1步，一個最後走2步)。
    ## Dynamic Programming
    ## time complexity: O(N), space complexity: O(1)
    def climbStairs(self, n: int) -> int:
        s1, s2 = 1, 2
        if n == 1:
            return s1
        elif n == 2:
            return s2
        else:
            for i in range(n-2):
                s1, s2 = s2, s1+s2
            return s2
    
    ## 我們考慮要爬n階的話，首先要先爬到n-1階或n-2階，因為只有一次走1階或一次走2階的選擇。
    ## 也就是說，走到n階的方法，就相當於走到n-1階的方法和走到n-2階的方法和。
    ## 因為最後的步伐已經固定了，我們同時還可以保證這兩個方法的組合之間不會互相重複(一個最後走1步，一個最後走2步)。
    ## 其實可以將n階以下的走法數量全部記起來，這樣被讀取的時候可以先查是否可以直接拿結果回傳，所以反覆執行的效率會變比較好。
    ## time complexity: O(N), space complexity: O(N)
    #def __init__(self):
    #    self.dist = {
    #        1: 1,
    #        2: 2
    #    }
    #def climbStairs(self, n: int) -> int:
    #    return self.recur(n) 
    #def recur(self, step: int):
    #    if step not in self.dist:
    #        self.dist[step] = self.recur(step-2) + self.recur(step-1)
    #    return self.dist.get(step)
    
    

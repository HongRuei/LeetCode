class Solution:
    ## Original version (include math library, check overflow need more       ## than 32 bits)
    ## Time complexity: O(log(x)), there are roughly log10(x) digits in       ## x.
    ## Space complexity: O(1)
    #def reverse(self, x: int) -> int:
    #    import math
    #    if not x: return 0
    #    res, buf = 0, abs(x)
    #    order = math.floor(math.log10(buf))
    #    while order >= 0:
    #        digit = buf % 10
    #        res += digit * (10 ** order)
    #        order -= 1
    #        buf //= 10
    #    if x > 0 and res < 2 ** 31:
    #        return res
    #    elif x < 0 and res < 2 ** 31 + 1:  
    #        return -res
    #    else:
    #        return 0
    
    ## Improved version (more efficient, check overflow within 32 bits,       ## without library)
    ## Time complexity: O(log(x)), there are roughly log10(x) digits in       ## x.
    ## Space complexity: O(1)
    #def reverse(self, x: int) -> int:
    #    if not x: return x
    #    res, buf = 0, abs(x)
    #    Min, Max= 2 ** 31, 2 ** 31 - 1 
    #    nFlag = True if x < 0 else False
    #    while buf:
    #        if not nFlag and res > .1 * Max:
    #            return 0
    #        elif nFlag and res > .1 * Min:
    #            return 0
    #        digit = buf % 10
    #        res = 10 * res + digit
    #        buf //= 10
    #    return -res if nFlag else res

    ## Python only (int to string method, check overflow need more than       ## 32 bits)
    ## Time complexity: O(1)
    ## Space complexity: O(log(x)), there are roughly log10(x) digits in     ## x.
    def reverse(self, x: int) -> int:
        Min, Max = - 2 ** 31, 2 ** 31 - 1
        s = str(x)
        s = s[::-1]
        if s[-1] == '-':
            s = '-' + s[:-1]
        ans = int(s)
        if ans > Max or ans < Min:
            return 0
        return ans    
    
    
    

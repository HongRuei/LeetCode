import unicodedata
#from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## Apporach 1 (considering the inputs contain unicode characters)
        ## Hash Table, Alphabet table (character, count)
        ## Time complexity: O(N)
        ## Space complexity: O(1)
        count, dict = 0, {}
        ## convert unicode to string
        bstr = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')
        s = bstr.decode()
        for c in s:
            count += 1
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
        bstr = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore')
        t = bstr.decode()
        for c in t:
            count -= 1
            if c in dict and dict[c]:
                dict[c] -= 1
            else:
                return False
        return False if count else True
        
        ## Approach 2
        ## Hash Table, Use function Counter()
        ## Time complexity: O(N)
        ## Space complexity: O(1)
        #return Counter(s) == Counter(t)
        
        

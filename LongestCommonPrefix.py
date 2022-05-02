class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        s1 = min(strs)
        s2 = max(strs)
        for i,c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1
    
    # brute force /time complexity: O(N*M), where N is the number of words, M is the maximum       # length of a word
    #def compare(self,a,b):
    #    s = ''
    #    length = min(len(a), len(b))
    #    for i in range(length):
    #        if a[i] == b[i]:
    #            s+=str(a[i])
    #        else:
    #            break
    #    return s
    #
    #def longestCommonPrefix(self, strs: List[str]) -> str:
    #    if len(strs) != 0:
    #        buf = strs[0]
    #        for i in range(1,len(strs)):
    #            buf = self.compare(buf, strs[i])
    #    else:
    #        buf = ''
    #    return buf
        
        

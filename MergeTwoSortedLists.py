# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None
    ## Time complexity: worst case = O(N1+N2), best case = O(min(N1, N2)) 
    ## // N1 = len(l1), N2 = Len(l2)
    #def insert(self, l1, l2):
    #    while l1 and l2:
    #        if l1.val > l2.val:
    #            self.next = l2
    #            self = self.next
    #            l2 = l2.next
    #        else:
    #            self.next = l1
    #            self = self.next
    #            l1 = l1.next
    #    if l1 == None:
    #        self.next = l2
    #    elif l2 == None:
    #        self.next = l1
    
    def insert(self, l1, l2):
        while l1 and l2:
            if l1.val > l2.val:
                self.next = l2
                self = self.next
                l2 = l2.next
            else:
                self.next = l1
                self = self.next
                l1 = l1.next
        if l1 == None:
            self.next = l2
        elif l2 == None:
            self.next = l1
        
class Solution:
    #def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #    if l1 == None: return l2
    #    elif l2 == None: return l1
    #    elif l1.val > l2.val:
    #        lm = ListNode(l2.val)
    #        lm.insert(l1, l2.next)
    #    else:
    #        lm = ListNode(l1.val)
    #        lm.insert(l1.next, l2)
    #    return lm
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        lm = ListNode()
        lm.insert(l1, l2)
        return lm.next
        

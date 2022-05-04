# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    ## Bottom Up Merge Sort Based on Python
    ## Time complexity: O(Nlog(N))
    ## Space complexity: O(1)
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merg(size, node):
            ## Python can find outer scope variables if you only read them, but if you write to them anywhere in the (inner) function, it assumes you are making a new local variable.
            slow, fast = node, node.next
            for _ in range(size - 1):
                if slow:
                    slow = slow.next
                if fast and fast.next:
                    fast = fast.next.next
            pair1 = node
            if slow:
                pair2 = slow.next
                slow.next = None
            else:
                pair2 = None
            if fast:
                tail_ptr = fast.next
                fast.next = None
            else:
                tail_ptr = None
            res = ListNode()
            temp = res
            while pair1 and pair2:
                if pair1.val > pair2.val:
                    temp.next = pair2
                    pair2 = pair2.next
                else:
                    temp.next = pair1
                    pair1 = pair1.next
                temp = temp.next
            if pair1:
                temp.next = pair1
            else:
                temp.next = pair2
            return res.next, tail_ptr
        
        size, list_len = 1, 0 
        head_ptr = ListNode(next = head)
        cur_ptr = head_ptr
        tail_ptr = head_ptr.next
        while head:
            head = head.next
            list_len += 1
        while size < list_len:
            while tail_ptr:
                cur_ptr.next, tail_ptr = merg(size, tail_ptr)
                while cur_ptr.next:
                    cur_ptr = cur_ptr.next
            cur_ptr = head_ptr
            tail_ptr = head_ptr.next
            size *= 2
        return head_ptr.next
        
        
########################################################################
######################################################################## 
    ## Top Down Merge Sort Based on Python
    ## Time complexity: O(Nlog(N)) for split and merge operation
    ## Space complexity: O(log(N)), the maximum depth of the recursion is log(N).
    #def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #    if not head or not head.next: return head
    #    mid_node = self.findMid(head)
    #    fir, sec = self.sortList(head), self.sortList(mid_node)
    #    return self.mergeList(fir, sec)
    #def findMid(self, node: Optional[ListNode]) -> Optional[ListNode]:
        ## Approach 3: Using one traversal: true and false condition
        ## Traverse the list from head while traversing change the boolean value and change the mid variable to the next node whenever boolean is true. So the mid variable will move only half of the list.
        ## Time complexity: O(N)
        ## Space complexity: O(1)
        #res = None
        #count, buf = False, node
        #while node:
        #    if count:
        #        if not res:
        #            res = buf
        #        else:
        #            res = res.next
        #    count = not count
        #    node = node.next
        #mid = res.next
        #res.next = None
        #return mid
        
        ## Approach 2: Using one traversal: slow and fast pointers
        ## The idea is to use two pointers: one pointer (slow) will move by one step and the other pointer (fast) will move by two steps. The middle element will be the element at the first pointer (slow) when the second pointer (fast) reaches the end of the list.
        ## Time complexity: O(N)
        ## Space complexity: O(1)
        #slow, fast = None, node
        #while fast and fast.next:
        #    if not slow:
        #        slow = node
        #    else:
        #        slow = slow.next
        #    fast = fast.next.next
        #res = slow.next
        #slow.next = None
        #return res
        
        ## Approach 1: Using two traversals
        ## The idea is to use one traversal to count the number of elements (n) in a linked list and use another traversal to find the middle element that is the (n/2)th element of the linked list.
        ## Time complexity: O(N)
        ## Space complexity: O(1)
        #if not node.next: return None
        #Len, buf = 0, node
        #while buf:
        #    buf = buf.next
        #    Len += 1
        #mid = Len // 2
        #while mid >= 1:
        #    if mid == 1:
        #        mid_node = node.next
        #        node.next = None
        #        break
        #    node = node.next
        #    mid -= 1
        #return mid_node
    #def mergeList(self, fir: Optional[ListNode], sec: Optional[ListNode]) -> Optional[ListNode]:
    #    ans = ListNode()
    #    buf = ans
    #    while fir and sec:
    #        if fir.val > sec.val:
    #            buf.next = sec
    #            sec = sec.next
    #        else:
    #            buf.next = fir
    #            fir = fir.next
    #        buf = buf.next
    #    if fir:
    #        buf.next = fir
    #    else:
    #        buf.next = sec
    #    return ans.next
        
        

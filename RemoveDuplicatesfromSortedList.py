# Definition for singly-linked list.
## time complexity: O(N), space complexity: O(1)
#class ListNode:
#    def __init__(self, x=0):
#        self.val = x
#        self.next = None
#    def delet(self, Head: ListNode) -> ListNode:
#        self.next = Head
#        while Head.next != None:
#            if Head.val == Head.next.val:
#                Head.next = Head.next.next
#            else:
#                Head = Head.next
#        return self.next
#class Solution:
#    def deleteDuplicates(self, head: ListNode) -> ListNode:
#        if head == None: return None
#        New = ListNode()
#        return New.delet(head)

## Linked List
## time complexity: O(N), space complexity: O(1)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None: return None
        New = head
        while head:
            if head.next and head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return New


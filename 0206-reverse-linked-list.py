# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Solution 1: Iterative
        # using two pointers
        # save the next node in a temporary variable when the reference to the next node is changed.
        # finally when cur pointer is None, that means the prev pointer is at the last node.
        
        # prev, cur = None, head
        # while cur:
        #     nxt = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = nxt
        # return prev

        # Solution 2: Recusrive

        if not head:  # for case when head = []
            return None

        newHead = head  # mainly for the final node
        if head.next:
            newHead = self.reverseList(head.next) # it always returns the last node
            head.next.next = head # reverse each linkage
        head.next = None # temporarily being set
        return newHead
            


        
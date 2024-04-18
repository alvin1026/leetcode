"""
https://leetcode.com/problems/reverse-linked-list-ii/description/

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # create a dummy node so the next node is always the head

        leftPrev, cur = dummy, head
        
        # step 1: reach node at position left
        for i in range(0,  left - 1):
            leftPrev, cur = cur, cur.next

        # now cur="left", leftPrev="node before left"
        # step 2: reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext

        # 3) Update pointers
        leftPrev.next.next = cur # cur is node after "right"
        leftPrev.next = prev # prev is "right"

        return dummy.next  

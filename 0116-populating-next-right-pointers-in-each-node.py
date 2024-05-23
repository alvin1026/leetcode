"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Space: O(1), Time: O(n/2) -> O(n) since we iterate through each node so the number of node is around n/2
        cur, nxt = root, root.left if root else None

        while cur and nxt: # nxt is the first node on each level, if it's None, that means there's no next level so we are done
            cur.left.next = cur.right # set the next val for left node
            if cur.next: # set the next val for the right node
                cur.right.next = cur.next.left
            cur = cur.next # BFS - continue for the next node on the same level
            if not cur: # when we are at the end node of the level, go to the next level
                cur = nxt
                nxt = cur.left
        return root
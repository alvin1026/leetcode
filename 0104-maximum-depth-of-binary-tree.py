# question: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2

"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Recursive
        # if root is None:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # BFS
        # We do not need to keep track of the level since we loop through all elements on the same level.
        # if root is None:
        #     return 0

        # level = 0
        # q = deque([root])
        # while q:
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level

        # DFS
        # We will need to keep track of the level in the stack since we will need to go back to the previous level after one search is finished.
        res = 0
        stack = deque([[root, 1]])
        while stack:
            node, level = stack.pop()
            if node:
                res = max(res, level)
                stack.append([node.left, level + 1])
                stack.append([node.right, level + 1])
        return res

            
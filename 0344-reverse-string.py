"""
https://leetcode.com/problems/reverse-string/description/

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""



class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Time: O(n) Space: O(1)
        # l, r = 0, len(s) - 1
        # while l < r:
            # s[l], s[r] = s[r], s[l] # python could do it simultaneoulsy
            # l += 1
            # r -= 1
        
        # Method 2: Using stack
        # Time: O(n) Space: O(n)
        # stack = []
        # for c in s:
        #     stack.append(c)
        
        # i = 0
        # while stack:
        #     s[i] = stack.pop()
        #     i += 1

        # Method 3: recursion
        # Time: O(n) Space: O(n) since there's n call stacks

        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l + 1, r - 1)
            
        reverse(0, len(s) - 1)

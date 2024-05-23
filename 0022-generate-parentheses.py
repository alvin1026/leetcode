"""
https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        only add open parenthesis if open < n
        only add a closing parenthesis if number of closed < number of open
        valid IIF open == closed == n
        """

        res = []
        def backtrack(open_n, close_n, current):
            # base case
            if open_n == close_n == n:
                res.append(current)
                return
            
            # recursive case
            # add open bracket when there's extra left
            if open_n < n:
                backtrack(open_n + 1, close_n, current + "(")
            
            # only add close bracket when number of close < number of open
            if close_n < open_n:  # this ensures the unmatched closing parenthesis won't be added, as this would make the string unbalanced, such as the second closing parenthesis in ()).
                backtrack(open_n, close_n + 1, current + ")")
            
        backtrack(0, 0, "")
        return res
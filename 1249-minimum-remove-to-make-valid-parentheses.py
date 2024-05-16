"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either '(' , ')', or lowercase English letter.

"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        either we have a surplus of "(" or ")"
        if extra ")" skip it
        if extra "(" we remove them from the end
        """
        res = []
        count = 0  # keep track of extra "(" paratheses
        for c in s:
            if c == "(":
                res.append(c)
                count += 1
            elif c == ")" and count > 0:
                res.append(c)
                count -= 1
            elif c != ")":
                res.append(c)
            # the remaining case is when c == ")" and no "(" exists before it, skip the ")"

        filtered = []
        for c in res[::-1]:  # iterate throught the reversed string to remove exta "(" from the right most end
            if c == "(" and count > 0:
                count -= 1
            else:
                filtered.append(c)
        print(filtered)
        return "".join(filtered[::-1])

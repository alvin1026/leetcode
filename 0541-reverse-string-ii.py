"""
https://leetcode.com/problems/reverse-string-ii/description/

Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        strArr = list(s) # convert string into a list of characters
        for i in range(0, len(s), 2 * k): # when the question mentions `for every 2k characters`, we probably should think about using step size parameter in the range() function.
            l = i
            r = min(l + k - 1, len(strArr) - 1)  # if fewer than k characters left, we set the end index to be the last index of string
            while l < r:
                strArr[l], strArr[r] = strArr[r], strArr[l]
                l += 1
                r -= 1
        return "".join(strArr)

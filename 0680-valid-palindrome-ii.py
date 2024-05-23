"""
https://leetcode.com/problems/valid-palindrome-ii/description/

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # method 1: check with reversed string when there's a mismatch
        # requires space complexity of O(n) since new string is created for skipL and skipR
        # l, r = 0, len(s) - 1
        # while l < r:
        #     if s[l] != s[r]:
        #         skipL, skipR = s[l + 1:r + 1], s[l:r]  # either move left pointer by 1 or right pointer by 1
        #         return skipL == skipL[::-1] or skipR == skipR[::-1]  # check again to see if the remaining string is palindrome
        #     l, r = l + 1, r - 1
        # return True

        # method 2: put the process into a function and run it with updated pointers again
        def isPal(l, r):
            while l < r:
                if s[l] == s[r]:
                    l, r = l + 1, r - 1
                else:
                    return False
            return True

        n = len(s) - 1
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l, r = l + 1, r - 1
            else:
                return isPal(l, r - 1) or isPal(l + 1, r)
        return True
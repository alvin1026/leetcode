"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        res = ""

        for word in words:
            charArr = list(word) # convert a single word into an array of characters
            l, r = 0, len(charArr) - 1
            while l < r:
                charArr[l], charArr[r] = charArr[r], charArr[l]
                l += 1
                r -= 1
            res += "".join(charArr) + " "
        return res.strip() # strip the final space
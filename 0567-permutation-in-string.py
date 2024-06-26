"""
https://leetcode.com/problems/permutation-in-string/description/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26 # using Unicode code point to represent character, e.g. 'b' -> 1, where the first item in the list stores number of b(s)
        
        for i in range(len(s1)):  # set up two lists to compare
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0  # create additional variable to store number of character matches so that it could be updated immediately when the window slides
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0 # represent the character being dropped when window slides
        for r in range(len(s1), len(s2)):  # represent character being added when window slides.
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:  # the case when nth element transferring from being equal to NOT equal
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            
            l += 1
        return matches == 26

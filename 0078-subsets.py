"""
https://leetcode.com/problems/subsets/description/

Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # method 1: recursive
        # def getPowerSet(numbers):
        #     if numbers == []:
        #         return [[]]
        #     powerSet = []
        #     head = numbers[0]
        #     tail = numbers[1:]
        #     tailPowerSet = getPowerSet(tail)
        #     for tailSet in tailPowerSet:
        #         powerSet.append(tailSet + [head]) # add head element to each set in the tail power set
        #     powerSet = powerSet + tailPowerSet  # add the tail power set to the full power set
        #     return powerSet

        # return getPowerSet(nums)


        # method 2: depth-first search
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
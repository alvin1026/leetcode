"""
https://leetcode.com/problems/search-a-2d-matrix/description/

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

"""



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        """
        Set up the first binary search to find the array that contains the target.
        Set up another binary search to find the target within that array.
        Therefore, time complexity is log(m) + log(n) = log(m * n)
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1  # binary search to select a single list that contains target
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break  # find the row with row[0] <= target <= row[-1]

        if not (top <= bot):
            return False
        l, r = 0, COLS - 1  # binary search inside a single list
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

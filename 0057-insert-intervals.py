# question: https://leetcode.com/problems/insert-interval/description/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # 1. compare the end of the newInterval and start of existing interval:
        #       if it's smaller, then it's not overlapped with the rest of the intervals since the intervals is sorted in ascending order
        # 2. compare the start of newInterval with end of existing interval:
        #.      if it's bigger, then it's not overlapped with the existing interval but might be overlapped with the rest.
        # 3. Otherwise, it is overlapped with the existing interval:
        #       construct new interval with the min(starts of both intervals) and max(ends of both intervals)


        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res
from typing import List 

class MergeIntervals:
    """
    Problem: Merge Intervals (#56) 

    Key Insights: 
    1. Sort by first element 
    2. Merge if start <= lastEnd

    Time Complexity:
    1. sorting: O(n log n)
    2. iterate through intervals O(n)
    3. Total: O(n log n) time

    Space Complexity: 
    1. Create new output list: O(n) space or O(1) space if exclude output 
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd)
            else:
                output.append([start, end])
        return output 
    
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        ans = []
        ans.append(intervals[0])

        for start, end in intervals:
            last = ans[-1][1]

            if start <= last: ans[-1][1] = max(last, end)
            else: ans.append([start, end])
        
        return ans
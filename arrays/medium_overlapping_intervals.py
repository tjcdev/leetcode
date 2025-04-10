"""
We're going to have to go over the array at least once (at least O(n))

- sorting the input array would be the easiest
- two pointers for the start of the interval, move along updating the end pointer until we encounter a gap

Only other way is running binary searches when you pick up each intervals. Which is O(nlogn) which is the equiv. sorted()
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals = sorted(intervals)

        start = intervals[0][0]
        end = intervals[0][1]
        ans = []
        for interval in intervals[1:]:
            if interval[0] <= end:
                end = max(interval[1], end)
            else:
                ans.append([start, end])
                start = interval[0]
                end = interval[1]
        ans.append([start, end])

        return ans

"""
[[1,4],[4,5],[6, 7]]
start = 1
end = 4

first iteration: interval = [4,5]
    end = 5

second iteration: interval = [6, 7]
    ans = [[1, 5]]

loop finishes:
ans = [[1, 5], [6, 7]]
"""
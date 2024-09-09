"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def min_meeting_rooms(self, intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        s = 0
        e = 0
        res = 0
        count = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prev_e = 0
        intervals = sorted(intervals, key= lambda x : x.start)
        for itvl in intervals:
            if prev_e > itvl.start:
                return False
            prev_e = itvl.end
        return True
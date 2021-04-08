# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
#
# Example 1:
#
# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
# Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into
# one [1,5].
#
# Example 2:
#
# Intervals: [[6,7], [2,4], [5,9]]
# Output: [[2,4], [5,9]]
# Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].
#
# Example 3:
#
# Intervals: [[1,4], [2,6], [3,5]]
# Output: [[1,6]]
# Explanation: Since all the given intervals overlap, we merged them into one.

# sort the list by .start to make sure that in each every compare
# the start point of current interval always >= the last existing merged one
# removed one variants..
# now only focus on compare previous endpoint and current startpoint to check overlap
# e.g. last merged (2, 9), current (6, 7)
# 9 > 6, i.e. overlap exists

from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    if len(intervals) < 2:
        return intervals


    intervals.sort(key=lambda x: x.start)

    mergedIntervals = []
    for interval in intervals:
        # if current mergedIntervals is empty
        # or no overlap then append current interval
        if not mergedIntervals or mergedIntervals[-1].end < interval.start:
            mergedIntervals.append(interval)

        else:
            # there is overlap
            mergedIntervals[-1].end = max(interval.end, mergedIntervals[-1].end)

    return mergedIntervals


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(5, 6), Interval(7, 9)]):
        i.print_interval()
    print()

main()
# Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.
#
# Example 1:
#
# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
# Output: [[1,3], [4,7], [8,12]]
# Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
# Example 2:
#
# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
# Output: [[1,3], [4,12]]
# Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
# Example 3:
#
# Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
# Output: [[1,4], [5,7]]
# Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].

def insert(intervals, new_interval):
    merged = []
    new_interval_start = new_interval[0]
    new_interval_end = new_interval[1]
    index = 0

    # add all non-overlap intervals into merged[]
    # i.e. non-interval is on the left of new interval so finish before new interval start
    # i.e. interval.end < new_interval_start
    # and get replace_index
    while index < len(intervals) and intervals[index][1] < new_interval_start:
        merged.append((intervals[index]))
        index += 1

    # if index is not at the end of list,
    # now index points the first interval which needs to be merged with new_interval..
    # then merge intervals..
    # continue doing this until interval.start > new_interval_end ..
    # i.e. current interval start after new_interval ends..
    while index < len(intervals) and intervals[index][0] <= new_interval_end:
        new_interval[0] = min(intervals[index][0], new_interval_start)
        new_interval[1] = max(intervals[index][1], new_interval_end)
        index += 1

    merged.append(new_interval)

    # add rest of the intervals if still didnt reach end of the list
    while index < len(intervals):
        merged.append(intervals[index])
        index += 1

    return merged


def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
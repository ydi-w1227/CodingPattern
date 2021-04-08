# Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.
#
# Example 1:
#
# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
# Explanation: The output list contains the common intervals between the two lists.
# Example 2:
#
# Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
# Output: [5, 7], [9, 10]
# Explanation: The output list contains the common intervals between the two lists.

def merge(intervals_a, intervals_b):
    result = []
    i, j = 0, 0
    start, end = 0, 1
    while i < len(intervals_a) and j < len(intervals_b):
        # condition to have a overlap is
        # when ones start time lies within the another interval
        # a_overlap_b is when b starts before or same as a and also when a starts, b still didnt finish yet
        a_overlap_b = intervals_b[j][start] <= intervals_a[i][start] and \
                    intervals_b[j][end] >= intervals_a[i][start]

        #b_overlap_a is when a starts before or same as b and also when b starts, a still didnt finish yet
        b_overlap_a = intervals_a[i][start] <= intervals_b[j][start] and \
                    intervals_a[i][end] >= intervals_b[j][start]

        # if there is overlap between a and b, find overlap part
        if a_overlap_b or b_overlap_a:
            overlap_start = max(intervals_a[i][start], intervals_b[j][start])
            overlap_end = min(intervals_a[i][end], intervals_b[j][end])
            result.append((overlap_start, overlap_end))

        # move next which end first..
        # e.g. [[1, 4], [5, 8]], [[2, 6]]
        # need to move i to look for next interval in a to find overlap with b
        if intervals_a[i][end] < intervals_b[j][end]:
            i += 1
        else:
            j+= 1

    return result


def main():
  print("Intervals Intersection: " + str(merge([[1, 4], [5, 8]], [[2, 4]])))

  print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))

  print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()


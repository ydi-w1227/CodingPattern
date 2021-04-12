# Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.
#
# Example 1:
#
# Meetings: [[1,4], [2,5], [7,9]]
# Output: 2
# Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can
# occur in any of the two rooms later.
# Example 2:
#
# Meetings: [[6,7], [2,4], [8,12]]
# Output: 1
# Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.
# Example 3:
#
# Meetings: [[1,4], [2,3], [3,6]]
# Output:2
# Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to
# hold all the meetings.
#
# Example 4:
#
# Meetings: [[4,5], [2,3], [2,4], [3,5]]
# Output: 2
# Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].
#
# Here is a visual representation of Example 4:


from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # # min heap based on meeting.end, i.e. push
    def __lt__(self, other):
        print('calling __lt')
        return self.end < other.end

    def __str__(self):
        return str(self.start) + ' --> ' + str(self.end)

def min_meeting_rooms(meetings):
    # sort meetings by start time
    meetings.sort(key=lambda meeting: meeting.start)
    [print(meeting) for meeting in meetings]

    minRooms = 0

    # create min-heap of all meetings
    minHeap = []
    for meeting in meetings:
        print('current meeting is: ')
        print(meeting)
        print('current heap is: ')
        [print(minHeap) for minHeap in minHeap]


        # remove all the meetings that have ended
        while len(minHeap) > 0 and meeting.start >= minHeap[0].end:
            heappop(minHeap)
            print('after pop')
            [print(minHeap) for minHeap in minHeap]


        # add the current meeting into min_heap
        print('after pushing: ')
        heappush(minHeap, meeting)
        [print(minHeap) for minHeap in minHeap]


        # all active meetings are in the min_heap,
        # so we need rooms for all of them.
        minRooms = max(minRooms, len(minHeap))
        print('min room: ', minRooms)
    return minRooms


def main():
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5), Meeting(4, 4.5), Meeting(4.5, 6) ])))
    # print("Minimum meeting rooms required: " +
    #     str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    # print("Minimum meeting rooms required: " +
    #     str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    # print("Minimum meeting rooms required: " +
    #     str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    # print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    # [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


main()


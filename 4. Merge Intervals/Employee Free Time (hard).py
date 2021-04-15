# For ‘K’ employees, we are given a list of intervals representing the working hours of each employee. Our goal is to find out if there is a free interval that is common to all employees. You can assume that each list of employee working hours is sorted on the start time.
#
# Example 1:
#
# Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
# Output: [3,5]
# Explanation: Both the employees are free between [3,5].
# Example 2:
#
# Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
# Output: [4,6], [8,9]
# Explanation: All employees are free between [4,6] and [8,9].
# Example 3:
#
# Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]]
# Output: [5,7]
# Explanation: All employees are free between [5,7].

# >>> x = [["a","b"], ["c"]]
# >>> [inner
# ...     for outer in x
# ...         for inner in outer]
# ['a', 'b', 'c']


from __future__ import print_function
from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

# normal solution
def find_employee_free_time(schedule):
    result = []
    total_schedule =  [elem for iterable in schedule for elem in iterable]
    print(total_schedule)
    total_schedule.sort(key=lambda s:s.start)

    # print
    # [s.print_interval() for s in total_schedule]
    # print('\n')

    for index in range(1, len(total_schedule)):
        if total_schedule[index-1].end < total_schedule[index].start:
            # no overlap
            result.append(Interval(total_schedule[index-1].end, total_schedule[index].start))

    return result

# use heap
class EmployeeInterval:
    # interval representing employee's working hours
    # index of the list containing working hours of this employee
    # index of the interval in the employee list
    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval      = interval
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex

    def __lt__(self, other):
        # min heap based on interval.start
        return self.interval.start < other.interval.start

    def print_interval(self):
        print("[" + str(self.interval.start) + "--> " + str(self.interval.end) +  ", "
              + str(self.employeeIndex) + ', ' + str(self.intervalIndex) + "]", end='')

# schedules for each employer is sorted
def find_employee_free_time_2(schedule):
    if schedule is None:
        return []

    n = len(schedule)
    result, min_heap = [], []
    print(n)
    # insert the first interval of each employee to the queue
    for i in range(n):
        heappush(min_heap,EmployeeInterval(schedule[i][0], i, 0))

    print('current min heap ')
    print([n.print_interval() for n in min_heap])
    print('\n')
    # get the smallest start time interval
    # make sure only pop one (second smallest, i.e. queueTop) at a time
    # and add one from same employee (i.e. queueTop) at a time if exists
    previousInterval = min_heap[0].interval
    while min_heap:
        queueTop = heappop(min_heap)
        print('current  smallest previousInterval is')
        previousInterval.print_interval()
        print('\n')
        print('second smallest queueTop is')
        queueTop.print_interval()
        print('\n')

        print('current min heap ')
        print([n.print_interval() for n in min_heap])
        print('\n')


        # if previousInterval is not overlapping with the next interval,
        # the new smallest interval for next loop will be queueTop
        # insert a free interval
        if previousInterval.end < queueTop.interval.start:
            print('no overlap, append')
            result.append(Interval(previousInterval.end, queueTop.interval.start))
            previousInterval = queueTop.interval

        else:
            print('there is an overlap')
            # overlapping intervals, update the previousInterval if needed
            # i.e. update comparative bigger end time one as a new smallest interval
            if previousInterval.end < queueTop.interval.end:
                previousInterval = queueTop.interval
                print(previousInterval.print_interval())
                print('\n')

        # if there are more intervals available for the same employee (second smallest),
        # add their next interval
        employeeSchedule = schedule[queueTop.employeeIndex]
        print(queueTop.employeeIndex)
        if len(employeeSchedule) > queueTop.intervalIndex + 1:
            print('there is more intervals for employee ', queueTop.employeeIndex)
            heappush(min_heap, EmployeeInterval(employeeSchedule[queueTop.intervalIndex + 1], queueTop.employeeIndex,
                                               queueTop.intervalIndex + 1))

    return result


def main():

    # input = [[Interval(1, 3), Interval(5, 6)], [
    #     Interval(2, 3), Interval(6, 8)]]
    # print("Free intervals: ", end='')
    # for interval in find_employee_free_time_2(input):
    #     interval.print_interval()
    # print()

    # input = [[Interval(1, 4), Interval(9, 12)], [
    #     Interval(2, 3)], [Interval(6, 8)]]
    # print("Free intervals: ", end='\n')
    # for interval in find_employee_free_time_2(input):
    #     interval.print_interval()
    # print()
    #

    input = [[Interval(1, 5), Interval(10, 12)], [
        Interval(2, 3) ], [Interval(3, 4), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time_2(input):
        interval.print_interval()
    print()


main()

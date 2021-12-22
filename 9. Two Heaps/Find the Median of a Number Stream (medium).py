# Design a class to calculate the median of a number stream. The class should have the following two methods:
#
# insertNum(int num): stores the number in the class
# findMedian(): returns the median of all numbers inserted in the class
# If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.
#
from heapq import *

class MedianOfAStream:
    maxHeap = []  # containing first half of numbers, max on top, i.e. lower index
    minHeap = []  # containing second half of numbers, min on top, i.e. lower index

    def insert_num(self, num):
        print(num)
        # push to maxHeap first
        # or if top of max heap is greater or equals to than num, then num should be top of max heap
        # make num negative is to make bigger value on lower index (i.e. closer to top) which will be pop first
        if not self.maxHeap or -self.maxHeap[0] >= num:
            print('push to max heap')
            heappush(self.maxHeap, -num)
            print(self.maxHeap)
        else:
            print('push to min heap')
            heappush(self.minHeap, num)
            print(self.minHeap)

        # either both the heaps will have equal number of elements or max-heap will have one
        # more element than the min-heap
        # otherwise balance out two queues
        # heappush: push to the beginning of queue
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
            print('balancing 1 ..')
            print(self.maxHeap)
            print(self.minHeap)

        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
            print('balancing 2 ..')
            print(self.maxHeap)
            print(self.minHeap)

    def find_median(self):

        if len(self.maxHeap) == len(self.minHeap):
            # we have even number of elements, take the average of middle two elements
            return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0

        # because max-heap will have one more element than the min-heap
        return -self.maxHeap[0] / 1.0


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()

# Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.
# Input: nums=[1, 2, -1, 3, 5], k = 3
# Output: [1.0, 2.0, 3.0]
# Explanation: Lets consider all windows of size ‘3’:
#
# [1, 2, -1, 3, 5] -> median is 1.0
# [1, 2, -1, 3, 5] -> median is 2.0
# [1, 2, -1, 3, 5] -> median is 3.0

from heapq import *
import heapq

class SlidingWindowMedian:


    def find_sliding_window_median(self, nums, k):
        result = []

        i = 0
        length = len(nums)
        while i < length - k + 1:
            sub_array = nums[i: i + k]
            i += 1
            median = self.find_median(sub_array)
            result.append(median)
        return result

    def find_median(self, sub_array):

        maxHeap = []
        minHeap = []
        maxHeap, minHeap = self.process_subarray(sub_array)
        if len(maxHeap) == len(minHeap):
            return (-maxHeap[0] + minHeap[0]) / 2.0
        return -maxHeap[0] / 1.0

    def process_subarray(self, sub_array):
        maxHeap = []
        minHeap = []
        for index in range(len(sub_array)):
            if not maxHeap or -maxHeap[0] >= sub_array[index]:
                heappush(maxHeap, -sub_array[index])
            else:
                heappush(minHeap, sub_array[index])


        if len(maxHeap) > len(minHeap) + 1:
            heappush(minHeap, -heappop(maxHeap))

        elif len(maxHeap) < len(minHeap):
            heappush(maxHeap, -heappop(minHeap))

        return maxHeap, minHeap


class SlidingWindowMedian_official:
  def __init__(self):
    self.maxHeap, self.minHeap = [], []

  def find_sliding_window_median(self, nums, k):
    result = [0.0 for x in range(len(nums) - k + 1)]
    for i in range(0, len(nums)):
      if not self.maxHeap or nums[i] <= -self.maxHeap[0]:
        heappush(self.maxHeap, -nums[i])
      else:
        heappush(self.minHeap, nums[i])

      self.rebalance_heaps()

      if i - k + 1 >= 0:  # if we have at least 'k' elements in the sliding window
        # add the median to the the result array
        if len(self.maxHeap) == len(self.minHeap):
          # we have even number of elements, take the average of middle two elements
          result[i - k + 1] = -self.maxHeap[0] / \
                              2.0 + self.minHeap[0] / 2.0
        else:  # because max-heap will have one more element than the min-heap
          result[i - k + 1] = -self.maxHeap[0] / 1.0

        # remove the element going out of the sliding window
        elementToBeRemoved = nums[i - k + 1]
        if elementToBeRemoved <= -self.maxHeap[0]:
          self.remove(self.maxHeap, -elementToBeRemoved)
        else:
          self.remove(self.minHeap, elementToBeRemoved)

        self.rebalance_heaps()

    return result

  # removes an element from the heap keeping the heap property
  def remove(self, heap, element):
    ind = heap.index(element)  # find the element
    # move the element to the end and delete it
    heap[ind] = heap[-1]
    del heap[-1]
    # we can use heapify to readjust the elements but that would be O(N),
    # instead, we will adjust only one element which will O(logN)
    if ind < len(heap):
      heapq._siftup(heap, ind)
      heapq._siftdown(heap, 0, ind)

  def rebalance_heaps(self):
    # either both the heaps will have equal number of elements or max-heap will have
    # one more element than the min-heap
    if len(self.maxHeap) > len(self.minHeap) + 1:
      heappush(self.minHeap, -heappop(self.maxHeap))
    elif len(self.maxHeap) < len(self.minHeap):
      heappush(self.maxHeap, -heappop(self.minHeap))



def main():

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()

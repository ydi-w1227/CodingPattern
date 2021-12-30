# Given an unsorted array of numbers, find the ‘K’ largest numbers in it.
#
# Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.
#
# Example 1:
#
# Input: [3, 1, 5, 12, 2, 11], K = 3
# Output: [5, 12, 11]

# Example 2:
#
# Input: [5, 12, 11, -1, 12], K = 3
# Output: [12, 11, 12]


# create a minheap to keep top #k of values..
# compare with root.. because root is the smallest number of current k numbers
# if larger than root, then add it in..
# hence, heap will contain #k of largest values

from heapq import *


def find_k_largest_numbers(nums, k):
    minHeap = []

    for i in range(k):
        heappush(minHeap, nums[i])

    for j in range(k, len(nums)):
        if minHeap[0] < nums[j]:
            heappop(minHeap)
            heappush(minHeap, nums[j])

    return list(minHeap)


def main():

    print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()


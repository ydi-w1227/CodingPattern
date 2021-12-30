# Given an unsorted array of numbers, find Kth smallest number in it.
#
# Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.
#
# Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.
#
# Example 1:
#
# Input: [1, 5, 12, 2, 11, 5], K = 3
# Output: 5
# Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

# Example 2:
#
# Input: [1, 5, 12, 2, 11, 5], K = 4
# Output: 5
# Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].

# Example 3:
#
# Input: [5, 12, 11, -1, 12], K = 3
# Output: 11
# Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].

# note: heapq will always save smallest value on the root.. so if making a maxHeap, need to save values as negative..
# make what you want for result at the root of the heap


# in this case, find kth smallest numbers..
# if we want kth number on the root, means this number originally is the largest of those #k values
# because the larger the value is, the smaller the negative version is.. it will closer to root..
# so we are using maxHeap here to make original larger value (smaller negative value) on root..

# so compare value with root..
# if the negative of the number is smaller than root, which means it is originally larger.
# e.g. say [-12, -1, -5], -12 will be the root, as it is smallest (originally it is 12)
#       next value is 2 is smaller than 12 and we want it
#       so compare -2 with -12(root).. -2 > -12 so we are going to add -2 in..
#       hence, it looks like we are adding larger negative value every time and re-adjust heap..[-5, -1, -2]
#       but we are actually keeping smaller original numbers

# again, root is always the smallest negative value among #k values.. i.e. original larger..
# then think in a way that, result will be [-5, -1, -2], k = 3
# -5 will be the smallest among the heap so it will be saved on root.. which original value 5 is the third smallest value..

from heapq import *

def find_Kth_smallest_number(nums, k):
    maxHeap = []
    # put first k numbers in the max heap
    for i in range(k):
        heappush(maxHeap, -nums[i])

    # go through the remaining numbers of the array, if the number from the array is smaller than the
    # top(biggest) number of the heap, remove the top number from heap and add the number from array
    for i in range(k, len(nums)):
        if -nums[i] > maxHeap[0]:
            heappop(maxHeap)
            heappush(maxHeap, -nums[i])

    print(maxHeap)
    # the root of the heap has the Kth smallest number
    return -maxHeap[0]


def main():

    print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
    print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

    print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()

# Given a string and a number ‘K’, find if the string can be rearranged
# such that the same characters are at least ‘K’ distance apart from each other.
#
# Example 1:
#
# Input: "mmpp", K=2
# Output: "mpmp" or "pmpm"
# Explanation: All same characters are 2 distance apart.
# Example 2:
#
# Input: "Programming", K=3
# Output: "rgmPrgmiano" or "gmringmrPoa" or "gmrPagimnor" and a few more
# Explanation: All same characters are 3 distance apart.
# Example 3:
#
# Input: "aab", K=2
# Output: "aba"
# Explanation: All same characters are 2 distance apart.
# Example 4:
#
# Input: "aappa", K=3
# Output: ""
# Explanation: We cannot find an arrangement of the string where any two 'a' are 3 distance apart.

from heapq import *
from collections import deque


def reorganize_string(str, k):
    if k <= 1:
        return str

    charFrequencyMap = {}
    for char in str:
        charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

    maxHeap = []
    # add all characters to the max heap
    for char, frequency in charFrequencyMap.items():
        heappush(maxHeap, (-frequency, char))

    queue = deque()
    resultString = []
    while maxHeap:
        frequency, char = heappop(maxHeap)
        # append the current character to the result string and decrement its count
        resultString.append(char)
        # decrement the frequency and append to the queue
        queue.append((char, frequency+1))
        if len(queue) == k:
            char, frequency = queue.popleft()
            if -frequency > 0:
                heappush(maxHeap, (frequency, char))

    # if we were successful in appending all the characters to the result string, return it
    return ''.join(resultString) if len(resultString) == len(str) else ""


def main():
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))


main()

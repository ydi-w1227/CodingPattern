# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
#
# Example 1:
#
# Input: [2, 1, 5, 1, 3, 2], k=3
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
# Example 2:
#
# Input: [2, 3, 4, 1, 5], k=2
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

import unittest

def max_sub_array_of_size_k(k, arr):
  maxValue, temp = 0, 0
  start = 0

  for end in range(len(arr)):
    temp += arr[end]
    if end >= k - 1:
      if temp > maxValue:
        maxValue = temp
      temp -= arr[start]
      start += 1
  return maxValue

class Test(unittest.TestCase):

    def test_max_sub_array_of_size_k(self):
        data1 = [3, [2, 1, 5, 1, 3, 2]]
        data2 = [2, [2, 3, 4, 1, 5]]
        self.assertEqual(9, max_sub_array_of_size_k(data1[0], data1[1]))
        self.assertEqual(7, max_sub_array_of_size_k(data2[0], data2[1]))

if __name__ == "__main__":
    unittest.main()
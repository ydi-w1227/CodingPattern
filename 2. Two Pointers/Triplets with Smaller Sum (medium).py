# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.
#
# Example 1:
#
# Input: [-1, 0, 2, 3], target=3
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
# Example 2:
#
# Input: [-1, 4, 2, 1, 3], target=5
# Output: 4
# Explanation: There are four triplets whose sum is less than the target:
#    [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]

def triplet_with_smaller_sum(arr, target):
  count = 0
  arr.sort()

  for i in range(len(arr)):
      low = i + 1
      high = len(arr) - 1
      remain = target - arr[i]
      while low < high:
          print('low is: ', arr[low])
          print('high is: ', arr[high])

          if arr[low] + arr[high] < remain:
              # after low and high are set, which sum of values are smaller than remain
              # high is not going to change anymore, low is going to + 1
              # so currenly value between low and high all satisfied < remain this criteria
              count += high - low
              low += 1
          else:
              high -= 1
  return count

def triplet_with_smaller_sum_2(arr, target):
  triplets = []
  arr.sort()

  for i in range(len(arr)):
      low = i + 1
      high = len(arr) - 1
      remain = target - arr[i]
      while low < high:
          print('low is: ', arr[low])
          print('high is: ', arr[high])

          if arr[low] + arr[high] < remain:
              for j in range(high, low, -1):
                  triplets.append([arr[i], arr[low], arr[j]])
              low += 1
          else:
              high -= 1
  return triplets

print(triplet_with_smaller_sum([-1, 0, 2, 3], target=3))
print(triplet_with_smaller_sum_2([-1, 0, 2, 3], target=3))
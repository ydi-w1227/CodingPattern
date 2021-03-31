# We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:
#
# If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
# If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
# Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.
#
# Example 1:
#
# Input: [1, 2, -1, 2, 2]
# Output: true
# Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0
# Example 2:
#
# Input: [2, 2, -1, 2]
# Output: true
# Explanation: The array has a cycle among indices: 1 -> 3 -> 1
# Example 3:
#
# Input: [2, 1, -1, -2]
# Output: false
# Explanation: The array does not have any cycle.


# this solution solved problems.. but it is not O(n)
def circular_array_loop_exists_1(arr):
    arr_len = len(arr)

    for index in range(len(arr)):
        checkedIndex = []
        # make sure is not negative
        next_index = (index + arr[index]) % arr_len
        checkedIndex.append(index)

        currentStart = arr[index]
        start_isPositive = checkPositive(currentStart)
        print('\n')
        print('start sum_index: ', index)
        print('which value is: ', currentStart)
        print('current is positive?: ', start_isPositive)
        print('checkedIndex: ', checkedIndex)
        print('next index is : ', next_index)
        print('\n')


        while len(checkedIndex) <= arr_len:
            print('current index is : ', next_index)
            print('current value is : ', arr[next_index])

            # if the value towards different direction
            # then check the next for loop, so break!
            cur_isPositive = checkPositive(arr[next_index])
            print('current value is positive?: ', cur_isPositive)
            if start_isPositive != cur_isPositive:
                print('current value is not in same direction, break!')
                break

            # if current value is in same direction but already visited
            # then there is a loop so break
            if next_index in checkedIndex:
                # if loop is only one element
                if checkedIndex[-1] == next_index:
                    print(checkedIndex)
                    break
                print(checkedIndex)
                return True

            # first time visit current index, add in checkedIndex
            checkedIndex.append(next_index)
            print('current checkedIndex is: ', checkedIndex)

            # add current value and compute next time index
            next_index += arr[next_index]
            print('next step will be index : ', next_index)

            if next_index >= arr_len or next_index < 0:
                next_index = next_index % arr_len
                print('next_index after modulo: ', next_index)

    # didnt find any cycle
    return False


def checkPositive(num):
    if num > 0:
        return 1
    elif num == 0:
        return 0
    else:
        return -1

# https://leetcode.com/problems/circular-array-loop/discuss/232417/Python-simple-solution-beats-100-with-O(1)-space
# no need to store visited points.. condition is visited nodes more than len(nums)
# another option: https://leetcode.com/problems/circular-array-loop/discuss/784810/Python%3A-Fast-Slow-pointers-O(n)-time-%2B-O(1)-space
def circularArrayLoop(nums: 'List[int]') -> 'bool':
    """
        :type nums: List[int]
        :rtype: bool
    """
    n = len(nums)
    for i, num in enumerate(nums):
        linkLength = 0
        j = i
        forward = nums[j] > 0
        while True:
            # or if forward != (nums[j] > 0)
            if (forward and nums[j] < 0) or (not forward and nums[j] > 0):
                break
            nextj = (j + nums[j] + n) % n
            if nextj == j:
                break
            j = nextj
            linkLength += 1
            if linkLength > n:
                return True
    return False


def circular_array_loop_exists_official(arr):
  for i in range(len(arr)):
    is_forward = arr[i] >= 0  # if we are moving forward or not
    slow, fast = i, i

    # if slow or fast becomes '-1' this means we can't find cycle for this number
    while True:
      # move one step for slow pointer
      slow = find_next_index(arr, is_forward, slow)
      # move one step for fast pointer
      fast = find_next_index(arr, is_forward, fast)
      if (fast != -1):
        # move another step for fast pointer
        fast = find_next_index(arr, is_forward, fast)
      if slow == -1 or fast == -1 or slow == fast:
        break

    if slow != -1 and slow == fast:
      return True

  return False


def find_next_index(arr, is_forward, current_index):
  direction = arr[current_index] >= 0

  if is_forward != direction:
    return -1  # change in direction, return -1

  next_index = (current_index + arr[current_index]) % len(arr)

  # one element cycle, return -1
  if next_index == current_index:
    next_index = -1

  return next_index

def main():
    # print(circular_array_loop_exists([2, 1]))
    # print(circular_array_loop_exists([1]))

    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    # print(circular_array_loop_exists([2, 2, -1, 2]))
    # print(circular_array_loop_exists([2, 1, -1, -2]))
    # print(circular_array_loop_exists([2, 2, 1, 2]))


    # print(circular_array_loop_exists([-2, -2, -1, -2]))
    # print(circular_array_loop_exists([-1,-2,-3,-4,-5]))
    # print(circularArrayLoop([3,1,2]))

main()
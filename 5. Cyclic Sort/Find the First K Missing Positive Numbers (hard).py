# Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.
#
# Example 1:
#
# Input: [3, -1, 4, 5, 5], k=3
# Output: [1, 2, 6]
# Explanation: The smallest missing positive numbers are 1, 2 and 6.
# Example 2:
#
# Input: [2, 3, 4], k=3
# Output: [1, 5, 6]
# Explanation: The smallest missing positive numbers are 1, 5 and 6.
# Example 3:
#
# Input: [-2, -3, 4], k=2
# Output: [1, 2]
# Explanation: The smallest missing positive numbers are 1 and 2.

# add numbers which is not at right index to set()
# for checking later if the additional numbers is in list already
# e.g. still one value needs to be added in missing Numbers,
# after sorting list = [5, 2, 3, 4], length of list is 4, k = 2
# normally apart from 1 will add 5 into result list, but 5 already in the list

def find_first_k_missing_positive(nums, k):
    missingNumbers = []
    i = 0
    n = len(nums)
    while i < n:
        right_index = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[right_index]:
            nums[i], nums[right_index] = nums[right_index], nums[i]
        else:
            i += 1

    print(nums)


    extra_numbers = set()
    for index in range(n):
        if len(missingNumbers) < k:
            if nums[index] != index + 1:
                missingNumbers.append(index + 1)
                extra_numbers.add(nums[index])

    acc = 1
    while len(missingNumbers) < k:
        candidate_number = acc + n
        if candidate_number not in extra_numbers:
            missingNumbers.append(candidate_number)
        acc += 1

    return missingNumbers

def main():
  print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
  print(find_first_k_missing_positive([2, 3, 4], 3))
  print(find_first_k_missing_positive([-2, -3, 4], 2))


main()

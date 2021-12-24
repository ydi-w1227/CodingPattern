# Given a set of distinct numbers, find all of its permutations.
#
# Permutation is defined as the re-arranging of the elements of the set.
# For example, {1, 2, 3} has the following six permutations:
#
# {1, 2, 3}
# {1, 3, 2}
# {2, 1, 3}
# {2, 3, 1}
# {3, 1, 2}
# {3, 2, 1}
# If a set has ‘n’ distinct elements it will have n!n! permutations.
#
# Example 1:
#
# Input: [1,3,5]
# Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]


from collections import deque


# double-ended queue solution
# make it like layer by layer.. each layer with different # of numbers to create permutations..
# until list all the possibilities of current layer, then go to next layer
def find_permutations(nums):
    numsLength = len(nums)
    result = []
    permutations = deque()
    permutations.append([])

    # loop through nums
    for currentNumber in nums:
        # we will take all existing permutations and add the current number to create new permutations
        n = len(permutations)
        print('length: ', n)

        # for each existing current permutation, need to find how many index could insert
        # so that we could create new permutations (pop out old one, and push back new one)
        for _ in range(n):
            print('start..')
            oldPermutation = permutations.popleft()
            print(permutations)
            print('old permutation: ' , oldPermutation)
            # create a new permutation by adding the current number at every position
            # 0-len(oldPermutation => positions..
            for j in range(len(oldPermutation)+1):
                newPermutation = list(oldPermutation)
                print('new permutation before: ' , newPermutation)
                newPermutation.insert(j, currentNumber)
                print('after insert..')
                print(newPermutation)

                # if # of values for current permutations == # of nums
                # then that means it is the final result
                # otherwise, add back to permutations list and go to next loop
                if len(newPermutation) == numsLength:
                    result.append(newPermutation)
                else:
                    permutations.append(newPermutation)
                    print('append permutations,,')
                    print(permutations)
    print('result: ', result)
    return result

# recursive solution
#  i feel it loops like a tree to go deeper and deeper.. till the end, then come back
def generate_permutations(nums):
  result = []
  generate_permutations_recursive(nums, 0, [], result)
  return result


def generate_permutations_recursive(nums, index, currentPermutation, result):
    if index == len(nums):
        result.append(currentPermutation)
    else:
        # create a new permutation by adding the current number at every position
        # loop through
        print('loop though: ', len(currentPermutation) + 1)

        for i in range(len(currentPermutation)+1):
            print('i is: ', i)
            newPermutation = list(currentPermutation)
            newPermutation.insert(i, nums[index])
            print('after insert: ', newPermutation)
            generate_permutations_recursive(
            nums, index + 1, newPermutation, result)

def main():
    # print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))
    print("Here are all the permutations: " + str(generate_permutations([1, 3, 5])))


main()
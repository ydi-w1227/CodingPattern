# Given a set with distinct elements, find all of its distinct subsets.
#
# Example 1:
#
# Input: [1, 3]
# Output: [], [1], [3], [1,3]
# Example 2:
#
# Input: [1, 5, 3]
# Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]

def find_subsets(nums):
    subsets = []
    # start by adding the empty subset
    subsets.append([])
    print(subsets)

    for currentNumber in nums:
        print('current number is: ', str(currentNumber))
        # we will take all existing subsets and insert the current number in them to create new subsets
        n = len(subsets)
        print('length of subsets: ', n)
        print(subsets)
        for i in range(n):
            print('start..', i)
            # create a new subset from the existing subset and insert the current element to it
            set1 = list(subsets[i])
            print(subsets[i])
            print(set1)
            set1.append(currentNumber)
            print(set1)
            subsets.append(set1)
            print(subsets)


    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    # print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()

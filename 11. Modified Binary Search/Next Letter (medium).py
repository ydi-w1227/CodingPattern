# Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than a given ‘key’.
#
# Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter. This also means that the smallest letter in the given array is greater than the last letter of the array and is also the first letter of the array.
#
# Write a function to return the next letter of the given ‘key’.
#
# Example 1:
#
# Input: ['a', 'c', 'f', 'h'], key = 'f'
# Output: 'h'
# Explanation: The smallest letter greater than 'f' is 'h' in the given array.
# Example 2:
#
# Input: ['a', 'c', 'f', 'h'], key = 'b'
# Output: 'c'
# Explanation: The smallest letter greater than 'b' is 'c'.
# Example 3:
#
# Input: ['a', 'c', 'f', 'h'], key = 'm'
# Output: 'a'
# Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.
# Example 4:
#
# Input: ['a', 'c', 'f', 'h'], key = 'h'
# Output: 'a'
# Explanation: As the array is assumed to be circular, the smallest letter greater than 'h' is 'a'.


# remember at the end.. the condition of breaking the loop is (start == end + 1)
#   - either start moves (key >= mid) or end moves (key < mid)
# same as before, start always point to next element when current mid < key, which is larger than current mid....
#      - which proved previous mid is a boundary
#      - e.g. a, c, f, h, key = b
#                           s1 = a, e1 = h, m1 = c => c > b => which means right side of c (include c as mid) is larger than a
#                           s2 = a, e2 = a, m2 = a => a < b => which means (previous mid) - 1 < a, i.e. previous mid is a boundary..
#                           so start = mid + 1 and points to c, which makes sense as start point to the next element
#
#      - another example, a, c, f, h, key = f
#                           s1 = a, e1 = h, m1 = c => c < f => which means left side of c (include c as mid) is smaller than f
#                           s2 = f, e2 = h, m2 = f => f == f => which will be ignored as it is not next element
#                           s3 = h, e3 = h, m3 = h => h > f => which means (previous mid) as a boundary of <= f
#                                                           => and (previous mid) + 1 is larger than f,
#                                                           => i.e. where the current start points to and it is what we want
#
# if start == length, means circular.. means should return index 0
# and max of start is length..

# when key < letters[mid] => end = mid - 1
# when key == letters[mid] => ignore it, and need to return next index.. so start = mid + 1
# when key > letters[mid] => start = mid + 1
# when key is larger than letters[end] => consider as circular..
#   since start == end + 1, start only would be able to == length, i.e. index of end element + 1
#   here using % length, if index == length, then will be 0, which is what we want as index 0

def search_next_letter(letters, key):
    n = len(letters)

    start, end = 0, n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key < letters[mid]:
            end = mid - 1
        else: # key >= letters[mid]:
            start = mid + 1

    # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end+1'
    return letters[start % n]


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()

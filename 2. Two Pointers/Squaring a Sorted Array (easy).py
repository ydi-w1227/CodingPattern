# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.
#
# Example 1:
#
# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]
# Example 2:
#
# Input: [-3, -1, 0, 1, 2]
# Output: [0, 1, 1, 4, 9]


def make_squares(arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    p1 = 0
    p2 = n - 1
    largestSquareIndex = n - 1

    while p1 <= p2:
        p1_s = arr[p1]**2
        p2_s = arr[p2]**2
        if p1_s < p2_s:
            squares[largestSquareIndex] = p2_s
            p2 -= 1
        else:
            squares[largestSquareIndex] = p1_s
            p1 += 1
        largestSquareIndex -= 1
    print(squares)
    return squares


print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
#print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))

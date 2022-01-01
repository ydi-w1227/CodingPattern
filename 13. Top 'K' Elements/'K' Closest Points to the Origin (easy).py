# Given an array of points in a 2D2D plane, find ‘K’ closest points to the origin.
#
# Example 1:
#
# Input: points = [[1,2],[1,3]], K = 1
# Output: [[1,2]]
# Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
# The Euclidean distance between (1, 3) and the origin is sqrt(10).
# Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.
# Example 2:
#
# Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
# Output: [[1, 3], [2, -1]]

from __future__ import print_function
from heapq import *


# __lt__ method will compare distance, get called when using heappush or after calling heappop to re-adjust the heap
# self -> the object which is going to be added when push or later node when pop(?)
# other -> the object which is currently on max-heap[0] when push or earlier node when pop(?)
# if return true, means other has smaller distance to origin, then this point wont be on the root
# i.e. when false, means other has larger distance which makes other (i.e. larger dist point) on the root
# if there are more than two element in the heap, it wont't compare every elements.. will only do once with current root. e.g. k = 3
# if there are only one element left in heap, it wont be called. e.g. k = 2 after pop only 1 element left

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # used for max-heap
    # arrange point with larger distance from origin on the front of heap
    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def distance_from_origin(self):
        # ignoring sqrt to calculate the distance
        return (self.x * self.x) + (self.y * self.y)

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


def find_closest_points(points, k):
    maxHeap = []
    # put first 'k' points in the max heap
    for i in range(k):
        heappush(maxHeap, points[i])

    # go through the remaining points of the input array, if a point is closer to the origin than the top point
    # of the max-heap, remove the top point from heap and add the point from the input array
    for i in range(k, len(points)):
        if points[i].distance_from_origin() < maxHeap[0].distance_from_origin():
            heappop(maxHeap)
            heappush(maxHeap, points[i])

    # the heap has 'k' points closest to the origin, return them in a list
    return list(maxHeap)


def main():

    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()

    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1), Point(0, 0)], 3)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()

main()

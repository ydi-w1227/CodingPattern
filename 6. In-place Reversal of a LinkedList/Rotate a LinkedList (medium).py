# Given the head of a Singly LinkedList and a number ‘k’,
# rotate the LinkedList to the right by ‘k’ nodes.

from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def rotate(head, rotations):
    last_node = head
    list_length = 1
    # traverse the linked list
    while last_node.next is not None:
        last_node = last_node.next
        list_length += 1
    print(list_length)

    # connect start and end of linked list
    last_node.next = head

    # no point of doing more than the length of sublist..
    rotations = rotations % list_length
    new_end = head
    # do rotation and get start node..
    # i.e. looking for new end node..
    while rotations > 1:
        new_end = new_end.next
        rotations -= 1
    # next of new_end is new start, let head points to it
    head = new_end.next
    # make new_end points to null
    new_end.next = None

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 3)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


main()

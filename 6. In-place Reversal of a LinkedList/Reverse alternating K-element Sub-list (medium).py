# Given the head of a LinkedList and a number ‘k’,
# reverse every alternating ‘k’ sized sub-list starting from the head.
#
# If, in the end, you are left with a sub-list with less than ‘k’ elements,
# reverse it too.

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


def reverse_alternate_k_elements(head, k):
    previous = None
    current = head
    while current is not None:
        last_node_of_previous = previous
        last_node_of_sublist  = current
        i = 0
        while i < k and current is not None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            i += 1
        if last_node_of_previous is not None:
            last_node_of_previous.next = previous
        else:
            head = previous
        last_node_of_sublist.next = current

        # skip k nodes
        j = 0
        while current is not None and j < k:
            previous = current
            current= current.next
            j += 1
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next.next.next = Node(9)


    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()

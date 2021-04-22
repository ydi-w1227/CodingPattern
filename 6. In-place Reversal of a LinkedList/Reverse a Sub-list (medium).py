# Given the head of a LinkedList and two positions ‘p’ and ‘q’,
# reverse the LinkedList from position ‘p’ to ‘q’.


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


def reverse_sub_list(head, p, q):
    if p == q:
        return head
    start, prev = head, head
    # Skip the first p-1 nodes to reach the node at position p
    while p - 1 > 0:
        # Remember the node at position p-1 to be used later
        # to connect with reverse
        prev = start
        start = prev.next
        p -= 1

    # start.print_list()
    # prev.print_list()

    # Reverse the nodes from p to q
    new_start, new_end, reversed_end_point = reverse(start, p, q)
    new_start.print_list()
    new_end.print_list()
    reversed_end_point.print_list()

    # connect p-1 and q+1 node to the reversed sublist
    prev.next = new_start
    reversed_end_point.next = new_end
    return head

def reverse(head, p, q):
    reversed_end_point, prev, temp = head, None, None
    # reversed_end_point points to the first point before reverse,
    # i.e. end node after reversed
    # after this while loop, prev points to node q (reversed),
    # head prints from node q + 1
    while p != q:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
        p += 1
    head.print_list()
    return prev, head, reversed_end_point

def reverse_sub_list_official(head, p, q):
    if p == q:
        return head

    # after skipping 'p-1' nodes, current will point to 'p'th node
    current, previous = head, None
    i = 0
    while current is not None and i < p - 1:
        previous = current
        current = current.next
        i += 1

    # we are interested in three parts of the LinkedList, the part before index 'p',
    # the part between 'p' and 'q', and the part after index 'q'
    last_node_of_first_part = previous
    # after reversing the LinkedList 'current' will become the last node of the sub-list
    last_node_of_sub_list = current
    next = None  # will be used to temporarily store the next node

    i = 0
    # reverse nodes between 'p' and 'q'
    while current is not None and i < q - p + 1:
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1

    # connect with the first part
    if last_node_of_first_part is not None:
        # 'previous' is now the first node of the sub-list
        last_node_of_first_part.next = previous
    # this means p == 1 i.e., we are changing the first node (head) of the LinkedList
    else:
        head = previous

    # connect with the last part
    last_node_of_sub_list.next = current
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
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()

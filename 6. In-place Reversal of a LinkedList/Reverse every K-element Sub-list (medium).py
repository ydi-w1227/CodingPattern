# Given the head of a LinkedList and a number ‘k’,
# reverse every ‘k’ sized sub-list starting from the head.
#
# If, in the end, you are left with a sub-list with less than ‘k’ elements,
# reverse it too.
#

# for reverse k elements, previous will move to new start (original_end) of sublist
# current will move to start of next sublist
# after reverse, need to connect previous sublist
# last_node_of_previous_part need to keep this points to last node of previous sublist
# which is 1) if last node of previous sublist doesnt exist (1st loop), then head points to previous
#          2) if last node of previous sublist exists,
#               then last node of previous sublist.next = previous (new start of this sublist after reverse)
# connect next sublist using last_node_of_sub_list.next = current
#           last_node_of_sub_list points to new end (original start of current sublist, i.e. "current" in previous loop)
#
# this process will end until current points to None which is the end of the linked list
# In this process, initialize  last_node_of_previous_part = previous (new end of previous sublist, which is also last_node_of_sub_list from previous loop)
#                               last_node_of_sub_list = current (the origin start of current sublist, which will be the new end, comes from previous loop after reverse)
# Hence, end of each process need to make sure previous = last_node_of_sub_list (new end of current sublist after reverse, i.e. which "current" points to in the beginning)


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


def reverse_every_k_elements(head, k):
    if k <= 1 or head is None:
        return head

    current, previous = head, None

    while True:
        # initialize value or lnpp = last node of reversed sublist (lnsl) from previous loop
        last_node_of_previous_part = previous

        # initialize value or
        # after reversing later,
        # the LinkedList 'current' will become the last node of the sub-list
        # i.e. first node of original sublist..
        last_node_of_sub_list = current

        # temp = None  # will be used to temporarily store the next node
        i = 0

        # after this loop,
        # previous will point to the last node of k elements.. which is new start of sublist
        # current will point to the next of last node.. which is the start of rest list..
        while current is not None and i < k:  # reverse 'k' nodes
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            i += 1


        # connect with the previous part
        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous
        else:
            head = previous

        # connect with the next part
        last_node_of_sub_list.next = current
        last_node_of_sub_list.print_list()
        if current is None:
            break
        # make sure previous points to lnsl in this loop
        previous = last_node_of_sub_list
    return head

def reverse(start):
    new_start = None
    new_end = start
    while start is not None:
        temp = start.next
        start.next = new_start
        new_start = start
        start = temp
    return new_start, new_end

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()

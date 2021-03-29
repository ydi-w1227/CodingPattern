# Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.
#
# Your algorithm should not use any extra space and the input LinkedList should be modified in-place.
#
# Example 1:
#
# Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
# Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null
# Example 2:
#
# Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
# Output: 2 -> 10 -> 4 -> 8 -> 6 -> null


from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
          print(str(temp.value) + " ", end='')
          temp = temp.next
        print()


def reorder(head):
    # edge case
    if head is None or head.next is None:
        return head

    # get middle of linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    first_head = head
    # now slow points to middle of the linked list
    # reverse second half for further insertion
    second_head = reverse(slow)

    first_head.print_list()
    second_head.print_list()

    # traverse first half and second half
    head = reArrange(first_head, second_head)

    return head

def reverse(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev

def reArrange(first_head, second_head):
    # save start node
    head = first_head
    # odd number of nodes.. point to the same last node
    # even number of nodes.. second_head will point to node which is from first_head in the end
    #                           i.e. there is one node less from second_head
    while first_head != second_head and second_head.next is not None:
        # save both next value, because .next will break later
        temp_f = first_head.next
        temp_s = second_head.next
        # break origin link and create new link
        first_head.next = second_head
        second_head.next = temp_f
        # two heads point to next node
        first_head = temp_f
        second_head = temp_s
    return head

def reorder_official(head):
  if head is None or head.next is None:
    return

  # find middle of the LinkedList
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

  # slow is now pointing to the middle node
  head_second_half = reverse(slow)  # reverse the second half
  head_first_half = head

  # rearrange to produce the LinkedList in the required order
  while head_first_half is not None and head_second_half is not None:
    temp = head_first_half.next
    head_first_half.next = head_second_half
    head_first_half = temp

    temp = head_second_half.next
    head_second_half.next = head_first_half
    head_second_half = temp

  # set the next of the last node to 'None'
  if head_first_half is not None:
    head_first_half.next = None


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()

    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    reorder(head)
    head.print_list()


main()

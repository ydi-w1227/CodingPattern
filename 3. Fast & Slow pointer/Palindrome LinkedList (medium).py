# Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
#
# Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.
#
# Example 1:
#
# Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
# Output: true
# Example 2:
#
# Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
# Output: false

# https://medium.com/dev-genius/linked-list-algorithm-is-it-a-palindrome-for-singly-linked-list-3137291f76c9
# find second half of linked list
# reverse the second half
# compare
# reverse the second half back

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        string = ''
        while self is not None:
            string += str(self.value) + '-->'
            self=self.next
        string += 'null'
        return string

def is_palindromic_linked_list(head):
    # edge case
    if head is None or head.next is None:
        return True

    slow, fast = head, head
    if slow.next is None:
        return False

    # odd list fast will point to last number
    # even list fast will point to null
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next


    # now slow points to the middle node of linked list if it is odd
    # or second middle node if it is even
    first_half_head = head
    second_half_head = reverse(slow)
    copy_second_half_head = second_half_head
    print(first_half_head.print_list())

    while first_half_head and second_half_head:
        # not palindrome
        if first_half_head.value != second_half_head.value:
            break
        first_half_head = first_half_head.next
        second_half_head = second_half_head.next

    reverse(copy_second_half_head)

    # if both reach to the last node
    # i.e. .next = none so jump out from while loop
    # use or because if linked list is even then first half will have one more element
    if first_half_head is None or second_half_head is None:
        return True
    return False

# 2->4->6->4->2->null
# become 2->4->6->null
#             /
#         2->4
def reverse(head):
    # reverse the linked list
    prev = None
    while head:
        # save the next node of current node
        temp = head.next
        # current node will point to previous_node in linked list
        head.next = prev
        # current node become previous_node for next loop
        prev = head
        # temp(next node of current node) become head in next loop
        head = temp
    print(prev.print_list())
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    print(head.print_list())
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print(head.print_list())
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()

# Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
# Given the head of a LinkedList with a cycle, find the length of the cycle.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    slow, fast = head, head
    while slow is not None and fast is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            size = find_cycle_length(slow)
            return (True, size)
    return (False, 0)

def find_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))



main()

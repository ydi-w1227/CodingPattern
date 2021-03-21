# Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.


from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def find_cycle_start(head):
  slow, fast = head, head
  while slow is not None and fast is not None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      # meetingPoint = find_start_point(head, fast)
      # return meetingPoint
      cycle_length = calculate_cycle_length(slow)
      print(cycle_length)
      return find_start(cycle_length, head)
  return None

# Method 1
# After finding the meeting point,
# if faster point starts from meeting point and slow starts from start(where head points to)
# they will meet at start point
# (proof is z = x mod(y+z), i.e. x has relations with multiple times(can be 0, 1 ,...) of y+z and one times z which reach start point)
def find_start_point(head, fast):
  slow = head
  fast = fast
  print(slow.value)
  print(fast.value)
  while slow is not None and fast is not None:
    if slow != fast:
      slow = slow.next
      fast = fast.next
    else:
      break
  return slow


# Method 2
# After finding meeting point, try to start slow and fast again from head
# move fast loop length ahead, and then increase slow and fast 1 step each time..
# until they meet
# This is because fast is only one loop length ahead slow (not necessary reach meeting point)
# once slow reach start point of loop, fast is loop length ahead which is exactly same point..
def calculate_cycle_length(slow):
  current = slow
  cycle_length = 0
  while True:
    current = current.next
    cycle_length += 1
    if current == slow:
      break
  return cycle_length

def find_start(cycle_length, head):
  slow, fast = head, head
  print(slow.value)
  while cycle_length != 0:
    fast = fast.next
    cycle_length -= 1
  while slow != fast:
    slow = slow.next
    fast = fast.next
    if slow == fast:
      break
  return slow


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()

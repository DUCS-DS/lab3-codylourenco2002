from llist import *

def llprint(lst, num):
    """print the first num terms of linked list lst"""
    current = lst.head
    for _ in range(num):
        if current:
            print(current.val, end=" ")
            current = current.next
        else:
            break
    print()

def find_cycle(lst):
    """return the start index and length of the cycle"""
    slow = fast = lst.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle

    # Find the start of the cycle
    slow = lst.head
    start_index = 0
    while slow != fast:
        slow = slow.next
        fast = fast.next
        start_index += 1

    # Find the length of the cycle
    cycle_length = 1
    fast = fast.next
    while slow != fast:
        fast = fast.next
        cycle_length += 1

    return start_index, cycle_length

if __name__ == "__main__":
    values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    linked_list = LList()
    for value in values:
        append(linked_list, Node(value))

    # Create a cycle of length 5 that starts at position 10
    node = linked_list.head
    for _ in range(10):
        node = node.next
    cycle_start = node

    node = linked_list.head
    while node.next:
        node = node.next
    node.next = cycle_start

    # Print the first 30 terms of the linked list
    llprint(linked_list, 30)
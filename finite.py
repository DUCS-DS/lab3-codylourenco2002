#Cody Lourenco
from llist import LList, Node, append

def length(lst):
    """return the length of a finite linked list"""
    current = lst.head
    count = 0
    while current:
        count += 1
        current = current.next
    return count

def llprint(lst):
    """print a finite linked list"""
    current = lst.head
    while current:
        print(current.val, end=" ")  # Note: changed from current.data to current.val
        current = current.next
    print()

if __name__ == "__main__":
    values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    linked_list = LList()
    for value in values:
        append(linked_list, Node(value))

    print("Length of linked list:", length(linked_list))
    print("Linked list:")
    llprint(linked_list)

    # Exercise 5
    from genfinite import lst
    print(length(lst))
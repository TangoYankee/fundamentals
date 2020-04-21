class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def unshift(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node


def create_linked_list():
    llist = LinkedList()
    for i in range(0, 17, 4):
        llist.unshift(i)
    return llist


def display(head):
    print("begin")
    while(head):
        print(head.value)
        head = head.next
    print("end")


def reverse_linked_list(head):
    current = head
    prev = None
    while(current):
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev


llist = create_linked_list()
display(llist.head)
reversed_head = reverse_linked_list(llist.head)
display(reversed_head)

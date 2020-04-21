[Home](/fundamentals/)

# Linked Lists

## Structure
```
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

```

## Reverse
```
def create_linked_list():
  llist = LinkedList()
  for i in range(0,17,4):
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
  prev = None # Eventually end with Null
  while(current):
    temp = current.next # Temporary node to prevent next node getting lost
    current.next = prev # Reverse pointer for current node
    prev = current # Current node falls one position
    current = temp # Find the temporary node
  return prev # Holds the last valid reference to a node. Current is now null

llist = create_linked_list()
display(llist.head)
reversed_head = reverse_linked_list(llist.head)
display(reversed_head)
```

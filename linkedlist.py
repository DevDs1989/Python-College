class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def traverse(self):
    current = self.head
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")

  def delete(self):
    current = self.head
    self.head = current.next
    current = None
    return
  def search(self, data):
    current = self.head
    count = 0
    while current:
      count += 1
      if current.data == data:
        print("Found at position: ", count)
        return True
      current = current.next
    print("Not found")
    return False
    
    

linked_list = LinkedList()
linked_list.insert(22)
linked_list.insert(21)
linked_list.insert(20)

linked_list.traverse()
linked_list.search(20)

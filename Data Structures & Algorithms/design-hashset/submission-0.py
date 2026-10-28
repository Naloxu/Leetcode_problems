class Node:
  def __init__(self, key:int) -> None:
    self.key = key
    self.next = None

class MyHashSet:

  def __init__(self):
    self.nodes = [Node(-1) for _ in range(10**4)]
    self.head = Node(-1)

  def add(self, key: int) -> None:
    current_node = self.head
    while current_node.next:
      if current_node.next.key == key:
        return
      current_node = current_node.next
    current_node.next = Node(key)
    return
    

  def remove(self, key: int) -> None:
    current_node = self.head
    while current_node.next:
      if current_node.next.key == key:
        current_node.next = current_node.next.next
        return
      current_node = current_node.next

  def contains(self, key: int) -> bool:
    current_node = self.head
    while current_node.next:
      if current_node.next.key == key:
        return True
      current_node = current_node.next
    return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
class Node:
  def __init__(self, value, children=[None]):
    self.value = value
    self.children = children

  def value(self):
    return self.value

  def traverse(self, value):
    for i in range(len(self.children)):
      if i is value:
        return self.children[i]

  def add_child(self, next_node):
    self.children.append(next_node)


class NodeTree:
  def __init__(self, value=None):
    self.head_node = Node(value)

  def get_head_node(self):
    return self.head_node

  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.add_child(self.head_node)
    self.head_node = new_node

  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.value() != None:
        string_list += str(current_node.value()) + "\n"
        current_node = current_node.traverse()
        return string_list

  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.value() == value_to_remove:
      self.head_node = current_node.traverse()
    else:
    while current_node:
      next_node = current_node.traverse()
    if next_node.value() == value_to_remove:
      current_node.add_child(next_node.traverse())
      current_node = None
    else:
      current_node = next_node


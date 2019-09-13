class Node:
	def __init__(self, value, next_node=None):
		self.value = value
		self.next_node = next_node
		
	def get_value(self):
		return self.value

	def get_next_node(self):
		return self.next_node

	def set_next_node(self, next_node):
		self.next_node = next_node

class LinkedList:
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

class TreeNode:
	def __init__(self, value):
		self.value = value 
		self.children = [] 

	def add_child(self, child_node):
		self.children.append(child_node) 
		
	def remove_child(self, child_node):

		self.children = [child for child in self.children if child is not child_node]

	def traverse(self):
		nodes_to_visit = [self]
		while len(nodes_to_visit) > 0:
			current_node = nodes_to_visit.pop()
			print(current_node.value)
			nodes_to_visit += current_node.children

class Vertex:
	def __init__(self, value):
		self.value = value
		self.edges = {}

	def add_edge(self, vertex, weight=0):
		self.edges[vertex.value] = weight

	def get_edges(self):
		return list(self.edges.keys())
	
	def remove_edge(self, edge):
		self.edges.pop(edge, None) 

class Graph:
	def __init__(self, directed = False):
		self.graph_dict = {}
		self.directed = directed

	def add_vertex(self, vertex):
		self.graph_dict[vertex.value] = vertex

	def add_edge(self, from_vertex, to_vertex, weight = 0):
		self.graph_dict[from_vertex.value].add_edge(to_vertex, weight)
		if not self.directed:
			self.graph_dict[to_vertex.value].add_edge(from_vertex, weight)

	def find_path(self, start_vertex, end_vertex):
		start = [start_vertex]
		seen = {}
		while len(start) > 0:
			current_vertex = start.pop(0)
			seen[current_vertex] = True
			if current_vertex == end_vertex:
				return True
			else:
				vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
				start += [vertex for vertex in vertices_to_visit if vertex not in seen]
		return False
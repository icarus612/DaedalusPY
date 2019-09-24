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
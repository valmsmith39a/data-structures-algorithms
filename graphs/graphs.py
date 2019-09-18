 g = { "a" : ["d"],
       "b" : ["c"],
       "c" : ["b", "c", "d", "e"],
       "d" : ["a", "c"],
       "e" : ["c"],
       "f" : []
     } 
class Graph(object):
	def __init__(self, graph_dict=None):
		if graph_dict==None:
			graph_dict = {}
		self.__graph_dict = graph_dict

	def generate_edges(self):
		edges = []
		for vertex in self.__graph_dict:
			for neighbor in self.__graph_dict[vertex]:
				if {neighbor, vertex} not in edges:
					edges.append({vertex, neighbor})
		return edges
	
	

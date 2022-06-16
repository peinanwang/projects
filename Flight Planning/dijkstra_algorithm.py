'''
dijkstra_algorithm.py
This file defines a weighted graph as the Graph class, which has dijkstra() 
method that uses Dijkstra's algorithm to find the shortest path. 
'''

class Graph:

	def __init__(self, graph_matrix):
		'''
		To construct a graph representing the passed-in matrix
		'''
		self.matrix = graph_matrix


	def find_min_distance(self, distance_lst, to_visit):
		'''
		To find the unvisted vertex with the lowest weight
		'''
		minimum = float("inf")
		min_index = -1
		
		for i in range(len(distance_lst)):
			if distance_lst[i] < minimum and i in to_visit:
				minimum = distance_lst[i]
				min_index = i
		return min_index


	def print_path(self, visited_vertices, j):
		'''
		print the path to get to vertex j
		'''
		#Base Case : if j is source
		if visited_vertices[j] == -1:
			print(j, end=" ")
			return
		self.print_path(visited_vertices , visited_vertices[j])
		print (j, end=" ")


	def display_result(self, src, distance_lst, visited_vertices):
		'''
		print the result to show the shortest path from the source vertex 
		to every other vertices
		'''
		print("Vertex\t\tTotal Weight of the Path\tPath")
		for i in range(0, len(distance_lst)):
			print(f"\n{src} --> {i} \t\t{distance_lst[i]}\t\t\t", end=" ")
			self.print_path(visited_vertices, i)
		print()
	

	def dijkstra(self, src):
		'''
		Use Dijkstra's algorithm to find the shortest path from a source vertex
		to every other vertex
		src: an integer, the source vertex 
		'''
		row = len(self.matrix)
		col = len(self.matrix[0])

        # initialize a list of distances from the source vertex
		# the distance from the source vertex to itself is set to 0
		distance_lst = [float("inf")] * row
		distance_lst[src] = 0  

		# initialize a list of visited vertices
		visited_vertices = [-1] * row

		# create a list of unvisted vertices
		to_visit = []
		for i in range(row):
			to_visit.append(i)

		while len(to_visit) != 0:
            
			# find an unvisited vertex that has the shortest distance
			# from the source vertex
			u = self.find_min_distance(distance_lst, to_visit)
            
			to_visit.remove(u)
            
			# if we can find a shorter path to an vertex by visiting vertex u 
			# from the source vertex. Update the distance in the distance list
			for i in range(col):
				if self.matrix[u][i] and i in to_visit:
					if distance_lst[u] + self.matrix[u][i] < distance_lst[i]:
						distance_lst[i] = distance_lst[u] + self.matrix[u][i]
						visited_vertices[i] = u
        
		# print the result to the terminal
		self.display_result(src, distance_lst, visited_vertices)

def main():
    # this main() is to test the dijkstra() method of the Graph class
	graph_matrix = [[0, 6, 2, float("inf")],
	                [6, 0, 3, 1],
		            [2, 3, 0, 5],
		            [float("inf"), 1, 5, 0]]
	
	g = Graph(graph_matrix)

	g.dijkstra(3)

if __name__ == "__main__":
	main()

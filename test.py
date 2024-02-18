adjacency_table = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['D', 'F'],
    'F': ['D', 'E']
}

def find_neighbors(vertex, adjacency_table):
    return adjacency_table[vertex]

def is_neighbor(vertex1, vertex2, adjacency_table):
    return vertex2 in adjacency_table[vertex1]

print(find_neighbors('A', adjacency_table)) # should print ['B', 'C']
print(find_neighbors('D', adjacency_table)) # should print ['C', 'E', 'F']

print(is_neighbor('A','B',adjacency_table)) # True
print(is_neighbor('D','F',adjacency_table)) # True
print(is_neighbor('C','F',adjacency_table)) # False
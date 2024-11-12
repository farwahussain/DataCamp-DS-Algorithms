import queue

graph = {
  '4' : ['6','7'],
  '6' : ['4', '7', '8'],
  '7' : ['4', '6', '9'],
  '8' : ['6', '9'],
  '9' : ['7', '8']
}

def BFS(graph, initial_vertex, search_value):
    visited_vertices = []
    bfs_queue = queue.SimpleQueue()
    visited_vertices.append(initial_vertex)
    bfs_queue.put(initial_vertex)
    
    while not bfs_queue.empty():
        current_vertex = bfs_queue.get()
        # Check if you found the search value
        if current_vertex == search_value:
            return True
        for adjucent_vertex in graph[current_vertex]:
             if adjucent_vertex not in visited_vertices:
                 visited_vertices.append(adjucent_vertex)
                 bfs_queue.put(adjucent_vertex)
                 
    return False

print(BFS(graph, '4', '8'))
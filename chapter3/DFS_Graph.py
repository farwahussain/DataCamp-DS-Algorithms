#implement a depth first search algorithm to traverse a graph.

graph = {
  '0' : ['1','2'],
  '1' : ['0', '2', '3'],
  '2' : ['0', '1', '4'],
  '3' : ['1', '4'],
  '4' : ['2', '3']
}

def DFS(visited_vertices, graph, current_vertex):
    #check if current not is not visited
    if current_vertex not in visited_vertices:
        #if true then print current node
        print(current_vertex)
        #add current node to visited list
        visited_vertices.add(current_vertex)
        #iterate over the graph 
        for adjacent_vertex in graph[current_vertex]:
            #recursively call DFS on adjacent vertex
            DFS(visited_vertices, graph, adjacent_vertex)

DFS(set(), graph, '0')
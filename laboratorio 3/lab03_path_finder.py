def find_path(graph, start, end, path):
     
    # Apuntamos que hemos llegado al nodo start.
    path.append(start)
    
    # Este es el caso trivial de la recursion. Hemos llegado al nodo end.
    if start == end:
        return path
    else:
    # TODO
    # Terminar de implementar esta funcion sin modificar lo anterior
        camino = []
        for i in range(len(graph[0])):
            if path.count(i)==0 and graph[start][i]==1:
                camino = find_path(graph,i,end,path)
                if camino and camino[len(camino)-1]==end:
                    break
        if not camino and path[len(path)-1]==start:
            path.pop()
        return camino
    
    
def test():
    g1 = [[0, 1, 1, 0, 0],
          [1, 0, 1, 1, 0],
          [1, 1, 0, 0, 1],
          [0, 1, 0, 0, 1],
          [0, 0, 1, 1, 0]]
    
    assert find_path(g1, 0, 4, []) in [[0, 2, 4], [0, 2, 1, 3, 4], [0, 1, 2, 4], [0, 1, 3, 4]]
    
    g2 = [[0, 1, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 1],
          [0, 0, 1, 0]]
    
    assert find_path(g2, 0, 1, []) in [[0,1]]    
    assert find_path(g2, 0, 2, []) == []
    
    g3 = [[0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0],
          [1, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 1],
          [0, 0, 1, 0, 0, 1],
          [0, 0, 0, 1, 1, 0]]
    
    assert find_path(g3, 1, 0, []) in [[1, 3, 2, 0], [1, 3, 5, 4, 2, 0]]
    
    g4 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 0, 1, 1, 0],
          [1, 0, 0, 0, 0, 1],
          [0, 1, 0, 0, 1, 0],
          [0, 1, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0]]
    
    assert find_path(g4, 0, 5, []) in [[0, 2, 5]]
         
test()

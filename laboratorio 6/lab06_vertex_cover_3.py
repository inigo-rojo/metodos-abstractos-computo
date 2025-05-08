from time import time

## vertex_cover_tree inicializa y llama al arbol de busqueda
def vertex_cover_tree(graph):
    n = len(graph)
    cover = [None]*n
    return recursive_vertex_cover(graph, cover)

def partial_validity_check(cover, graph):
    # TODO: Programa el codigo de la funcion
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j]==1 and (cover[j]==0 and cover[i]==0):
                return False
    return True

def next_none(cover,empezar):
    for i in range(len(cover)-empezar):
        if cover[i+empezar]==None:
            return i+empezar
    return -1

def completar(cover):
    combinacion1=[]
    combinacion2=[]
    for i in range(len(cover)):
        if cover[i]==None:
            combinacion1.append(0)
            combinacion2.append(1)  
        else:
            combinacion1.append(cover[i])
            combinacion2.append(cover[i])
    return combinacion1,combinacion2

def recursive_vertex_cover(graph, cover):
    ############
    # TODO: Programa esta parte de la funcion
    #
    # Comprueba es posible construir un cover valido.
    # Si no es posible, devuelve [1]*len(cover).
    # En otro caso, encuentra dos nodos u y v conectados y que no estan en el cover.
    # Si no los hay, completa el cover decidiendo si los que faltan deben formar parte 
    # del cover o no y una vez hecho esto, devuelve el cover completo.
    # En otro caso continua con u y v
    u= next_none(cover,0)
    v= next_none(cover,u+1)
    if u==-1 and v==-1:
        if partial_validity_check(cover,graph)==True:
            return cover
        else:
            return [1]*len(graph)
    elif u!=-1 and v==-1:
        combinacion1,combinacion2=completar(cover)
        if partial_validity_check(combinacion1,graph)==True and partial_validity_check(combinacion2,graph)==False:
            return combinacion1
        elif partial_validity_check(combinacion1,graph)==False and partial_validity_check(combinacion2,graph)==True:
            return combinacion2
        elif partial_validity_check(combinacion1,graph)==True and partial_validity_check(combinacion2,graph)==True:
            return combinacion1
        else:
            return [1]*len(graph)
    else:
    
    # Final de tu codigo
    # Lo siguiente abre las tres ramas del arbol de busqueda.
    # No modificar nada.
    ##############
        copy_cover = list(cover)
        cover[u] = 1
        cover[v] = 0
        c10 = recursive_vertex_cover(graph, cover)
        cover = list(copy_cover)
        cover[u] = 0
        cover[v] = 1
        c01 = recursive_vertex_cover(graph, cover)
        cover = list(copy_cover)
        cover[u] = 1
        cover[v] = 1
        c11 = recursive_vertex_cover(graph, cover)
        if c10.count(1) <= min(c01.count(1), c11.count(1)):
            return c10
        elif c01.count(1) <= c11.count(1):
            return c01
        else:
            return c11
    
def test():
    
    g1 =  [[0, 1],
           [1, 0]]
       
    g2 = [[0, 1, 1],
          [1, 0, 0],
          [1, 0, 0]]
        
    
    g3 = [[0, 1, 1, 1, 1],
          [1, 0, 0, 0, 1],
          [1, 0, 0, 1, 1],
          [1, 0, 1, 0, 1],
          [1, 1, 1, 1, 0]]
    
        
    g4 = [[0, 1, 1, 1],
          [1, 0, 1, 0],
          [1, 1, 0, 1],
          [1, 0, 1, 0]]
    
       
    g5 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 0, 1, 1, 0],
          [1, 0, 0, 1, 1, 1],
          [0, 1, 1, 0, 0, 1],
          [0, 1, 1, 0, 0, 0],
          [0, 0, 1, 1, 0, 0]]
    
    g6 = [[0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
          [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
          [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
          [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
          [1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
          [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
          [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
          [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
          [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0]]

    
   

 
#    Descomentar para probar la funcion recursive_vertex_cover
    assert vertex_cover_tree(g1) in [[1,0],[0,1]]
    assert vertex_cover_tree(g2)  == [1,0,0]
    assert vertex_cover_tree(g3) in [[1, 0, 1, 0, 1], 
                                    [1, 0, 0, 1, 1]]
    assert vertex_cover_tree(g4)  == [1, 0, 1, 0]
    assert vertex_cover_tree(g5)  in  [[0, 1, 1, 1, 0, 0], 
                                       [0, 1, 1, 0, 0, 1]]
#    
#    
    assert vertex_cover_tree(g6) in [[1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
                                     [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
                                     [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                                     [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                                     [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
                                     [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
                                     [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                                     [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                                     [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                                     [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
                                     [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                                     [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
                                     [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
                                     [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                                     [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
                                     [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                                     [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                                     [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                                     [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
                                     [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
                                     [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                                     [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
                                     [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                                     [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
                                     [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                                     [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
                                     [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0],
                                     [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
                                     [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
                                     [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1],
                                     [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1]]
    
start_time = time()
test()
elapsed_time = time() - start_time   
print("Elapsed time: %0.10f seconds." % elapsed_time) 
print '0.0820000172 segundos en el ordenador de sobremesa'     
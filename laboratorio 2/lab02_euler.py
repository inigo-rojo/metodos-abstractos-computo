def graph_has_Eulerian_circuit(g):
    #acepta una matriz y devuelve si tiene circuito euleriano o no
    # TODO: 
    # Programar el codigo esta funcion
    # Puedes definir funciones auxiliares si lo estimas oportuno
    #este for rota por cada fila de la matriz que examinamos para saber si tiene circuito euleriano
    for i in range(len(g)):
        contador = 0
        #este for rota por cada columna de la matriz, si tiene conexion a otro nodo aumenta el contador
        #si el contador es par significa que habra circuito euleriano y pasa a la siguiente fila
        #si una fila tiene grado impar para porque ya sabe que no hay circuito euleriano
        for j in range(len(g[i])):
            if(g[i][j]==1):
                contador= contador +1
        if contador%2!=0:
            return False
    return True

def test():
    g1 = [[0, 1, 1, 0, 0],
          [1, 0, 1, 1, 1],
          [1, 1, 0, 1, 1],
          [0, 1, 1, 0, 1],
          [0, 1, 1, 1, 0]]
    assert not graph_has_Eulerian_circuit(g1)


    g2 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 1, 1, 1, 0],
          [1, 1, 0, 1, 1, 0],
          [0, 1, 1, 0, 1, 1],
          [0, 1, 1, 1, 0, 1],
          [0, 0, 0, 1, 1, 0]]
    
    assert graph_has_Eulerian_circuit(g2)

    g3 = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 0, 1, 1, 1],
          [1, 1, 0, 0, 1, 1, 1, 1],
          [0, 1, 0, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 0],
          [0, 1, 1, 1, 0, 0, 1, 1],
          [0, 1, 1, 0, 1, 1, 0, 1],
          [0, 1, 1, 0, 0, 1, 1, 0]]
    
    assert not graph_has_Eulerian_circuit(g3)
    
    g4 = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
          [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
          [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 1, 1, 0, 1, 1, 0, 0],
          [0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]
    
    assert graph_has_Eulerian_circuit(g4)
    

test()


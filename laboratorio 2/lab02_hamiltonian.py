from itertools import permutations
def graph_has_Hamiltonian_circuit(g):
    # TODO: 
    # Programar el codigo esta funcion
    # Puedes definir funciones auxiliares si lo estimas oportuno
    #acepta una matriz como entrada y devuelve si tiene circuito hamiltoniano
    li= range(len(g))
    li.remove(0)
    lista = list(permutations(li))
    #despues de crear la lista de permutaciones(suponiendo que partimos/terminamos en el nodo 0)
    #el for rota por cada permutacion de nodos
    for i in range(len(lista)):
        caminoPosible = lista[i]
        empezar = True
        #se asigna el camino posible y se rota por cada elemento de la lista haber si es atravesable
        for j in range(len(caminoPosible)):
            #comprueba que desde el nodo 0 se pueda llegar hasta aqui
            if empezar==True:
                if g[0][caminoPosible[j]]==0:
                    #no tiene camino desde el nodo 0, pasamos a la siguiente permutacion
                    break
                else:
                    empezar=False
                    #tiene camino desde el nodo 0
            if j == len(caminoPosible)-1:
                if g[caminoPosible[j]][0]==1:
                    #puede volver al nodo inicial 0, hay camino hamiltoniano
                    return True
            else:
                if g[caminoPosible[j]][caminoPosible[j+1]]==0:
                    #no tiene conexion al siguiente nodo, pasamos a la siguiente permutacion
                    break
    return False

def test():
    g1 = [[0, 1, 1, 0, 0],
          [1, 0, 1, 1, 1],
          [1, 1, 0, 1, 1],
          [0, 1, 1, 0, 1],
          [0, 1, 1, 1, 0]]
    assert graph_has_Hamiltonian_circuit(g1)


    g2 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 1, 1, 1, 0],
          [1, 1, 0, 1, 1, 0],
          [0, 1, 1, 0, 1, 1],
          [0, 1, 1, 1, 0, 1],
          [0, 0, 0, 1, 1, 0]]
    
    assert graph_has_Hamiltonian_circuit(g2)


    g3 = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 0, 1, 1, 1],
          [1, 1, 0, 0, 1, 1, 1, 1],
          [0, 1, 0, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 0],
          [0, 1, 1, 1, 0, 0, 1, 1],
          [0, 1, 1, 0, 1, 1, 0, 1],
          [0, 1, 1, 0, 0, 1, 1, 0]]
    
    assert graph_has_Hamiltonian_circuit(g3)
   
   
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
    
    assert not graph_has_Hamiltonian_circuit(g4)
    
    
test()

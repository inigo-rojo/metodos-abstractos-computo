
def is_satisfied(num_variables, clauses, assignment):
     # Prendicion: num_variables + 1 = len(assignment)

     # TODO: 
     # - Programar el codigo esta funcion
     # - Puedes definir funciones auxiliares si lo estimas oportuno
     #este for rota por todas la clausulas para ver si todas son correctas
     for i in range(len(clauses)):
         clausulaCorrecta=False
         #este for evalua cada variable de la clausula actual buscando una que sea correcta
         for j in range(len(clauses[i])):
             if clauses[i][j] > 0 and assignment[clauses[i][j]]==1:
                 clausulaCorrecta=True
                 break
             if clauses[i][j] < 0 and assignment[clauses[i][j]*(-1)]==0:
                 clausulaCorrecta=True
                 break
         #si ninguna variable de la clausula es correcta, la clausula es incorrecta y no satisface la formula
         if clausulaCorrecta == False:
            return False
     return True
            
                 
   

def test():
    num_variables = 4
    clauses = [[1,2,-3],[2,-4],[-1,3,4]]
    assignment = [0,1,1,1,1]
    assert is_satisfied(num_variables, clauses, assignment)
    assignment = [0,1,0,1,1]
    assert not is_satisfied(num_variables, clauses, assignment)
    clauses = [[-3, -1], [2, -3, -4, -1], [-1, -4], [-3], [-1, -2], [-3, 4, -2], [-1, -4, 2]]
    assignment = [0,0,0,1,0]
    assert not is_satisfied(num_variables, clauses, assignment)
    
test()    
#el tiempo de ejecucion de de O(n*n) en el peor de los casos(cada clausula tiene todas las variables)

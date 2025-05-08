from tools import list_minisat2list_our_sat 

def sat_preprocessing(num_variables, clauses):
    # TODO: 
    # Programar el codigo esta funcion
    # Puedes definir funciones auxiliares si lo estimas oportuno
    finalizar=False
    finalizar1=False
    finalizar2=False
    literales = [None]*(num_variables+1)
    while finalizar != True:
        finalizar1=pasoA(num_variables, clauses,literales)
        finalizar2=pasoB(num_variables, clauses,literales)
        if finalizar1 and finalizar2:
            finalizar=True
        else:
            pasoC(num_variables, clauses,literales)
            pasoD(num_variables, clauses,literales)
        print 'atascado en bucle'
    print 'termina una comprobacion'
    if len(clauses)==1 and len(clauses[0])==0:
        return [[1],[-1]]
    else:
        return clauses
    
def pasoA(num_variables,clauses,literales):
    for i in range(len(clauses)):
        if len(clauses[i])==1:
            if clauses[i][0]>0:
                literales[clauses[i][0]]==1
            else:
                literales[clauses[i][0]]==0
            return False
    return True
def pasoB(num_variables,clauses,literales):
    conteoclausulas=[[0,1]]*(num_variables+1)
    for i in range(len(clauses)):
        for j in range(len(clauses[i])):
            if clauses[i][j]>0:
                conteoclausulas[clauses[i][j]][0]=conteoclausulas[clauses[i][j]][0]+1
                conteoclausulas[clauses[i][j]][1]=1
            else:
                conteoclausulas[(-1)*clauses[i][j]][0]=conteoclausulas[(-1)*clauses[i][j]][0]+1
                conteoclausulas[(-1)*clauses[i][j]][1]=-1
    for i in range (len(conteoclausulas)):
        if conteoclausulas[i][0]==1:
            if conteoclausulas[i][1]==1:
                literales[i]=1
            else:
                literales[i]=-1
            return False
    return True
        
            
def pasoC(num_variables,clauses,literales):
    clausulaseliminar=[]
    for i in range(len(clauses)):
        eliminar=False
        for j in range(len(clauses[i])):
            if clauses[i][j]>0:
                if literales[clauses[i][j]]!=None:
                    if literales[clauses[i][j]]==1:
                       eliminar=True
                       break
                    else:
                       clauses[i][j]=0
            else:
                if literales[(-1)*clauses[i][j]]!=None:
                    if literales[(-1)*clauses[i][j]]==-1:
                       eliminar=True
                       break
                    else:
                       clauses[i][j]=0
        if eliminar==True:
            clausulaseliminar.append(i)
        else:
            while clauses[i].count(0) > 0:
                clauses[i].remove(0)
    borrados=0
    for i in range(len(clausulaseliminar)):
        clauses.remove(clausulaseliminar[i]-borrados)
        borrados+=1
        
        
def pasoD(num_variables,clauses,literales):
    for i in range(len(clauses)):
        for j in range(len(clauses[i])):
            literaleseliminar=[]
            if clauses[i][j]>0:
                if literales[clauses[i][j]]!=None:
                    if literales[clauses[i][j]]==0:
                        literaleseliminar.append(clauses[i][j])
            else:
                if literales[(-1)*clauses[i][j]]!=None:
                    if literales[(-1)*clauses[i][j]]==1:
                        literaleseliminar.append((-1)*clauses[i][j])
        borrados=0
        for j in range(len(literaleseliminar)):
            clauses[i].remove(literaleseliminar[j]-borrados)
            borrados+=1
                    
def test():
    
    assert [] == sat_preprocessing(1, [[1]])
    assert [[1],[-1]] == sat_preprocessing(1, [[1], [-1]])
    assert [] == sat_preprocessing(4, [[4], [-3, -1], [3, -4, 2, 1], [1, -3, 4],
                                         [-1, -3, -4, 2], [4, 3, 1, 2], [4, 3],
                                         [1, 3, -4], [3, -4, 1], [-1]])
    assert [[1],[-1]] == sat_preprocessing(5, [[4, -2], [-1, -2], [1], [-4],
                                         [5, 1, 4, -2, 3], [-1, 2, 3, 5],
                                         [-3, -1], [-4], [4, -1, 2]])
    
    ans = [[5, 6, 2, 4], [3, 5, 2, 4], [-5, 2, 3], [-3, 2, -5, 6, -4]]
    assert ans == sat_preprocessing(6, [[-5, 3, 2, 6, 1], [5, 6, 2, 4],
                                        [3, 5, 2, -1, 4], [1], [2, 1, 4, 3, 6],
                                        [-1, -5, 2, 3], [-3, 2, -5, 6, -4]])
    # Nuevo assert
    assert [] == sat_preprocessing(7, [[-5, 3, 2, 6, 1], [5, 6, 2, 4],
                                        [3, 5, 2, -1, 4], [1], [2, 1, 4, 3, 6],
                                        [-1, -5, 2, 3], [-3, 2, -5, 6, -4, 7]])
    print 'acaba'
         

test()

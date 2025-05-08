from vertex_cover import solve_vc


def multisolve(graph, problem):    
    if problem ==   "VERTEX COVER":
        #devolvemos la respuesta de manera directa ya que no hay que aplicar equivalencias
        return solve_vc(graph)
    else:
        if problem == "INDEPENDENT SET":
            #obtenemos la solucion vertex cover
            grafo = solve_vc(graph)
            #modificamos la respuesta en funcion de la equivalencia entre vertex cover y independent set
            for i in range(len(grafo)):
                if grafo[i]==0:
                    grafo[i]=1
                else:
                    grafo[i]=0
                    #devolvemos la respuesta
            return grafo
        if problem == "CLIQUE":
            #ya que la variable del grafo se modifica en memoria, para no afectar a la ejecucion debemos copiarla
            #al ser python 2.7 no podemos usar deepcopy()
            graphmod = []
            for i in range(len(graph)):
                seccion=[]
                for j in range(len(graph[i])):
                    seccion.append(graph[i][j])
                graphmod.append(seccion)
            #una vez tenemos nuestra copia del grafo la modificamos para que responda a la equivalencia de I.S
            for i in range(len(graphmod)):
                for j in range(len(graphmod[i])):
                    if graphmod[i][j]==1:
                        graphmod[i][j]=0
                    else:
                        graphmod[i][j]=1
                graphmod[i][i]=0
            #convertido a IS, ahora invocamos la solucion del vertex cover
            grafo = solve_vc(graphmod)
            #modificamos la respuesta en funcion de la equivalencia entre vertex cover y independent set
            for i in range(len(grafo)):
                if grafo[i]==0:
                    grafo[i]=1
                else:
                    grafo[i]=0
            #devolvemos la solucion
            return grafo


def test():
   graph = [[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
   
   sol_vertex = multisolve(graph, "VERTEX COVER")
   sol_clique = multisolve(graph, "CLIQUE")
   sol_independent_set =  multisolve(graph, "INDEPENDENT SET")
   
   assert sol_vertex in [[0,0,1,1], [1,0,0,1], [0,1,1,0]]
   assert sol_independent_set in [[1,0,0,1],[1,1,0,0],[0,1,1,0]]
   assert sol_clique in [[1,0,1,0],[0,0,1,1],[0,1,0,1]]
   
   graph = [[0,1,1],[1,0,1],[1,1,0]]
   
   sol_vertex = multisolve(graph, "VERTEX COVER")
   sol_clique = multisolve(graph, "CLIQUE")
   sol_independent_set =  multisolve(graph, "INDEPENDENT SET")    
   
   assert sol_vertex in [[0,1,1], [1,0,1], [1,1,0]]
   assert sol_independent_set in [[1,0,0],[0,1,0],[0,0,1]]
   assert sol_clique in [[1,1,1]]


test()

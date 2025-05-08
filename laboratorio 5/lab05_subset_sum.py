from time import time
from itertools import permutations

def tuple2list(a):
    return list(a) if type(a) == tuple else a


# la funcion has_sum, dada una coleccion de positivos y un valor "value", decide si
# hay una subcoleccion de positivos que sumen "value" o no.    
def has_sum(value, collection):
    #TODO
    resul = False
    if value==0:
        return True
    elif collection==[]:
        return False
    elif collection[0]>value:
        resul=has_sum(value,collection[1:])
    else:
        resul=(has_sum(value-collection[0],collection[1:]) or has_sum(value,collection[1:]))
    return resul

# la funcion subset, dada una coleccion de positivos y un valor "value", si existe
# una subcoleccion de positivos que sumen "value" devuelve dicha subcoleccion.
# En otro caso devuelve la lista [None].    
def subset(value, collection):
    #TODO
    '''ha tardado 12.0749998093 segundos la coleccion 6'''
    resul = []
    if value==0:
        return resul
    elif collection==[]:
        return [None]
    elif collection[0]>value:
        return subset(value,collection[1:])
    else:
        resul1=subset(value-collection[0],collection[1:])
        if resul1!=[None]:
            resul.extend(resul1)
            resul.append(collection[0])
            return resul
        else:
            return subset(value,collection[1:])
    return resul

    
def test():
    
    # coleccion 0
    collection0 = [3, 11, 8, 13, 16, 1, 6]
    value0 = 59
    
    # Primera coleccion
    collection1 = [3, 11, 8, 13, 16, 1, 6]
    value1 = 21
    
    sol11 = [3, 11, 1, 6]
    perm11 = map(tuple2list, permutations(sol11))
    perm12 = [[13, 8], [8, 13]]
   
    # Segunda coleccion
    collection2 = [518533, 1037066, 2074132, 1648264,
                   796528, 1593056, 686112, 1372224,
                   244448, 488896, 977792, 1955584,
                   1411168, 322336, 644672, 1289344,
                   78688, 157376, 314752, 629504, 1259008]
    value2 = 2463098
    
    sol21 = subset(value2, collection2) 
    perm21 = map(tuple2list, permutations(sol21))
    
    # Tercera coleccion
    collection3 = [15, 22, 14, 26, 32, 9, 16, 8]
    value3 = 53
    
    sol31 = [15, 22, 16]
    perm31 = map(tuple2list, permutations(sol31))
    sol32 = [14, 15, 16, 8]
    perm32 = map(tuple2list, permutations(sol32))    
    sol33 = [9, 22, 14, 8]
    perm33 = map(tuple2list, permutations(sol33))
    
    #Cuarta coleccion
    collection4 = [1,5,6]
    value4 = 6
    perm41 = [[6], [1, 5], [5, 1]]
    
    #Quinta coleccion
    collection5 = [4,5,1]
    value5 = 6
    perm51 = [[1, 5], [5, 1]]
    

    
#   DESCOMENTAR PARA PROBAR HAS_SUM
#######################################################    
    '''assert not has_sum(value0, collection0)
    assert has_sum(value1, collection1)
    assert has_sum(value2, collection2)
    assert has_sum(value3, collection3)
    assert has_sum(value4, collection4)
    assert has_sum(value5, collection5)'''
    
    
    
#   DESCOMENTAR PARA PROBAR SUBSET
###############################################################
    '''assert subset(value0, collection0) == [None]
    assert subset(value1, collection1) in perm11 + perm12 
    assert subset(value2, collection2) in perm21
    assert subset(value3, collection3) in perm31 + perm32 + perm33
    assert subset(value4, collection4) in perm41 
    assert subset(value5, collection5) in perm51'''



### PARA MEDIR TIEMPO USA ESTA COLECCION QUE NO TIENE SUBCOLECCIONES
### QUE SUMEN VALUE5
####################################################################    
    collection6 = range(1,25)
    value6 = 301
    assert subset(value6, collection6) == [None] 

'''ha tardado 12.0749998093 segundos la coleccion 6'''
    
start_time = time()
test()
elapsed_time = time() - start_time   
print("Elapsed time: %0.10f seconds." % elapsed_time)   

from typing import Set, Any
from TdP_collections.graphs.graph import Graph


"""
Scrivere una funzione bipartite() che, preso in input un grafo G non diretto, verifica
se G è bipartito e restituisce una partizione (X, Y) dei vertici di G tale che tutti gli
archi del grafo collegano un vertice di X ad un vertice di Y. Nel caso in cui il grafo non
sia bipartito la funzione deve restituire None. Analizzare la complessità della
funzione proposta.
"""

def bipartite(g):
    discovered = {}

    for u in g.vertices():  # prendo un vertice di partenza
        s = u
        break
        
    red = set()
    blue = set()
    level = [s]
    nb = 0                   # variabile non bipartito a 0
    red.add(s)               # coloro di rosso il primo vertice

    while len(level) > 0 and nb == 0:
        next_level = []
        for u in level:
            if u in red:       # salvo il colore del vertice che si trova nel livello
                color = 1
            elif u in blue:
                color = 2
            for e in g.incident_edges(u):
                if nb == None:            # se nel vertice precedente si è verificata la condizione di non bipartizione usciamo dal ciclo
                    break
                else:
                    v = e.opposite(u)     # prendo i vertici collegati a quello attuale
                    if v not in discovered:  # se non sono stati ancora visitati li inserisco in discovered e nel livello successivo
                        discovered[v] = e
                        next_level.append(v)
                        if color == 1:
                            blue.add(v)  # se il vertice attuale è rosso coloro quelli collegati di blu
                        elif color == 2:
                            red.add(v)  # se il vertice attuale è blu coloro quelli collegati di rosso
                    else:
                        if v in red and color == 1 or v in blue and color == 2:  # se i vertici collegati a quello attuale sono già stati visitati controllo il loro colore e se è lo stesso
                            nb = None  # attuale imposto la variabile non bipartito a None

        level = next_level  # vado a controllare il livello successivo
    return nb, red, blue  # ritorno il valore di nb e le due partizioni


if __name__ == '__main__':

    gbi = Graph()      #GRAFO UNO

    a = gbi.insert_vertex("A")
    b = gbi.insert_vertex("B")
    c = gbi.insert_vertex("C")
    d = gbi.insert_vertex("D")
    e = gbi.insert_vertex("E")

    gbi.insert_edge(a, b)
    gbi.insert_edge(a, c)
    gbi.insert_edge(b, d)
    gbi.insert_edge(d, e)
    gbi.insert_edge(e, a)

    gbi2 = Graph()    #GRAFO DUE

    a = gbi2.insert_vertex("A")
    b = gbi2.insert_vertex("B")
    c = gbi2.insert_vertex("C")
    d = gbi2.insert_vertex("D")
    e = gbi2.insert_vertex("E")

    gbi2.insert_edge(a, b, None)
    gbi2.insert_edge(a, e, None)
    gbi2.insert_edge(b, c, None)
    gbi2.insert_edge(d, e, None)

    gnbi = Graph()   #GRAFO TRE

    a = gnbi.insert_vertex("A")
    b = gnbi.insert_vertex("B")
    c = gnbi.insert_vertex("C")
    d = gnbi.insert_vertex("D")
    e = gnbi.insert_vertex("E")

    gnbi.insert_edge(a, b, None)
    gnbi.insert_edge(a, c, None)
    gnbi.insert_edge(b, d, None)
    gnbi.insert_edge(c, e, None)
    gnbi.insert_edge(d, e, None)

    gnbi2 = Graph()  #GRAFO QUATTRO

    a = gnbi2.insert_vertex("A")
    b = gnbi2.insert_vertex("B")
    c = gnbi2.insert_vertex("C")
    d = gnbi2.insert_vertex("D")
    e = gnbi2.insert_vertex("E")

    gnbi2.insert_edge(a, b, None)
    gnbi2.insert_edge(a, e, None)
    gnbi2.insert_edge(b, c, None)
    gnbi2.insert_edge(c, d, None)
    gnbi2.insert_edge(d, e, None)





    a, rosso, blu = bipartite(gbi)  # per fare test ci sono quattro grafi due bipartiti gbi e gbi2 e due non bipartiti gnbi e gnbi2
    print("\nTEST PRIMO GRAFO\n")
    if (a == None):
            print("\nGrafo non bipartito")
            print("\n-------------------------------------------------------\n")
    else:
        print("Grafo bipartito\n")
        print("Partizione X\n")
        for i in rosso:
            print(i)
        print("\nPartizione Y\n")
        for c in blu:
            print(c)
        print("\n-------------------------------------------------------\n")


    a, rosso, blu = bipartite(gbi2)  # per fare test ci sono quattro grafi due bipartiti gbi e gbi2 e due non bipartiti gnbi e gnbi2
    print("\nTEST SECONDO GRAFO\n")
    if (a == None):
            print("\nGrafo non bipartito")
            print("\n-------------------------------------------------------\n")
    else:
        print("Grafo bipartito\n")
        print("Partizione X\n")
        for i in rosso:
            print(i)
        print("\nPartizione Y\n")
        for c in blu:
            print(c)
        print("\n-------------------------------------------------------\n")



    a, rosso, blu = bipartite(gnbi)  # per fare test ci sono quattro grafi due bipartiti gbi e gbi2 e due non bipartiti gnbi e gnbi2
    print("\nTEST TERZO GRAFO\n")
    if (a == None):
            print("\nGrafo non bipartito")
            print("\n-------------------------------------------------------\n")
    else:
        print("Grafo bipartito\n")
        print("Partizione X\n")
        for i in rosso:
            print(i)
        print("\nPartizione Y\n")
        for c in blu:
            print(c)
        print("\n-------------------------------------------------------\n")






    a, rosso, blu = bipartite(gnbi2)  # per fare test ci sono quattro grafi due bipartiti gbi e gbi2 e due non bipartiti gnbi e gnbi2
    print("\nTEST QUARTO GRAFO\n")
    if (a == None):
            print("\nGrafo non bipartito")
            print("\n-------------------------------------------------------\n")
    else:
        print("Grafo bipartito\n")
        print("Partizione X\n")
        for i in rosso:
            print(i)
        print("\nPartizione Y\n")
        for c in blu:
            print(c)
        print("\n-------------------------------------------------------\n")



























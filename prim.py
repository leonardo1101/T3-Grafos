# coding=utf-8
import networkx as nx


# algoritmo de Prim, retornando a minimum spanning tree mst
def mst_prim(G, r):

    # for each v ∈ V {
    #     λ(v) = ∞
    #     π(v) = NIL
    # }
    #
    # λ(r) = 0
    # Q = V
    #
    # while Q > 0 {
    #   u = ExtractMin(Q)
    #   for each v ∈ N(u) {
    #       if v ∈ Q and λ(v) > w(u, v) {
    #           λ(v) = w(u, v)
    #           π(v) = u
    #       }
    #   }
    # }

    # fila de prioridades e visitados
    queue, visitados = [], []


    # for each v ∈ V { λ(v) = ∞ ; π(v) = NIL }
    lambdas = [float("inf")] * G.number_of_nodes()
    pi = [None] * G.number_of_nodes()

    # λ(r) = 0
    lambdas[r] = 0

    # Q = V
    for v in G.nodes():
        queue.append((lambdas[v], v))

    # while Q > 0
    while len(queue) > 0:

        # u = ExtractMin(Q) ///// fila ordenada pelo valor do lambda para extrair o min
        queue.sort()

        # remove a tupla <lambda, v> com menor lambda e pega apenas o v
        u = queue.pop(0)[1]
        visitados.append(u)

        # for each v ∈ N(u) /// para cada neighbor de u
        for v in G.neighbors(u):

            # if v ∈ Q and λ(v) > w(u, v) /// se v nao tiver sido visitado e a se lambda de v for maior que distancia de u e v
            if not v in visitados and lambdas[v] > G[u][v]['weight']:

                # λ(v) = w(u, v) /// remove a tupla <lambda, v> da fila de prioridades, atualiza seu valor, e depois recoloca a mesma na fila
                queue.remove((lambdas[v], v))
                lambdas[v] = G[u][v]['weight']
                queue.append((lambdas[v], v))

                # π(v) = u
                pi[v] = u

    # criacao da mst, na qual iremos colocar os valores resultantes do algoritmo
    mst = nx.Graph()

    # adição dos nós na MST com seus respectivos pesos
    for u in G.nodes():
        mst.add_node(u)

        # definimos o predecessor para cada vertice u pertencente ao nosso grafo G
        if pi[u] is not None:

            # colocamos à aresta de seu predecessor
            mst.add_edge(u, pi[u])

            # colocamos o peso (distancia) do nosso precedessor
            mst[u][pi[u]]['weight'] = G[u][pi[u]]['weight']

    # retornamos mst
    return mst



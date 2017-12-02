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
    # while Q ≠ 0 {
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

    # for each v ∈ V {
    for v in G.nodes():

        # λ(v) = ∞
        G.node[v]['lambda'] = float("inf")

        # π(v) = NIL
        G.node[v]['pi'] = None

    # λ(r) = 0
    G.node[r]['lambda'] = 0

    # Q = V
    for v in G.nodes():
        queue.append((G.node[v]['lambda'], v))

    # while Q ≠ 0
    while len(queue) > 0:

        # u = ExtractMin(Q) ///// fila ordenada pelo valor do lambda para extrair o min
        queue.sort()

        # remove a tupla <lambda, v> com menor lambda e pega apenas o v
        u = queue.pop(0)[1]
        visitados.append(u)

        # for each v ∈ N(u) /// para cada neighbor de u
        for v in G.neighbors(u):

            # if v ∈ Q and λ(v) > w(u, v) /// se v nao tiver sido visitado e a se lambda de v for maior que distancia de u e v
            if not v in visitados and G.node[v]['lambda'] > G[u][v]['weight']:

                # λ(v) = w(u, v) /// remove a tupla <lambda, v> da fila de prioridades, atualiza seu valor, e depois recoloca a mesma na fila
                queue.remove((G.node[v]['lambda'], v))
                G.node[v]['lambda'] = G[u][v]['weight']
                queue.append((G.node[v]['lambda'], v))

                # π(v) = u
                G.node[v]['pi'] = u

    # criacao da mst, na qual iremos colocar os valores resultantes do algoritmo
    mst = nx.Graph()

    # adição dos nós na MST com seus respectivos pesos
    for u in G.nodes():
        mst.add_node(u)

        # definimos o predecessor para cada vertice u pertencente ao nosso grafo G
        if G.node[u]['pi'] is not None:

            # colocamos à aresta de seu predecessor
            mst.add_edge(u, G.node[u]['pi'])

            # colocamos o peso (distancia) do nosso precedessor
            mst[u][G.node[u]['pi']]['weight'] = G[u][G.node[u]['pi']]['weight']

    # retornamos mst
    return mst



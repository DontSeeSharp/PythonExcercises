"""EX15."""
import networkx as nx

labyrinth5 = [[' ', ' ', ' ', ' '],
              [' ', ' ', 'X', ' '],
              ['X', ' ', ' ', ' '],
              ['X', 'X', 'X', ' ']]

labyrinth7 = [[' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              [' ', ' ', ' ', 'X', ' ', 'X', ' ', 'X'],
              ['X', 'X', ' ', ' ', ' ', ' ', ' ', 'X'],
              ['X', ' ', ' ', 'X', 'X', ' ', 'X', 'X'],
              ['X', ' ', 'X', 'X', 'X', ' ', 'X', 'X'],
              ['X', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', ' ', ' ']]


def create_list_of_moves(labyrinth):
    """
    Create  list of moves.

    args:
    labyrinth - ASCII labyrinth

    returns:
    A list, which has nodes as string in the right order for creating edges.
    """
    list_of_moves = []
    alphabet = "ABCDEFGHIJKLMNOPQRSZTUVWÕÄÖÜXY"
    for list_num in range(len(labyrinth)):

        for char_num in range(len(labyrinth[list_num])):
            try:
                if labyrinth[list_num][char_num] == ' ' and labyrinth[
                        list_num][char_num + 1] == ' ':
                    list_of_moves.append(
                        (alphabet[list_num] + str(char_num), alphabet[list_num] + str(char_num + 1)))
            except IndexError:
                pass

            try:
                if labyrinth[list_num][char_num] == ' ' and list_num - \
                        1 >= 0 and labyrinth[list_num - 1][char_num] == ' ':
                    list_of_moves.append(
                        (alphabet[list_num - 1] + str(char_num), alphabet[list_num] + str(char_num)))
            except IndexError:
                pass
    return list_of_moves


def create_graph(labyrinth):
    """
    Take ASCII map and return  networkx graph.

    args:
    labyrinth - ASCII map that contains list of lists.
    returns:
    networkx graph with weights
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSZTUVWÕÄÖÜXY"
    last_node = alphabet[len(labyrinth) - 1] + str(len(labyrinth))
    list_of_moves = create_list_of_moves(labyrinth)
    G = nx.MultiGraph(labyrinth1=labyrinth)

    for i in list_of_moves:
        G.add_edge(i[0], i[1], weight=1)

    for i in nx.nodes(G):
        print(i)
        if len(G.neighbors(i)) == 2 and i != 'A0' and i != last_node:
            j = G[i][G.neighbors(i)[0]][0]['weight']
            k = G[i][G.neighbors(i)[1]][0]['weight']

            G.add_edge(G.neighbors(i)[0], G.neighbors(i)[1], weight=(j + k))

            G.remove_edge(i, G.neighbors(i)[1])
            G.remove_edge(i, G.neighbors(i)[0])
            G.remove_node(i)

    for i in nx.nodes(G):
        G.node[i]['lastnode'] = 0

    if len(labyrinth) > 1:
        last_node = alphabet[len(labyrinth) - 1] + str(len(labyrinth[0]) - 1)
        G.node[last_node]['lastnode'] = 1
    else:
        G.add_node("A0")

    return G


def create_graph2(labyrinth):
    """
    Take ASCII map and return networkx graph.

    args:
    labyrinth - ASCII map that contains list of lists.
    returns:
    networkx graph without weights
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSZTUVWÃÃÃÃXY"
    list_of_moves = create_list_of_moves(labyrinth)
    G = nx.Graph()

    for i in list_of_moves:
        G.add_edge(i[0], i[1])

    for i in nx.nodes(G):
        G.node[i]['lastnode'] = 0

    if len(labyrinth) > 1:
        last_node = alphabet[len(labyrinth) - 1] + str(len(labyrinth[0]) - 1)
        G.node[last_node]['lastnode'] = 1
    else:
        G.add_node("A0")

    return G


def find_shortest_path(graph):
    """
    Take networkx graph and calculate the shortest path.

    args:
    graph - a networkx graph
    returns:
    List, that contains shortest path
    """
    G1 = graph
    G = create_graph2(G1.graph['labyrinth1'])

    list_of_nodes = nx.nodes(G)

    if len(list_of_nodes) == 1:
        return list_of_nodes

    for i in list_of_nodes:
        if i.count("A0") == 1:
            start_node = i
        if G.node[i]['lastnode'] == 1:
            end_node = i

    length = nx.astar_path(G, start_node, end_node)
    return length

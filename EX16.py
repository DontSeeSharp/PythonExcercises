"""EX16."""
import networkx as nx


def set_node_colors(G):
    """
    Set G.node[node]['color'] attribute for all nodes according to priorities and rules.

    Args:
    G - networkx graph
    Returns:
    G - networkx graph
    """
    for node in nx.nodes(G):
        if G.node[node]['color'] == 'none':
            G = set_node_color(G, node)
        G = set_neighbor_colors(G, node)

    return G


def set_node_color(G, node):
    """
    Set G.node[node]['color'] attribute for a single node according to priorities and rules.

    Args:
    G - networkx graph
    node - a node to set the attribute to
    Returns:
    G - networkx graph
    """
    if G.node[node]['color'] == 'none':
        priority_list = [0, 0, 0, 0]

        for neighbor in G.neighbors(node):
            if G.node[neighbor]['color'] != 'none':
                priority_list[G.node[neighbor]['color']] = 1

        node_color = priority_list.index(0)
        G.node[node]['color'] = node_color

    return G


def set_neighbor_colors(G, node):
    """
    Set G.node[node]['color'] attribute for node neighbors.

    Args:
    G - networkx graph
    node - a node which neighbors get their attribute modified
    Returns:
    G - networkx graph
    """
    for neighbor in G.neighbors(node):
        G = set_node_color(G, neighbor)

    return G


def create_color_none_graph(adjacency_matrix, G):
    """
    Create graph with G.node[node]['color'] attribute 0 on all nodes.

    Args:
    Input: adjacency_matrix - graph adjacency_matrix where [x][y] = 1 means
                              that region x and region y share common border.
    G - empty networkx graph
    Returns:
    G - networkx graph
    """
    for row_num in range(len(adjacency_matrix)):
        for index_num in range(row_num):
            if adjacency_matrix[row_num][index_num] == 1:
                G.add_edge(row_num, index_num)
                G.node[row_num]['color'] = 'none'
                G.node[index_num]['color'] = 'none'
    return G


def get_region_colors(adjacency_matrix):
    """
    Calculate color for each region in the graph.

    Input: adjacency_matrix - graph adjacency_matrix where [x][y] = 1 means
                              that region x and region y share common border.

    Output: colors_dictionary - dictionary object where key is region number
                                and value is color (witches - 1, vampires - 2, werewolves - 3, hybrids - 4)
    """
    G = nx.Graph()
    colors_dictionary = {}

    if len(adjacency_matrix) == 1:
        colors_dictionary[0] = 1
        return colors_dictionary

    G = create_color_none_graph(adjacency_matrix, G)
    G = set_node_colors(G)

    for node in nx.nodes(G):
        node_color = G.node[node]['color']
        node_color += 1
        G.node[node]['color'] = node_color

    for node in nx.nodes(G):
        colors_dictionary[node] = G.node[node]['color']

    return colors_dictionary


def get_graph(adjacency_matrix):
    """
    Create colored graph from adjacency_matrix.

    Input: adjacency_matrix - graph adjacency_matrix where [x][y] = 1 means
                              that region x and region y share common border.
    Output: network_x_graph_object - plottable networkx graph
    """
    G = nx.Graph()

    if len(adjacency_matrix) == 1:
        G.add_node("0")
    else:
        for row_num in range(len(adjacency_matrix)):
            for index_num in range(row_num):
                if adjacency_matrix[row_num][index_num] == 1:
                    G.add_edge(row_num, index_num)
    return G

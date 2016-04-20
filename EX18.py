"""EX18."""
import networkx as nx


def bfs_memory(nodes, probability, start, end):
    """
    Function to implement breath-first search memoryzing (using a queue) the nodes already visited.

    Using NetworkX to generate a random unweighted graph with nodes and probability of forming edges.
    Arguments:
    nodes: number of nodes in the random graph. Should be >10 (e.g. 20)
    probability: probability to generate edges between nodes (e.g. 0.2)
    start: starting node for breath-first search (e.g. 2)
    end: ending node for breath-first search (e.g. 10)
    Returns:
    set:nodes visited
    """
    G = nx.fast_gnp_random_graph(nodes, probability)

    for node in nx.nodes(G):
        if len(G.neighbors(node)) == 0:
            G.remove_node(node)

    if len(nx.nodes(G)) == 0:
        return False

    visited_list = [start]
    node_list = [start]

    while True:
        if end in node_list:
            return visited_list

        if len(node_list) == 0:
            return False

        current_node = node_list[0]

        node_list.pop(0)

        if current_node not in visited_list:
            visited_list.append(current_node)

        for node in G.neighbors(current_node):
            if node not in visited_list:
                node_list.append(node)

    return False


def bfs_without_memory(nodes, probability, start, end):
    """
    Function to implement breath-first search without memoryzing (using a queue) the nodes already visited.

    Using NetworkX to generate a random unweighted graph with nodes and probability of forming edges.
    Arguments:
    nodes: number of nodes in the random graph. Should be >10 (e.g. 20)
    probability: probability to generate edges between nodes (e.g. 0.2)
    start: starting node for breath-first search (e.g. 2)
    end: ending node for breath-first search (e.g. 10)
    Returns:
    boolean: True if the path from node {start} to node {end} exists else False
    """
    G = nx.fast_gnp_random_graph(nodes, probability)

    for node in nx.nodes(G):
        if len(G.neighbors(node)) == 0:
            G.remove_node(node)

    if len(nx.nodes(G)) == 0:
        return False

    node_list = [start]
    counter = 100
    while counter != 0:
        if end in node_list:
            return True

        for node in G.neighbors(node_list[0]):
            node_list.append(node)

        node_list.pop(0)

        counter -= 1

    return False

if __name__ == '__main__':
    print(bfs_memory(20, 0.2, 1, 100))

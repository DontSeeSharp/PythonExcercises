"""EX19."""
import networkx as nx


def find_relative_iterative(graph, name):
    """
    Iterative implementation.

    Find how many nodes are visited during the depth first search.
    The algorithm must work with cycles and look through every node if
    name doesn't exist in the graph.

    Args:
    graph - family tree (networkx graph object)
    name  - searched relative (string)

    Return:
    number of nodes visited (int)
    """
    G = graph
    start = G.nodes()[0]
    print("start: " + str(start))
    visited = {start}
    visited.pop()
    stack = [start]
    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)

            for neighbor in G.neighbors(node):
                if neighbor not in visited:
                    stack.append(neighbor)

        if name in visited:
            return len(visited)
    if name not in visited:
        return False
    else:
        return len(visited)


def find_relative_recursive(graph, name):
    """
    Recursive implementation.

    Find how many nodes are visited during the depth first search.
    The algorithm must work with cycles and look through every node if
    name doesn't exist in the graph.

    Args:
    graph - family tree (networkx graph object)
    name  - searched relative (string)

    Return:
    number of nodes visited (int)
    """
    G = graph
    start = G.nodes()[0]
    print("start2:" + str(start))
    visited = {start}
    if start not in G.nodes():
        return False
    if start == name:
        return 1
    number_visited = find_recursive(G, name, start, visited)
    return number_visited


def find_recursive(graph, name, start, visited):
    """
    Recursive implementation.

    Find how many nodes are visited during the depth first search.
    The algorithm must work with cycles and look through every node if
    name doesn't exist in the graph.

    Args:
    graph - family tree (networkx graph object)
    name  - searched relative (string)
    start - the node to start(continue) from
    visited - visited node set

    Return:
    number of nodes visited (int)
    """
    G = graph

    if name in visited:
        return

    for node in G.neighbors(start):
        if node not in visited and name not in visited:
            visited.add(node)
            find_recursive(G, name, node, visited)

    if name in visited:
        return len(visited)
    else:
        return False


if __name__ == "__main__":

    example_graph = nx.Graph()

    example_graph.add_node("Mari")

    print(find_relative_iterative(example_graph, "Mari"))  # 1

    print(find_relative_recursive(example_graph, "Mari"))  # 1

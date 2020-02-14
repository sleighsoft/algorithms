def tarjan(connections, nserver):
    """Implements Tarjan's algorithm for finding Strongly
    Connected Components.
    
    The algorithm is used to compute critical edges in a server landscape.
    A critical edge is an edge, that if it fails, part of the servers are no
    longer reachable.
    
    Args:
        connections (List[(node1, node2)]): A list of tuple storing edges
            between nodes as intengers.
        nserver (int): The total number of servers

    Returns:
        critical_connections(List[(node1,node2)]): A list of storing critical
            connections, that if they fail, lead to unreachable servers.
    """
    n = nserver

    adjacent = [[] for _ in range(n)]
    low = [0] * n
    identifier = [0] * n
    critical_connections = []
    depth = [0]

    for i, v in connections:
        i -= 1
        v -= 1
        adjacent[i].append(v)
        adjacent[v].append(i)

    def dfs_visit(current, parent):
        # Increment ID
        depth[0] += 1
        # ID
        identifier[current] = depth[0]
        # Lowest ID node that can be reached from this one
        # - Will be updated on backwards pass
        low[current] = depth[0]

        # Loop through all neighbors
        for n in adjacent[current]:
            # In case there is an edge going back, skip it
            # => Graph is bidirectional anyway
            if n == parent:
                continue
            # Check if neighbor node has already been visited
            if identifier[n] == 0:
                # Recursion
                dfs_visit(n, current)

                # If there is no way back to the original node,
                # then we have found a critical edge
                if low[n] > identifier[current]:
                    critical_connections.append((n + 1, current + 1))
            # If the neighboring node can reach an ancestor of
            # the current node, then this node can also reach it.
            # Pick the lowest node that can be reached.
            low[current] = min(low[current], low[n])

    dfs_visit(0, -1)
    return critical_connections


if __name__ == "__main__":
    print(tarjan([(1, 2), (1, 3), (3, 4), (1, 4), (4, 5)], 5))
    print(
        tarjan(
            [
                (1, 2),
                (1, 3),
                (2, 3),
                (3, 4),
                (4, 6),
                (4, 5),
                (5, 6),
                (5, 7),
                (6, 7),
                (7, 8),
                (8, 9),
                (8, 10),
                (9, 10),
            ],
            10,
        )
    )
    print(tarjan([(1, 2), (2, 3), (3, 4), (4, 2)], 4))


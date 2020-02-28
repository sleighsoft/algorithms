def kruskal(connections):
    """Greedy algorithm for the computation of minimal spanning trees (MST) of
    undirected graphs.
    
    Args:
        connections (List[(node1, node2, weight)]): A list of tuple storing edges
            between nodes as intengers and an edge weight.

    Returns:
        mst (List[(node1, node2, weight)]): The minimal spanning tree given
            `connections`.
    """

    def union(array, a, b):
        """Part of the union-find data structure for finding disjoint sets.

        Changes `array` so that `b` is part of `a`. Replaces all occurrences
        of `array[b]` with `array[a]`.
        
        Args:
            array (List): The union-find array.
            a (Any): Index into `array`.
            b (Any): Index into `array`. Will be unioned with `a`.
        """
        change = array[b]
        new = array[a]
        for i in range(len(array)):
            if array[i] == change:
                array[i] = new

    def find(array, a, b):
        """Part of the union-find data structure for finding disjoint sets.

        Checks if `array[a] == array[b]`.
        
        Args:
            array (List): The union-find array.
            a (Any): Index into `array`.
            b (Any): Index into `array`. Will be unioned with `a`.
        
        Returns:
            [bool]: True if `a` and `b` are joined.
        """
        return array[a] == array[b]

    sorted_connections = sorted(connections, key=lambda x: x[2])

    max_node_id = 0
    for e in connections:
        max_node_id = max(max_node_id, e[0], e[1])

    union_find_array = [i for i in range(max_node_id + 1)]

    mst = []
    for e in sorted_connections:
        if not find(union_find_array, e[0], e[1]):
            union(union_find_array, e[0], e[1])
            mst.append(e)
    return mst


if __name__ == "__main__":
    graph = [
        (0, 1, 7),
        (1, 2, 8),
        (2, 4, 5),
        (3, 0, 5),
        (3, 1, 9),
        (4, 1, 7),
        (4, 3, 15),
        (5, 3, 6),
        (5, 4, 8),
        (6, 5, 11),
        (6, 4, 9),
    ]

    mst = kruskal(graph)
    print(mst)

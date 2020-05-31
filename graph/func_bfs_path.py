# -*- coding: utf-8 -*-
from collections import (defaultdict, deque)

def bfs_path(graph, start, end):
    """
    BFS最短路径

    Parameters
    ----------
    graph : defaultdict
        图.
    start : str
        起点.
    end : str
        终点.

    Returns
    -------
    list
        最短路径.

    """
    queue = deque([start])
    visited = {start}
    path = {start: None}
    
    while queue:
        node_curt = queue.popleft()
        
        for node_next in graph[node_curt]:
            if node_next not in visited:
                visited.add(node_next)
                queue.append(node_next)
                path[node_next] = node_curt
            
    lst_path = []
    while end:
        lst_path.append(end)
        end = path[end]
    
    return " -> ".join(lst_path[::-1])


if __name__ == "__main__":
    graph = defaultdict(list)
    graph["A"] = ["B", "C"]
    graph["B"] = ["A", "D", "C"]
    graph["C"] = ["A", "B", "D", "E"]
    graph["D"] = ["B", "C", "F"]
    graph["E"] = ["C", "D"]
    graph["F"] = ["D"]
    print("graph \n", graph)
    
    start = "A"
    end = "E"
    
    shortest_path = bfs_path(graph, start, end)
    print(shortest_path)

# -*- coding: utf-8 -*-
from collections import (defaultdict, deque)

def bfs_step(graph, start, end):
    """
    BFS最小步数

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
    int
        最小步数.

    """
    queue = deque([(start, 0)])
    visited = {start}
    
    while queue:
        node_curt, step_curt = queue.popleft()
        
        for node_next in graph[node_curt]:
            if node_next == end:
                return step_curt + 1
            else:
                if node_next not in visited:
                    visited.add(node_next)
                    queue.append((node_next, step_curt+1))
    
    return 0
    
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
    
    minimum_step = bfs_step(graph, start, end)
    print(minimum_step)

import heapq
import collections 
from typing import List

class NetworkDelayTime:
    """
    Problem: Network Delay Time (LeetCode #743) 
    
    Signal is sent from a given node. Get the min time it takes all nodes to receive the signal. 

    Key Insights: 
    1. Use Dijkstra's algorithm to get the shortest path from start node to every other node in the graph 

    Time Complexity: O(E log E): Each edge is added to the heap once and removed once. Each heap push / pop takes O (log E) time. 
    Space Complexity: O(E + V), E = number of edges, V = number of vertices (nodes)
        1. edges: O(E)
        2. min heap: O(V)
        3. visited: O(V)
    """

    def network_delay_time(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))

        min_heap = [(0, k)]
        visited = set()
        t = 0

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited:
                continue 
            visited.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w1 + w2, n2))
        
        return t if len(visited) == n else -1 


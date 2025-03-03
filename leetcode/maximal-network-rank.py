class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph, res = defaultdict(list), 0

        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        for n1 in range(n-1):
            for n2 in range(n1+1, n):
                visited = set()
                for adj in graph[n1]:
                    visited.add((min(adj, n1), max(adj, n1)))
                
                for adj in graph[n2]:
                    visited.add((min(adj, n2), max(adj, n2)))
                
                res = max(res, len(visited))
        
        return res

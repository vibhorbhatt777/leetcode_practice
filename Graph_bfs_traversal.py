from collections import deque
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        n = len(adj)
        ans = []
        queue = deque()
        visited = [0] * n
        starting_node = 0
        queue.append(starting_node)
        visited[starting_node] = 1
        
        while queue:
            current = queue.popleft()
            ans.append(current)
            
            for node in adj[current]:
                if not visited[node]:
                    queue.append(node)
                    visited[node] = 1
        
        return ans

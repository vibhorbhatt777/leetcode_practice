class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        # code here
        n = len(adj)
        visited = [0] * n
        result = []
        
        def dfs_helper(node):
            visited[node] = 1
            result.append(node)
            
            for neighbor in  adj[node]:
                if not visited[neighbor]:
                    dfs_helper(neighbor)
            
        dfs_helper(0)
        
        return result
        
        

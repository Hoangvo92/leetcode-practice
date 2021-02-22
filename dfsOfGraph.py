#User function Template for python3
#For directed Graph
class Solution:

 
    def dfsOfGraph(self, V, adj):
        # code here
        s = 0
        visited = [False for i in range(V)] 
 
        # Create a stack for DFS 
        stack = []
 
        # Push the current source node. 
        stack.append(s) 
        ans = list()
        while (len(stack)): 
            # Pop a vertex from stack and print it 
            s = stack[-1] 
            stack.pop()
 
            # Stack may contain same vertex twice. So 
            # we need to print the popped item only 
            # if it is not visited. 
            if (not visited[s]): 
               # print(s,end=' ')
                ans.append(s)
                visited[s] = True
 
            # Get all adjacent vertices of the popped vertex s 
            # If a adjacent has not been visited, then push it 
            # to the stack. 
            for node in adj[s]: 
                if (not visited[node]): 
                    stack.append(node) 
        
        return ans


#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob = Solution()
        ans = ob.dfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
        

# } Driver Code Ends





#for undirected graph
#User function Template for python3

class Solution:
    
    def DFSUtil(self, v, visited, adj):
 
        # Mark the current node as visited
        # and print it
        visited.append(v)
       # print(v, end=' ')
        
 
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in adj[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited, adj)

 
    def dfsOfGraph(self, V, adj):
        # code here
        s = 0
        visited = list()
 
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(s, visited, adj)
 
        # Create a stack for DFS 

        
        return visited


#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob = Solution()
        ans = ob.dfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
        

# } Driver Code Ends
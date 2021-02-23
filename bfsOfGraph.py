#User function Template for python3

class Solution:

                
    def bfsOfGraph(self, V, adj):
        # code here
        s = 0
        visited = [False for i in range(V)] 
 

        queue = []
 
        # Push the current source node. 
        queue.append(s) 
        ans = list()
        while (len(queue)): 
           
            s = queue.pop(0)
            ans.append(s)
       
 

            # Get all adjacent vertices of the popped vertex s 
            # If a adjacent has not been visited, then push it 
            # to the stack. 
            for node in adj[s]: 
                if visited[node]== False: 
                    queue.append(node) 
                    visited[node] = True
        
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
        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
        

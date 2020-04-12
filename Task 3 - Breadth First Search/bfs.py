# N = number of nodes
# graph = {0: [1, 2], 
#          1: [3], 
#          2: [3, 4], 
#          3: [], 
#          4: [3]}    for a graph with N=5. This is a demo graph.

print("Enter the number of nodes")
N = int(input())
node_list = []
for i in range(N):
    node_list.append(i)

graph = dict.fromkeys(node_list)
for i in range(N):
    print("Enter number of connections for node {}".format(i))
    conn = int(input())
    n_list = []
    for c in range(conn):
        print("Enter the neighbour of node {}".format(i))
        n = int(input())
        n_list.append(n)
    graph[i]=n_list
    
    
    
visited = []     #it stores the nodes that have been visited
queue = []       #it stores the order in which the nodes are visited

#here node refers to the source node
def bfs(visited, queue, node): 
    visited.append(node)
    queue.append(node)
    
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        
        for neighbour in graph[s]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
                
        
bfs(visited, queue, 0)

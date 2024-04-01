from queue import PriorityQueue

h = [10,8,5,7,3,6,5,3,1,0]
g = [[0,6,0,0,0,3,0,0,0,0],
     [6,0,3,2,0,0,0,0,0,0],
     [0,3,0,1,5,0,0,0,0,0],
     [0,2,1,0,8,0,0,0,0,0],
     [0,0,5,8,0,0,0,0,5,5],
     [3,0,0,0,0,0,1,7,0,0],
     [0,0,0,0,0,7,0,0,2,0],
     [0,0,0,0,5,0,3,2,0,3],
     [0,0,0,0,5,0,0,0,3,0]]


def a_star(graph,heu,start,end):
    g = [float("inf")]*len(graph)
    g[start] = 0
    f = [float("inf")]*len(graph)
    f[start] = g[start] + heu[start]
    frontier = PriorityQueue()
    frontier.put((f[start],start))
    visited = []
    while True :
        node = frontier.get()[1]
        if node == end :
            return f[node]
        for i in range(len(graph)):
            if i not in visited and graph[node][i] != 0:
                if i not in frontier:
                    frontier.put((f[i],i))
                if g[i] > graph[node][i]+ g[node]:
                    g[i] = graph[node][i] + g[node]
                    f[i] = heu[i]+g[i]


print(a_star(g,h,0,9))



            
        





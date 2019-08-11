

inf=1000000000

graph = {
        0:[inf,3,10,1],
        1:[3,inf,inf,100],
        2:[10,inf,inf,3],
        3:[1,100,10,inf]}


# 0-3


routes = []

def rec_find_shortest_path(visited, now,prev,end):
    temp = visited
    if now == end:
        routes.append(visited)
        return 1
    paths =graph[now]
    
    for k in paths:
        if k==inf or paths.index(k) == prev  :
            continue
        visited.append(paths.index(k))
        #print("visited",visited)
        a = rec_find_shortest_path(visited,paths.index(k),now,end)
        if a==1:
            break
        visited = temp
    return a


def find_minimum(paths):
    sums = []
    fake_routes = paths.copy()
    for r_one in fake_routes:
        zero = 0
        start = r_one[0]
        for rr in r_one[1:]:
            zero = zero + graph[start][rr]
            start=rr
        sums.append(zero)
    min_index = sums.index(min(sums))
    return min_index


def dijkstra(start,end):
    
    iclone_graph = graph[start]
    initial_routes =[]
    for ii in iclone_graph:
        if ii!=inf:
            initial_routes.append(iclone_graph.index(ii))
            
    for ir_one in initial_routes:
       visited_list = [start,ir_one]
       rec_find_shortest_path(visited_list,ir_one,0,3)
       
    return routes[find_minimum(routes)]
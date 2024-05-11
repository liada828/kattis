n, m = [int(a) for a in input().split()] # get the map size
graph = [] # save the map
for i in range(n):
    graph.append([int(d) for d in input()])

def neighbours(pos):
# calculate the neighbours of the current position
   nbs = []
   pos_x, pos_y = pos
   pos_tp = graph[pos_x][pos_y]
   x, y = pos[0]-1, pos[1]
   if x>=0 and graph[x][y] == pos_tp:
      nbs.append((x,y))
   x, y = pos[0], pos[1]-1
   if y>=0 and graph[x][y] == pos_tp:
      nbs.append((x,y))
   x, y = pos[0]+1, pos[1]
   if x<=n-1 and graph[x][y] == pos_tp:
      nbs.append((x,y))
   x, y = pos[0], pos[1]+1
   if y<=m-1 and graph[x][y] == pos_tp:
      nbs.append((x,y))
   return nbs

# search using Breadth First Search(BFS) algorithm 
def bfs_search(graph, start, target):
   que = [start]
   visited = [[False for i in range(m)] for j in range(n)]
   start_tp = graph[start[0]][start[1]]
   while(len(que) != 0):
    curr = que.pop()
    if curr==target and start_tp==1: # check current position is target or not
        print("decimal")
        return 
    elif curr==target and start_tp==0:
        print("binary")
        return
    else:
        visited[curr[0]][curr[1]] = True # mark current position as checked
    for c_x,c_y in neighbours(curr): # add the un-visited neighbours to the queue
        if not visited[c_x][c_y]:
            que.append((c_x,c_y))
   print("neither") # when the queue is empty, means that target is unreachable
            

for i in range(int(input())):
    pos = [int(d)-1 for d in input().split()]
    start = (pos[0],pos[1])
    target = (pos[2],pos[3])
    bfs_search(graph, start, target)
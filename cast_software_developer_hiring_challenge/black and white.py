import queue

n, m = map(int, input().split())

ans = {}
matrix = [[0]*n]*n
# print(matrix)

for i in range(1, n+1):
    ans[str(i)] = []
    
for i in range(m):
    u, v, w = map(int, input().split())
    ans[str(u)].append([v, w])

arr = list(map(int, input().split()))

# print(ans)

vertex = queue.Queue()

v = ans["1"]
for j in range(len(v)):
    
    if matrix[0][v[j][0]-1]==0:
        matrix[0][v[j][0]-1] = 1
        black, white = 0 ,0
        
        if arr[0]:
            white+=1
        else:
            black+=1
        
        if arr[v[j][0]-1]:
            white += 1
        else:
            black += 1
        vertex.put([v[j][0], v[j][1], black, white])

res = 10**9
flag = 0

while vertex.empty()==False:
    new_vertex = vertex.get()
    # print(new_vertex)

    v = ans[str(new_vertex[0])]
    # print(v)
    weight, black ,white = new_vertex[1], new_vertex[2], new_vertex[3]

    if new_vertex[0]==n and abs(black-white)<=1:
        flag = 1
        res = min(res, weight)

    for j in range(len(v)):
        # print(arr[v[j][0]-1])
        if matrix[new_vertex[0]-1][v[j][0]-1]==0:
            matrix[new_vertex[0]-1][v[j][0]-1] = 1
            if (arr[v[j][0]-1]):
                white += 1
            else:
                black += 1
            weight += v[j][1]
            vertex.put([v[j][0], weight, black, white])

if flag:
    print(res)
else:
    print(-1)

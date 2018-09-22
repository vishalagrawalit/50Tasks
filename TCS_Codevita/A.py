grid = input()
m, n, k = grid.split(",")
m, n, k = int(m), int(n), int(k)

matrix = []
pos = []
for i in range(m):
    matrix.append([10000]*n)
    pos.append([1000]*n)

count = 0
flag = 0

boat = []
for _ in range(k):
    val = input()
    x, y = val.split(",")
    x, y = int(x), int(y)
    x, y = m-1-y, x
    #print(x, y)
    boat.append((x, y))
    
for a in range(k):
    x, y = boat[a][0], boat[a][1]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] > abs(x-i) + abs(y-j):
                pos[i][j] = [x, y, 0]
            else:
                pos[i][j] = [i, j, 0]
            matrix[i][j] = min(abs(x-i) + abs(y-j), matrix[i][j])
            

count = 0
for a in range(k):
    x, y = boat[a][0], boat[a][1]
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==abs(x-i) + abs(y-j):
                if pos[i][j][0]!=x or pos[i][j][1]!=y:
                    if pos[i][j][2]==0:
                        pos[i][j][2] = 1
                    elif pos[i][j][2]==1:
                        pos[i][j][2] = 2
                        count+=1
            
print(count)





















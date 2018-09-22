import queue

n = int(input())

val = input()

arr = val.split(",")
#print(arr)

total = queue.Queue()
stone = queue.Queue()
d = dict()

total.put(int(arr[0]))
stone.put(0)
d[(int(arr[0]), 0)] = 1

if n>=2:
    total.put(2*int(arr[1]))
    stone.put(1)
    d[(2*int(arr[1]), 1)] = 2
    
if n>=3:
    total.put(3*int(arr[2]))
    stone.put(2)
    d[(3*int(arr[2]), 2)] = 3
    
maxi = int(arr[0])
while total.empty()==False:
    current_tot = total.get()
    current_sto = stone.get()
    jump = d[(current_tot, current_sto)]
    maxi = max(maxi, current_tot)

    if current_sto+1<=n-1:
        current = current_tot + int(arr[current_sto+1])
        # print(current_tot)
        if (current, int(current_sto+1)) not in d:
            total.put(int(current))
            stone.put(int(current_sto+1))
            d[(current, current_sto+1)] = jump
            

    if current_sto+2<=n-1:
        current = current_tot + 2*int(arr[current_sto+2])
        # print(current_tot)
        if (current, int(current_sto+2)) not in d:
            total.put(int(current))
            stone.put(int(current_sto+2))
            d[(current, current_sto+2)] = jump

    if jump!=3:
        if current_sto+3<=n-1:
            current = current_tot + 3*int(arr[current_sto+3])
            # print(current_tot)
            if (current, int(current_sto+3)) not in d:
                total.put(int(current))
                stone.put(int(current_sto+3))
                d[(current, current_sto+3)] = 3

print(maxi)




















        
    

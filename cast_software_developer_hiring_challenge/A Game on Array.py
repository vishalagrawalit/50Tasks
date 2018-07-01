n = int(input())
arr = list(map(int, input().split()))

if n&1:
    alex = arr[n//2]
    flag = 1
else:
    alex = 0
    flag = 0
bob = 0

i = 0
k, l = n//2, n//2-1
x, y = n//2-1, n//2+1
while i<n//2:
    # print(alex, bob)
    if flag==0:
        alex += max(arr[k], arr[l])
        bob += min(arr[k], arr[l])
        k+=1
        l-=1
    else:
        alex += min(arr[x], arr[y])
        bob += max(arr[x], arr[y])
        x-=1
        y+=1
    i+=1


if alex>=bob:
    print("Alex", (alex-bob))
else:
    print("Bob", (bob-alex))

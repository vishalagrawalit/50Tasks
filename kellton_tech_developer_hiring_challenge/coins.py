from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

a = Counter(arr)
# print(a)
total = sum(arr)
arr = list(set(arr))
arr.sort()
# print(arr)

if len(arr) <= 2:
    print("NO")
else:
    last = arr[0] *  a[arr[0]]

    for i in range(1, len(arr)-1):
        if total - last - arr[i]*a[arr[i]] == last:
            print("YES")
            break
        else:
            last += arr[i]*a[arr[i]]
    else:
        print("NO")

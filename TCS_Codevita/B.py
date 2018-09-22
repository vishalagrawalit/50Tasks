from math import sqrt
def divisor(n) :
    i = 2
    ans = []
    while i <= sqrt(n):
        if (n % i == 0) :
            if (n // i == i) :
                ans.append(i)
            else :
                ans.append(i)
                ans.append(n//i)
        i = i + 1

    return ans

square = []
for i in range(2, 10**5):
    if i*i>10**9:
        square.append(i*i)
        break
    square.append(i*i)

n = int(input())

count = 0
divi = divisor(n)
for i in range(len(divi)):
    for j in range(len(square)):
        if square[j]>divi[i]:
            break
        elif divi[i]%square[j]==0:
            count+=1
            break
            print(divi[i])

print(len(divi)-count)

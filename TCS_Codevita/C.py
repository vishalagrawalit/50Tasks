def prime_num(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1

    primes = []
    for i in range(2, n):
        if prime[i]:
            primes.append(i)
    return primes

primes = prime_num(10**6+5)

x, y = 0,0
l = len(primes)
d = dict()
i = 0
right, up, left, down = 1, 0, 0, 0
while i<l:
    j = 0
    while j<right and i<l:
        d[(x, y)] = primes[i]
        i+=1
        j+=1
        x+=1
    up = right
    j = 0
    while j<up and i<l:
        d[(x, y)] = primes[i]
        i+=1
        j+=1
        y+=1
    left = up+1
    j=0
    while j<left and i<l:
        d[(x, y)] = primes[i]
        i+=1
        j+=1
        x-=1
    down = left
    j = 0
    while j<down and i<l:
        d[(x, y)] = primes[i]
        i+=1
        j+=1
        y-=1
    right = down+1
        
for i in range(int(input())):
    m, n = input().split(",")
    print(d[(int(m)), int(n)])








    

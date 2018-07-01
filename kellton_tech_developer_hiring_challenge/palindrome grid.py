from collections import Counter

for _ in range(int(input())):
    n, m = map(int, input().split())

    final_word = ""
    for _ in range(n):
        s = input()
        final_word += s

    count = Counter(final_word)
    common = list(set(final_word))

    if n&1==0 and m&1==0:
        for i in range(len(common)):
            if count[common[i]]%4!=0:
                print("NO")
        else:
            print("YES")

    elif n&1==0 and m&1==1:
        flag = 0
        for i in range(len(common)):
            if count[common[i]]%4==2:
                flag+=1
            elif count[common[i]]%4==1 or count[common[i]]%4==3:
                print("NO")
                break
            if flag==m//2:
                print("NO")
                break
        else:
            print("YES")

    elif n&1==1 and m&1==0:
        flag = 0
        for i in range(len(common)):
            if count[common[i]]%4==2:
                flag+=1
            elif count[common[i]]%4==1 or count[common[i]]%4==3:
                print("NO")
                break
            if flag==n//2:
                print("NO")
                break
        else:
            print("YES")

    else:
        flag, one = 0, 0
        for i in range(len(common)):
            if count[common[i]]%4==2:
                flag+=1
            elif count[common[i]]%4==1 and one==0:
                one+=1
            elif count[common[i]]%4==1 and one==1:
                print("NO")
                break
            elif count[common[i]]%4==3:
                print("NO")
                break
            if flag==n//2 + m//2:
                print("NO")
                break
        else:
            print("YES")
























            
                    

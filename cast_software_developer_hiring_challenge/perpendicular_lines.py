#Perpendicular Lines

'''
Given 4 points of the form (xi, yi) in 2D plane,
find out if the lines formed by (x1, y1), (x2, y2) and (x3, y3), (x4, y4)
are perpendicular to each other.

NOTE:
It is NOT provided that the points are distinct i.e
the first two or the last two points may be equal too!

INPUT FORMAT:
First line T is the number of test cases. Each test case is followed by 2 lines.
The first line of every test case contains four integers (x1, y1) and (x2, y2).
The second line contains four integers (x3, y3) and (x4, y4).

OUTPUT FORMAT:
For every test case :
print "YES" without quotes if the lines are perpendicular to each other
print "NO" without quotes if the lines are not perpendicular
print "INVALID" without quotes if there are less than 2 lines
'''

for i in range(int(input())):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    if arr1[0]==arr1[2] and arr1[1]==arr1[3]:
        print("INVALID")
    elif arr2[0]==arr2[2] and arr2[1]==arr2[3]:
        print("INVALID")
    else:
        if (arr1[2]-arr1[0]) == 0:
            if (arr2[3]-arr2[1]) == 0:
                print("YES")
            else:
                print("NO")
        elif (arr2[2]-arr2[0]) == 0:
            if (arr1[3]-arr1[1]) == 0:
                print("YES")
            else:
                print("NO")
        else:
            slope1 = (arr1[3]-arr1[1])/(arr1[2]-arr1[0])
            slope2 = (arr2[3]-arr2[1])/(arr2[2]-arr2[0])

            if slope1 * slope2 == -1:
                print("YES")
            else:
                print("NO")

            

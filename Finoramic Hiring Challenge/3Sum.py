class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        mini, res = float('INF'), -1
        for i in range(0, len(A) - 2):
            a = A[i]
            start, end = i + 1, len(A) - 1
            while start < end:
                b, c = A[start], A[end]

                if abs(B - (a + b + c)) < mini:
                    mini = abs(B - (a + b + c))
                    res = a + b + c

                if a + b + c == B:
                    return B
                elif a + b + c > B:
                    end = end - 1
                else:
                    start = start + 1
        return res

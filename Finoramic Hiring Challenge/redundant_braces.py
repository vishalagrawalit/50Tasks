class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        for i in range(len(A)):
            if A[i] in ['-', '+', '*', '/', '(']:
                stack.append(A[i])
            elif A[i]==")":
                if stack[-1]=="(":
                    return 1
                while len(stack)>0 and stack[-1]!="(":
                    stack.pop()
                stack.pop()
        return 0

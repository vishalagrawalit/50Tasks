class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        sorted_words = []
        
        for i in range(len(A)):
            x = list(A[i])
            x.sort()
            x = ''.join(x)
            sorted_words.append(x)
            
        unique = list(set(sorted_words))
        
        # print(sorted_words)
        ans = []
        for i in range(len(unique)):
            res = []
            ind = -1
            while True:
                try:
                    ind = sorted_words.index(unique[i], ind+1)
                    res.append(ind+1)
                except ValueError:
                    break
            ans.append(res)
        
        return ans
            
        
        
        
        
        
        
        
        

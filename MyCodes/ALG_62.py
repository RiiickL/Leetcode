class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==1:
            return 1
        else:
            L = [1 for x in range(n)]
            for k in range(m-2):
                #Iteration:
                for k1 in range(len(L)-1):
                    L[k1+1] = L[k1]+L[k1+1]
            return sum(L)
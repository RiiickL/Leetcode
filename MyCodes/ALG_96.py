class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res_list = [1, 1]
        for length in range(2,n+1):
            res = 0
            w = length//2
            for loop in range(w):
                res = res+res_list[loop]*res_list[length-loop-1]
            res = res*2
            if length%2==1:
                res = res+res_list[w]**2
            res_list.append(res)
        return res_list[-1]
    def test(self):
        print(self.numTrees(4))
a=Solution()
a.test()        
        
        
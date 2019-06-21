class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Init:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        list_ret = [1, 2]
        
        # Loop:
        for num in range(3, n+1):
            x = list_ret[num-3]+list_ret[num-2]
            list_ret.append(x)
            
        return x
        
        
        
        
        
        
        
        
        
a = Solution()
a.climbStairs(3)

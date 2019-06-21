class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            flag = -1
        else:
            flag = 1
            
        if x>=2147483647 or x<=-2147483648:
            return 0
            
        def iteration_f(nums):
            yield 0
            res = nums
            while(res != 0):
                yield res%10
                res = res//10
        from functools import reduce
        
        result = flag*reduce(lambda a, b: 10*a+b, [c for c in iteration_f(abs(x))])
        
        if result>=2147483647 or result<=-2147483648:
            return 0
        return result

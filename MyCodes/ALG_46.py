class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def f(list_x,n,x):
            for k in range(0, n+1):
                list_y = list_x[:]
                list_y.insert(k,x)
                yield list_y
        
        list_ret = [[]]
        list_n = 0
        for x in nums:
            list_x = [y for g in list_ret for y in f(g,list_n,x)]
            list_ret = list_x[:]
            list_n = list_n+1
        return list_ret

        
a = Solution()
a.permute([1,2,3])
        
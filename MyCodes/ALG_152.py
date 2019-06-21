class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        n_head = 1
        n_tail = 1
        tmp = 1
        n_nums = 0
        for n in nums:
            if n==0:
                if n_nums==0:
                    cmp = 0
                elif n_nums==1:
                    if tmp>0:
                        cmp = tmp
                    else:
                        cmp = 0
                elif tmp>0:
                    cmp = tmp
                else:
                    cmp = max(tmp//n_head, tmp//n_tail)
                if cmp>res:
                    res = cmp
                n_head = 1
                n_tail = 1
                n_nums = 0
                tmp = 1
            else:
                n_nums = n_nums+1
                tmp = tmp*n
                if n<0:
                    if n_head==1:
                        n_head = tmp
                        n_tail = n
                    else:
                        n_tail = n
                else:
                    n_tail = n_tail*n
        
        if n_nums!=0:
            if n_nums==1:
                cmp = tmp
            elif tmp>0:
                cmp = tmp
            else:
                cmp = max(tmp//n_head, tmp//n_tail)
            if cmp>res:
                res = cmp
        
        return res
    def test(self):
        print(self.maxProduct([6,3,-10,0,2]))
a=Solution()
a.test() 
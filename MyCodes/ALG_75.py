class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos0 = 0
        posr = 0
        pos2 = len(nums)-1
        if pos2>0:
            while(True):
                if posr>pos2:
                    break
                if nums[posr]==0:
                    nums[posr] = nums[pos0]
                    nums[pos0] = 0
                    pos0 = pos0+1
                    if posr<pos0:
                        posr = posr+1
                elif nums[posr]==2:
                    nums[posr] = nums[pos2]
                    nums[pos2] = 2
                    pos2 = pos2-1
                else:
                    posr = posr+1
    def test(self):
        nums = [1,0]
        self.sortColors(nums)
        print(nums)
a = Solution()
a.test()       
        
        
        
        
        
        
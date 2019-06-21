class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n==0:
            return -1
        width = n//2
        pos = width
        flag = 2
        if(target>nums[0]):
            while(True):
                width = width//2
                if width==0:
                    if flag>0:
                        width=1
                        flag = flag-1
                    else:
                        return -1
                if pos<0 or pos>=n:
                    return -1
                if nums[pos]==target:
                    return pos
                elif nums[pos]>target:
                    pos = pos-width
                elif nums[pos]<nums[0]:
                    pos = pos-width
                else:
                    pos = pos+width
        elif target==nums[0]:
            return 0
        else:
            while(True):
                width = width//2
                if width==0:
                    if flag>0:
                        width=1
                        flag = flag-1
                    else:
                        return -1
                if pos<0 or pos>=n:
                    return -1
                if nums[pos]==target:
                    return pos
                elif nums[pos]<target:
                    pos = pos+width
                elif nums[pos]>nums[-1]:
                    pos = pos+width
                else:
                    pos = pos-width
    def test(self):
        print(self.search([4,5,6,7,0,1,2],2))
a=Solution()
a.test()
        
        
        
        
        
        
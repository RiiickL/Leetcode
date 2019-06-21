class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for k in range(n-1):
            for k1 in range(k+1,n):
                if (nums[k]+nums[k1]) == target:
                    return [k, k1]
        return None
            
            
            
        
        
        
        
        
        
        
        
        
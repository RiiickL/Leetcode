class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        sum = 0
        for k in range(len(nums)):
            sum = sum+nums[k]
            if sum>ans:
                ans = sum
            if sum<0:
                sum = 0
        return ans
        

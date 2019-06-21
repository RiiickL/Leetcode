class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m0,m1 = 0,0
        for value in nums:
            m0,m1 = max(m1,m0), value+m0
        return max(m0,m1)
            
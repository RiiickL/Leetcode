class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        min_pos = l+1
        for i in range(l):
            self.check(nums, i, l)
            
        for i in range(l):
            if nums[i] != i+1:
                min_pos = i+1
                break
        return min_pos
        
    def check(self, nums, i, l):
        j = nums[i]-1
        if i != j and nums[i]>0 and j<l:
            nums[i] = 0
            self.check(nums, j, l)
            nums[j] = j+1
            

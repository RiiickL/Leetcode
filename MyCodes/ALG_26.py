class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        else:
            count = 1 
            for check_val in nums:
                if check_val!=nums[count-1]:
                    nums[count] = check_val
                    count = count+1
        return count
        
        
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        else:
            count = 1
            for check_pos in range(len(nums)-1):
                if nums[check_pos]!=nums[check_pos+1]:
                    nums[count] = nums[check_pos+1]
                    count = count+1
        return count
        
        
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        else:
            count = 1 
            current_val = nums[0]
            for check_val in nums:
                if check_val!=current_val:
                    current_val = check_val
                    nums[count] = check_val
                    count = count+1
        return count
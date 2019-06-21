class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        set_pos = 0
        for check_val in nums:
            if check_val!=val:
                nums[set_pos] = check_val
                set_pos = set_pos+1
        return set_pos
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
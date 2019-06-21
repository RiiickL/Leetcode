class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lennums = len(nums)
        ksteps = k%lennums
        
        #save the last ksteps values:
        lastnums = list(nums[-ksteps:])
        
        for loop1 in range(ksteps):
            source_val = nums[loop1]
            target_ptr = loop1+k
            while target_ptr<lennums:
                nums[target_ptr] = source_val
                source_val = nums[target_ptr]
                target_ptr = target_ptr+k
        
        for loop1 in range(ksteps):
            nums[loop1] = lastnums[loop1]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_len = len(nums)
        if num_len<3:
            return num_len
        p_save = 0
        p_load = 1
        #determin if the last values are duplicated
        if nums[-1]==[-2]:
            dup_flag = 1
        else:
            dup_flag = 0
        while p_load<num_len:
            #determine if it is duplicate number with nums[p_save]
            if nums[p_save]!=nums[p_load]:
                #continue
                p_save = p_save+1
                nums[p_save] = nums[p_load]
                p_load = p_load+1
            else:
                #find the duplicate number,
                #crossing the number with two steps
                #untill find the differ-one
                p_save = p_save+1
                nums[p_save] = nums[p_load]
                p_load = p_load+2
                while p_load<num_len:
                    if nums[p_save]!=nums[p_load]:
                        if nums[p_load]==nums[p_load-1]:
                            #indicates this is duplicate number too!
                            #continue duplicate LOOP
                            nums[p_save+1] = nums[p_load]
                            nums[p_save+2] = nums[p_load]
                            p_save = p_save+2
                        else:
                            #indicates this is single number
                            if nums[p_save]!=nums[p_load-1]:
                                nums[p_save+1] = nums[p_load-1]
                                nums[p_save+2] = nums[p_load]
                                p_save = p_save+2
                                p_load = p_load+1
                            else:
                                nums[p_save+1] = nums[p_load]
                                p_save = p_save+1
                                p_load = p_load+1
                            break;
                    else:
                        p_load = p_load+2
        if dup_flag:
            if nums[p_save]!=nums[p_save-1]:
                nums[p_save+1] = nums[p_save]
                return p_save+2
            else:
                return p_save+1
        else:
            if nums[p_save]!=nums[-1]:
                nums[p_save+1] = nums[p_save]
                return p_save+2
            else:
                return p_save+1
a=Solution()
a.removeDuplicates([1,1,2,3])

        
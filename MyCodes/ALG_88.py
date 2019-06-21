class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # return insert position index
        def find_pos(find_num, range_from, range_to):
            d = (range_to-range_from)
            if d>1:
                range_m = range_from+d//2
                if nums1[range_m]==find_num:
                    return range_m
                elif find_num<nums1[range_m]:
                    return find_pos(find_num, range_from, range_m)
                else:
                    return find_pos(find_num, range_m, range_to)
                return range_from
            elif find_num<=nums1[range_from]:
                return range_from
            else:
                return range_to
        
        nums_pos = [0 for x in range(n)]
        
        def insert_pos(nums2_from, nums2_to, nums1_from, nums1_to):
            d = nums2_to-nums2_from
            if d>1:
                
                nums2_m = nums2_from+d//2
                
                nums1_m = find_pos(nums2[nums2_m], nums1_from, nums1_to)
                
                nums_pos[nums2_m] = nums1_m
                
                insert_pos(nums2_from, nums2_m, nums1_from, nums1_m)
                insert_pos(nums2_m, nums2_to, nums1_m, nums1_to)
        if n>0:
            pos0 = find_pos(nums2[0], 0, m-1)
            nums_pos[0] = pos0
            pos1 = find_pos(nums2[-1], pos0, m-1)
            nums_pos[-1] = pos1
        
            insert_pos(0, n, pos0, pos1)
        
        insert_num = 0
        for k in range(n):
            nums1.insert(nums_pos[k]+insert_num, nums2[k])
            insert_num = insert_num+1
        
        
        
        
        
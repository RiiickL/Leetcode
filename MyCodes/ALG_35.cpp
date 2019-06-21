int searchInsert(int* nums, int numsSize, int target) {
    
	int		loop;
	
	for(loop=0; loop<numsSize; loop++)
	{
		if(target<=nums[loop])
			return	loop;
		
	}
	
	return	numsSize;
	
}
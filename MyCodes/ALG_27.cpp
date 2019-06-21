#include	<stdio.h>
#include 	<stdlib.h>
#include	<math.h>
/*
int removeDuplicates(int* nums, int numsSize) {
    
	int		loop, loop1;
	int		countSize;
	bool	flag;
	
	if(numsSize<2)
		return numsSize;
	
	for(loop=1; loop<numsSize; loop++)
	{
		flag = true;
		for(loop1=0; loop1<countSize; loop1++)
		{
			if(nums[loop] == nums[loop1])
			{
				flag = false;
				break;
			}
			
		}
		
		if(flag)
		{
			nums[countSize] = nums[loop];
			countSize++;
			
		}
		
	}
	
	return countSize;
	
}
*/
int removeDuplicates(int* nums, int numsSize) {
    
	int		loop;
	int		count;
	
	count = 0;
	
	for(loop=1; loop<numsSize; loop++)
	{
		if(nums[loop] == nums[loop-1])
			count++;
		else
			nums[loop-count] = nums[loop];
	}
	
	return numsSize-count;
	
}

void main()
{
	int			loop;
	static int			nums[]={0,1,1,0,1};
	int			output;
	int			end;
	int			size;
	
	//Main:
	size = 5;
	
	output = removeDuplicates(nums, size);
	
	printf("[%d]\n",output);
	for(loop=0; loop<output; loop++)
	{
		printf("[%d]",nums[loop]);
		
	}
	
	scanf("%d",&end);
	
	
}
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int 	loop;
	int		mod, sum;
    int 	pos_id;
    double  result;
    
	sum = nums1Size+nums2Size;
	mod = sum%2;
	if(mod == 0)
	{
		//Even number
		pos_id = sum/2 - 1;
		//the value would be the (num[pos_id]+num[pos_id+1])/2.0;
		
		if(pos_id>nums1Size)
		{
			nums2_ptr = pos_id-nums1Size;
			
			d = nums1Size;
			
			{
				if(nums1[nums1_ptr]>nums2[nums2_ptr])
				{
					nums1_ptr = nums1_ptr-d;
					nums2_ptr = nums2_ptr+d;
				}
				else
				{
					nums1_ptr = nums1_ptr+d;
					nums2_ptr = nums2_ptr-d;
				}
				
				d = d/2;
				
			}
			while(d == 0)
			
		}
		else
		{
			
		}
		
		result = 
		
		
	}
	else
	{
		//Odd number
		pos_id = (sum-1)/2;
		//the value would be the num[pos_id]*1.0;
		
	}
	
	
    
    return result;
}
#include	<stdio.h>
#include 	<stdlib.h>
#include 	<string.h>
#include	<math.h>

//version 1.0
//find out all of uncontinues substring


int lengthSubstring(char* s, int left_ptr, int right_ptr, int level)
	{
		int	loop;
		int depth_tmp;
		int depth_max;
		int	size;
		int	count;
		
		size = right_ptr - left_ptr - level + 1;
		
		if(size == 1)
		{
			if(s[left_ptr] == s[left_ptr+level])
			{
				depth_max = 0;
			}
			else
			{
				depth_max = 1;
			}
			
		}
		else
		{
			depth_max = 0;
			count = 0;
			
			for(loop=0; loop<size; loop++)
			{
				if(s[left_ptr+loop] != s[left_ptr+loop+level])
				{
					count++;
					if(loop == (size-1))
					{
						if(count > depth_max)
						{
							depth_tmp = lengthSubstring(s, left_ptr+loop-count+1, left_ptr+loop+level, level+1) + 1;
							
							if(depth_tmp > depth_max)
							{
								depth_max = depth_tmp;
							}
						}
						
					}
					
				}
				else
				{
					if(count > depth_max)
					{
						depth_tmp = lengthSubstring(s, left_ptr+loop-count, left_ptr+loop+level-1, level+1) + 1;
						
						if(depth_tmp > depth_max)
						{
							depth_max = depth_tmp;
						}
					}
					count = 0;
				}
				
			}
			
		}
		
		return depth_max;
	}


int lengthOfLongestSubstring(char* s) {
    
	int	lvi_count;
	int	s_length;
	
	s_length = strlen(s);
	
	lvi_count = lengthSubstring(s, 0, s_length-1, 1);
	
	
	return lvi_count+1;
	
}


void main()
{
	char		str_input[5];
	int			result;
	int			end;
	int			s_length;
	
	str_input[0] = 'o';
	str_input[1] = 'h';
	str_input[2] = 'o';
	str_input[3] = 'm';
	str_input[4] = 'm';
	
	//Main:
	//result = lengthOfLongestSubstring(str_input);
	//s_length = strlen(str_input);
	s_length = 5;
	result = lengthSubstring(str_input, 0, s_length-1, 1);
	
	printf("[%d]",result+1);
	
	scanf("%d",&end);
	
	
}






#include	<stdio.h>
#include 	<stdlib.h>
#include	<math.h>
#include	<string.h>

char* countAndSay(int n) {
    
	int		loop, loop1;
	int		count;
	int		length;
	char	str1[4096];
	char	str2[4096];
	int		pos;
	char	char1;
	
	memset(str1, 0, 4096);
	memset(str2, 0, 4096);
	str1[0] = '1';
	
	for(loop=0; loop<(n-1); loop++)
	{
		char1 = str1[0];
		length = strlen(str1);
		count = 0;
		pos = 0;
		
		for(loop1=0; loop1<length+1; loop1++)
		{
			if(str1[loop1]==char1)
				count++;
			else
			{
				str2[pos] = 48+count;
				str2[pos+1] = char1;
				char1 = str1[loop1];
				count = 1;
				pos += 2;
				
			}
			
		}
		str2[pos] = 0;
		strcpy(str1, str2);
		
	}
	
	return str1;
	
}

void main()
{
	int			loop;
	char*		str_ptr;
	int			end;
	
	//Main:
	for(loop=1; loop<12; loop++)
	{
		str_ptr = countAndSay(loop);
		
		printf("[%d][%s]\n",loop, str_ptr);
		
	}
	
	scanf("%d",&end);
	
	
}
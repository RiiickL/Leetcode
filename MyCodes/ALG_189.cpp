#pragma once
#include "leetcode_comm.h"

class Solution {
public:
    int size,steps;
    int start_val;
    
    void rotate(vector<int>& nums, int k) {
        //INIT:
        int count_times = 0;
        size = nums.size();
        steps = k % size;
        int start_pos = 0;
        start_val = nums[0];
        int return_pos = 0;
        int return_val;
        //LOOP:
        while (count_times < steps) {
            //play PING PANG:
            //get return position:
            do {
                return_pos = PingPangBack(nums, return_pos, return_val);
                start_val = nums[return_pos];
                nums[return_pos] = return_val;
                count_times++;
            } while (start_pos != return_pos);
            start_pos++;
            start_val = nums[start_pos];
            return_pos = start_pos;
        } 
    }

    int PingPangBack(vector<int>& nums, int pos, int& return_val) {
        int last_save = start_val;
        int temp_save;
        for (pos += steps; pos < size; pos += steps) {
            temp_save = nums[pos];
            nums[pos] = last_save;
            last_save = temp_save;
        }
        return_val = last_save;
        return pos - size;
    }

};
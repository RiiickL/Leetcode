#pragma once
#include "leetcode_comm.h"

class Solution {
public:
    string convertToTitle(int n) {
        string res = "";
        int mod_val;
        int div_val = n;
        char c_val;
        do {
            mod_val = (div_val - 1) % 26;
            div_val = (div_val - 1) / 26;
            //set RES according to mod_val;
            c_val = 'A' + mod_val;
            res = c_val + res;
            //loop when div_val not equls to 0;
        } while (div_val != 0);

        return res;
    }
};
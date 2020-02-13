#pragma once
#include "leetcode_comm.h"


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 0) {
            return 0;
        }
        vector<int>::iterator it = prices.begin();
        int profits = 0;
        int last_val = *it;
        it++;
        int gain;
        while (it != prices.end()) {
            gain = *it - last_val;
            last_val = *it;
            if (gain > 0) {
                profits += gain;
            }
            it++;
        }
        return profits;
    }
};
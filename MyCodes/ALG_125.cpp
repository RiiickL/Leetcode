#pragma once
#include "leetcode_comm.h"

class Solution {
public:
    bool isPalindrome(string s) {
        // 1. INIT:
        int h_ptr = s.size()-1;
        if (h_ptr <= 0) {
            return true;
        }
        int l_ptr = 0;

        // 2. LOOPs:
        int l_val = 0;
        int h_val = 0;
        do {
            //fint the valid l_ptr before h_ptr;
            for (l_ptr; l_ptr < h_ptr; l_ptr++) {
                l_val = ValidChange(s[l_ptr]);
                if (l_val>0) {
                    break;
                }
            }
            if (l_ptr == h_ptr) {
                return true;
            }
            for (h_ptr; h_ptr > l_ptr; h_ptr--) {
                h_val = ValidChange(s[h_ptr]);
                if (h_val>0) {
                    break;
                }
            }
            if (l_ptr == h_ptr) {
                return true;
            }
            else if (l_val != h_val) {
                return false;
            }
            //update:
            l_ptr++;
            h_ptr--;
        } while (l_ptr < h_ptr);
        return true;
    }

    int ValidChange(char input) {
        //lower case: 97 - 122;
        //upper case: 65 - 90;
        //0-9: 48 - 57;
        if (input <= 90) {
            if (input >= 65) {
                return int(input);
            }
            if (input > 47 && input < 58) {
                return int(input);
            }
        }
        if (input > 96 && input < 123) {
            return int(input) - 32;
        }
        return 0;
    }

};

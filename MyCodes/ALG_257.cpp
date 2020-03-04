#pragma once
#include "leetcode_comm.h"
#include <iostream>
#include <string>
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };
 
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> output_vec;
        if (root != NULL) {
            iterFunc(root, std::to_string(root->val), output_vec);
        }
        return output_vec;
    }

    void iterFunc(TreeNode* node, string input_str, vector<string>& insert_vec) {
        if (node->left != NULL) {
            iterFunc(node->left, input_str + "->" + std::to_string(node->left->val), insert_vec);
        }
        if (node->right != NULL) {
            iterFunc(node->right, input_str + "->" + std::to_string(node->right->val), insert_vec);
        }
        else if (node->left == NULL) {
            //insert it into insert_vec;
            insert_vec.push_back(input_str);
        }
    }

};
#pragma once
#include "leetcode_comm.h"

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
    
};

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (root == NULL) {
            return true;
        }
        return SymmCheck(root->left, root->right);
    }

    bool SymmCheck(TreeNode* left_tree, TreeNode* right_tree) {
        if (left_tree == NULL && right_tree == NULL) {
            return true;
        }

        if (left_tree == NULL || right_tree == NULL) {
            return false;
        }

        if (left_tree->val == right_tree->val) {
            if (SymmCheck(left_tree->left, right_tree->right) &&
                SymmCheck(left_tree->right, right_tree->left)){
                return true;
            }
            else {
                return false;
            }
        }
        else {
            return false;
        }
    }

};


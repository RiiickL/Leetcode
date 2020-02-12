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
        TreeNode* sortedArrayToBST(vector<int>& nums) {
            return createBST(nums, 0, nums.size() -1);
        }

        TreeNode* createBST(vector<int>& nums, int start, int end) {
            int size = end - start;
            if (size < 0) {
                return NULL;
            }
            if (size == 0) {
                return new TreeNode(nums[start]);
            }
            if (size == 1) {
                TreeNode* root = new TreeNode(nums[start]);
                root->right = new TreeNode(nums[end]);
                return root;
            }

            int mid = start + size / 2;
            TreeNode* root = new TreeNode(nums[mid]);

            root->left = createBST(nums, start, mid-1);
            root->right = createBST(nums, mid+1, end);
            return root;
        }

    };
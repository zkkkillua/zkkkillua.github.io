---
title: 530. 二叉搜索树的最小绝对差
date: 2020-10-12 15:05:44
categories: 
- leetcode
tags: 
- 树
---
## 1. 中序遍历
看到二叉搜索树优先考虑**“二叉搜索树的中序序列是递增的”**。  
获取中序序列后两两比较差值。  
时间`O(n)`，空间`O(n)`。  
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int getMinimumDifference(TreeNode* root) {
        vector<int> nums;
        stack<TreeNode*> st;

        while (root != nullptr || !st.empty()) {
            if (root == nullptr) {
                TreeNode* temp = st.top();
                st.pop();
                nums.push_back(temp->val);
                root = temp->right;
            } else {
                st.push(root);
                root = root->left;
            }
        }

        int ans = INT_MAX, n = nums.size();
        for (int i = 1; i < n; i++)
            ans = min(ans, nums[i] - nums[i - 1]);
        
        return ans;
    }
};
```
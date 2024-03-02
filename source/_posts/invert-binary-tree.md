---
title: 226.翻转二叉树
date: 2020-09-16 21:23:12
categories: 
- leetcode
tags: 
- 树
---

## 1. 递归
先交换左右子节点，然后再递归反转左右子树。  
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
    TreeNode* invertTree(TreeNode* root) {
        if (root != nullptr) {
            TreeNode* temp = root->left;
            root->left = root->right;
            root->right = temp;
            invertTree(root->left);
            invertTree(root->right);
        }
        
        return root;
    }
};
```
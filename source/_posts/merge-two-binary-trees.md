---
title: 617.合并二叉树
date: 2020-09-24 10:20:55
categories: 
- leetcode
tags:
---
## 1. 递归
合并两棵二叉树相当于新建一个值为两棵二叉树根节点值和的根节点，然后递归合并左子树和右子树。  
时间`O(m + n)`，空间`O(m + n)`。  
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
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (t1 == nullptr && t2 == nullptr)
            return nullptr;
        
        TreeNode* root = new TreeNode(0);
        if (t1 != nullptr)
            root->val += t1->val;
        if (t2 != nullptr)
            root->val += t2->val;
        
        root->left = mergeTrees(t1 == nullptr ? nullptr : t1->left, t2 == nullptr ? nullptr : t2->left);
        root->right = mergeTrees(t1 == nullptr ? nullptr : t1->right, t2 == nullptr ? nullptr : t2->right);

        return root;
    }
};
```
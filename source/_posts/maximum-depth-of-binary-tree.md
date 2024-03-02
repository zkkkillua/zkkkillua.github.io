---
title: 104.二叉树的最大深度
date: 2020-07-28 10:39:03
categories: leetcode
tags: 
- dp
---
## 1. 递归
时间`O(n)`，空间`O(height)`（递归栈）  
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
    int maxDepth(TreeNode* root) {
        if (root == nullptr)
            return 0;
        return max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
};
```

## 2. 迭代
类似层次遍历，时间`O(n)`，空间`O(n)`.  
```cpp
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr)
            return 0;
        int height = 0;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            height++;
            int n = q.size();
            for (int i = 0; i < n; i++) {
                TreeNode* temp = q.front();
                q.pop();
                if (temp->left != nullptr)
                    q.push(temp->left);
                if (temp->right != nullptr)
                    q.push(temp->right);
            }
        }

        return height;
    }
};
```
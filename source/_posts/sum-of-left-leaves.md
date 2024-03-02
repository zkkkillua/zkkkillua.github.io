---
title: 404.左叶子之和
date: 2020-09-19 16:35:49
categories: 
- leetcode
tags: 
- 树
---
## 1. 递归
递归求解左叶子的和，直接在最小的树（2层）中定位到左叶子，而不是递归到只剩一个节点，因为这样无法判断左右。  
时间`O(n)`，空间`O(n)`.  
```cpp
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        if (root == nullptr)
            return 0;
        else if (root->left != nullptr && root->left->left == nullptr && root->left->right == nullptr)
            return root->left->val + sumOfLeftLeaves(root->right);
        else
            return sumOfLeftLeaves(root->left) + sumOfLeftLeaves(root->right);
    }
};
```
  
## 2. 迭代
使用层次遍历，逐个判断是否为左叶子。  
时间`O(n)`，空间`O(n)`。  
```cpp
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        if (root == 0)
            return 0;

        int ans = 0;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode* cur = q.front();
            q.pop();
            if (cur->left != nullptr && cur->left->left == nullptr && cur->left->right == nullptr)
                ans += cur->left->val;
            else if (cur->left != nullptr)
                q.push(cur->left);
            if (cur->right != nullptr)
                q.push(cur->right);
        }

        return ans;
    }
};
```
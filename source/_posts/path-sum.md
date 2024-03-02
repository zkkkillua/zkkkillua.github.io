---
title: 112. 路径总和
date: 2020-09-27 16:45:59
categories: 
- leetcode
tags: 
- 树
---
## 1. 递归
递归访问子节点，同时修改目标值。  
需要注意的是空节点被看作空，而不是0，所以需要调整边界条件的判断。  
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
    bool hasPathSum(TreeNode* root, int sum) {
        if (root == nullptr)
            return false;
        if (root->left == nullptr && root->right == nullptr)
            return root->val == sum;

        return hasPathSum(root->left, sum - root->val) || hasPathSum(root->right, sum - root->val);
    }
};
```
  
## 2. 迭代
使用队列暂存节点和当前的目标值，不断访问队首元素，判断其是否为叶子节点以及将其子节点和对应目标值入队列。  
时间`O(n)`，空间`O(n)`。  
```cpp
class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if (root == nullptr)
            return false;

        bool flag = false;
        queue<pair<TreeNode*, int>> q;
        q.emplace(root, sum);
        while (!q.empty()) {
            TreeNode* cur = q.front().first;
            int curSum = q.front().second;
            q.pop();
            if (cur->left == nullptr && cur->right == nullptr && cur->val == curSum) {
                flag = true;
                break;
            }
            if (cur->left != nullptr)
                q.emplace(cur->left, curSum - cur->val);
            if (cur->right != nullptr)
                q.emplace(cur->right, curSum - cur->val);
        }

        return flag;
    }
};
```
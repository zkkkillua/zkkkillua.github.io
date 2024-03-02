---
title: 102.二叉树的层序遍历
date: 2020-05-13 11:47:18
categories: leetcode
tags: 
- 树
---
## 1. queue实现层次遍历
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*> q;
        vector<vector<int>> ans;

        if (root != nullptr)
            q.push(root);
        while (!q.empty()) {
            vector<int> sub;
            int qsz = q.size();
            while (qsz--) {
                TreeNode* temp = q.front();
                q.pop();
                sub.push_back(temp->val);
                if (temp->left != nullptr)
                    q.push(temp->left);
                if (temp->right != nullptr)
                    q.push(temp->right);
            }
            ans.push_back(sub);
        }

        return ans;
    }
};
```
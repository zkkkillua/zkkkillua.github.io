---
title: 94.二叉树的中序遍历
date: 2020-05-13 23:06:05
categories: leetcode
tags: 
- 树
---
## 相关
1. 二叉树的前序遍历：144
2. 二叉树的后序遍历：145

## 1. 递归
左根右直接递归实现。  
时间`O(n)`，空间`O(n)`.  
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
    vector<int> inorderTraversal(TreeNode* root) {
        if (root == nullptr)
            return {};
        vector<int> ans;
        vector<int> leftAns = inorderTraversal(root->left);
        vector<int> rightAns = inorderTraversal(root->right);
        ans.insert(ans.end(), leftAns.begin(), leftAns.end());
        ans.push_back(root->val);
        ans.insert(ans.end(), rightAns.begin(), rightAns.end());

        return ans;
    }
};
```
  
## 2. 迭代
中序遍历的访问顺序是左根右。  
想象一棵二叉树，实际的访问过程是一直左左左访问到最左，直到左子树为空才输出节点的值，然后去到右节点，继续左左左...  
所以可以直接模拟出上述过程，时间`O(n)`，空间`O(n)`.  
```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode*> st;
        vector<int> ans;

        while (!st.empty() || root != nullptr) {
            if (root == nullptr) {
                root = st.top();
                st.pop();
                ans.push_back(root->val);
                root = root->right;
            } else {
                st.push(root);
                root = root->left;
            }
        }

        return ans;
    }
};
```
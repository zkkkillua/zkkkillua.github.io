---
title: 106. 从中序与后序遍历序列构造二叉树
date: 2020-09-27 11:05:42
categories: 
- leetcode
tags: 
- 树
---
## 1. 递归
参照“105. 从前序与中序遍历序列构造二叉树”。  
中序遍历：左根右  
后序遍历：左右根  
  
从后序遍历结尾处获得当前的根节点，然后到中序遍历中查找根节点的位置，并以此划分中序和后序序列为左右子树两部分。  
同时使用hash表优化，避免每次都要遍历中序序列才能找到根节点，降低时间复杂度。  
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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int n = inorder.size();
        for (int i = 0; i < n; i++) 
            index[inorder[i]] = i;
        
        return buildTree(postorder, 0, n - 1, 0, n - 1);
    }
private:
    TreeNode* buildTree(vector<int>& postorder, int ibegin, int iend, int pbegin, int pend) {
        if (ibegin > iend)
            return nullptr;
        
        TreeNode* root = new TreeNode(postorder[pend]);
        int leftCount = index[postorder[pend]] - ibegin;
        root->left = buildTree(postorder, ibegin, ibegin + leftCount - 1, pbegin, pbegin + leftCount - 1);
        root->right = buildTree(postorder, ibegin + leftCount + 1, iend, pbegin + leftCount, pend - 1);

        return root;
    }
    unordered_map<int, int> index;
};
```
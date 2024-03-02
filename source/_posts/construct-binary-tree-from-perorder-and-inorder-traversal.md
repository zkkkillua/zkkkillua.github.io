---
title: 105. 从前序与中序遍历序列构造二叉树
date: 2020-09-27 10:52:49
categories: 
- leetcode
tags: 
- 树
---
## 1. 递归
前序遍历是根左右，因此前序序列的首个字符为根节点，之后一部分是左子树的节点，左子树部分的右侧一部分是右子树节点。  
中序遍历是左根右，因此中序遍历的开头一部分是左子树的节点，然后是根节点，之后剩下的右部分是右子树的节点。  
  
因此可以首先根据前序遍历的首个字符，确定根节点。  
然后在中序序列中找到根节点，其左侧的部分就是左子树的节点，右侧部分就是右子树的节点。  
根据中序序列中左右部分的长度，就可以在前序序列中划分出左右子树的部分。  
然后递归构造即可。  
时间`O(n^2)`，空间`O(n)`。  
  
因为每次都要遍历中序序列，找到当前的root，所以时间复杂度比较高。  
因此可以使用hash预先处理中序序列，之后每次就能用`O(1)`的方法查找到当前的root，时间复杂度降低到`O(n)`。  
`unordered_map<序列中的值, 该值对应在序列中的位置>`  
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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int n = preorder.size();
        for (int i = 0; i < n; i++)
            index[inorder[i]] = i;

        return buildTree(preorder, 0, n - 1, 0, n - 1);
    }
private:
    TreeNode* buildTree(vector<int>& preorder, int pstart, int pend, int istart, int iend) {
        if (pstart > pend)
            return nullptr;
        
        TreeNode* root = new TreeNode(preorder[pstart]);
        int leftCount = index[preorder[pstart]] - istart;
        root->left = buildTree(preorder, pstart + 1, pstart + leftCount, istart, istart + leftCount - 1);
        root->right = buildTree(preorder, pstart + leftCount + 1, pend, istart + leftCount + 1, iend);

        return root;
    }
    unordered_map<int, int> index;
};
```
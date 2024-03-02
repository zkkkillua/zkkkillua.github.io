---
title: 235.二叉搜索树的最近公共祖先
date: 2020-09-28 16:05:40
categories: 
- leetcode
tags: 
- 树
---
## 1. 普通二叉树的最近公共祖先
参照“[236.二叉树的最近公共祖先](https://zkkkillua.github.io/lowest-common-ancestor-of-a-binary-tree/)”，可以使用递归或迭代求解。  

递归求解是到左右子树中查找有无给定的p和q节点，根据不同的条件返回指针。  
迭代求解是使用hash表记录各节点的父节点，然后比较p和q的各祖先节点，可以是朴素比较/记录层数/记录是否访问。  

## 2. 迭代
如果p或q等于当前节点，返回当前节点。  
如果p和q都小于或者都大于当前节点，则到左子树或右子树中查找。  
如果p和q一个大于当前节点，一个小于当前节点，说明p和q在当前节点处分开，则当前节点一定是二者的最近公共祖先。  
相较于普通的二叉树，利用二叉搜索树的性质减少了对不必要的分支的访问。  
时间`O(n)`，空间`O(1)`。  
```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == nullptr)
            return nullptr;
        
        TreeNode* ans = nullptr;
        while (root != nullptr) {
            if (p->val < root->val && q->val < root->val) 
                root = root->left;
            else if (p->val > root->val && q->val > root->val)
                root = root->right;            
            else {
                ans = root;
                break;
            }
        }

        return ans;
    }
};
```
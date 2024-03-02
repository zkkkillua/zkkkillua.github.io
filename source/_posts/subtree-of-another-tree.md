---
title: 572.另一棵树的子树
date: 2020-05-08 00:04:53
categories: leetcode
tags:
---
## 相关题目：
**100. 相同的树**  

## 1. 递归
t是s的子树，则可能是：  
1. s的子树
2. s的左子树的子树
3. s的右子树的子树

而判断是否是子树的过程，就是判断当前s中为根的节点的子树与t树是否相同。  
时间复杂度：这里与“相同的树”遍历所有节点`O(n)`不同，此处最差需要看s的每一个节点对应的子树是否是与t相同的，所以需要`O(|s| * |t|)`.  
空间复杂度：递归栈最深是`O(n)`.  
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* s, TreeNode* t) {
        if (s == nullptr && t == nullptr)
            return true;
        if (s == nullptr || t == nullptr)
            return false;
        if (s->val != t->val)
            return false;
        return isSameTree(s->left, t->left) && isSameTree(s->right, t->right);
    }

    bool isSubtree(TreeNode* s, TreeNode* t) {
        if (s == nullptr && t == nullptr)
            return true;
        if (s == nullptr)
            return false;
        if (t == nullptr)
            return true;
        if (s->val != t->val)   // 如果s和t的根节点的值不等，则t只可能是s的左或右子树的子树
            return isSubtree(s->left, t) || isSubtree(s->right, t);
        else                    // 如果s和t的根节点的值相等，则t与s可能相同，而如果不同则只可能是s的左或右子树的子树
            return isSameTree(s, t) || isSubtree(s->left, t) || isSubtree(s->right, t);
    }
};
```
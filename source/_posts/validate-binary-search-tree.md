---
title: 98.验证二叉搜索树
date: 2020-05-05 17:59:58
categories: leetcode
tags: 
- 树
---
## 1. 中序遍历判断是否是递增序列
**中序遍历：左根右**  
可以用递归实现，也可以用栈模拟递归栈来迭代实现，这里用迭代实现。  
时间复杂度：遍历所有的节点，`O(n)`。  
空间复杂度：递归栈，深度最大`O(n)`。  
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
    bool isValidBST(TreeNode* root) {
        int pre = INT32_MIN;
        bool modified = false;
        stack<TreeNode*> st;

        while (root != nullptr || !st.empty()) {
            while (root != nullptr) {
                st.push(root);
                root = root->left;
            }
            root = st.top();
            st.pop();
            if (!modified) {
                pre = root->val;
                modified = true;
            } else {
                if (pre < root->val)
                    pre = root->val;
                else 
                    return false;
            }
            root = root->right;
        }

        return true;
    }
};
```
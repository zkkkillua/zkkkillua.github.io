---
title: 100.相同的树
date: 2020-05-07 17:54:32
categories: leetcode
tags: 
- 树
---
## 1. 递归
两棵树相同，则所有的节点的值和位置相同。  
可以通过递归比较根左右的想等情况。  
时间复杂度：遍历所有节点`O(n)`.  
空间复杂度：递归栈最深是`O(n)`.  
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == nullptr && q == nullptr)
            return true;
        if (p == nullptr || q == nullptr)
            return false;
        if (p->val != q->val)
            return false;
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

## 2. 迭代
相同的方法，不过用stack模拟递归栈来实现。  
时间复杂度和空间复杂度与上述递归方法相同。  
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        stack<pair<TreeNode*, TreeNode*> > st;
        st.push(make_pair(p, q));
        
        while (!st.empty()) {
            pair<TreeNode*, TreeNode*> temp = st.top();
            st.pop();
            p = temp.first;
            q = temp.second;
            if (p == nullptr && q == nullptr)
                continue;
            if (p == nullptr || q == nullptr)
                return false;
            if (p->val != q->val)
                return false;
            st.push(make_pair(p->left, q->left));
            st.push(make_pair(p->right, q->right));
        }

        return true;
    }
};
```
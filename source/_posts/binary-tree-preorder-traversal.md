---
title: 144.二叉树的前序遍历
date: 2020-07-21 23:43:33
categories: leetcode
tags: 
- 树
---
## 相关
1. 二叉树的中序遍历：94
2. 二叉树的后序遍历：145
3. N叉树的前序遍历：589
4. N叉树的后序遍历：590

## 1. 递归
根左右直接递归实现。  
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
    vector<int> preorderTraversal(TreeNode* root) {
        if (root == nullptr)
            return {};
        
        vector<int> ans;
        ans.push_back(root->val);
        vector<int> leftAns = preorderTraversal(root->left);
        vector<int> rightAns = preorderTraversal(root->right);
        ans.insert(ans.end(), leftAns.begin(), leftAns.end());
        ans.insert(ans.end(), rightAns.begin(), rightAns.end());

        return ans;
    }
};
```

## 2. 迭代
用stack模拟递归栈。  
访问栈顶元素（根） -> 右节点压栈 -> 左节点压栈 ->  
上述循环中，左节点入栈之后接着就出栈了，所以可以只将右节点入栈，下次直接访问左节点。  
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
    vector<int> preorderTraversal(TreeNode* root) {
        stack<TreeNode*> st;
        vector<int> ans;
        while (!st.empty() || root != nullptr) {
            if (root == nullptr) {
                root = st.top();
                st.pop();
            }
            ans.push_back(root->val);
            if (root->right != nullptr)
                st.push(root->right);
            root = root->left;
        }

        return ans;
    }
};
```
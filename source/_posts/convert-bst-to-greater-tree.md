---
title: 538.把二叉搜索树转换为累加树
date: 2020-09-21 09:49:35
categories: 
- leetcode
tags: 
- 树
---
## 1. 中序遍历
BST的中序遍历得到的结果是从小到大的有序序列，可以使用一个数组记录这个序列，然后遍历BST，对每个节点累加值。  
为了降低累加过程需要的时间，可以使用hash表统计大于各个值的节点值之和，从而避免每次都要重新求和。  
时间`O(n)`，空间`O(n)`。  
```cpp
class Solution {
public:
    TreeNode* convertBST(TreeNode* root) {
        if (root == nullptr)
            return root;

        vector<int> vals;
        midOrder(root, vals);
        unordered_map<int, int> sum;
        int temp = 0;
        for (int i = vals.size() - 1; i >= 0; i--) {
            temp += vals[i];
            sum[vals[i]] = temp;
        }

        queue<TreeNode*> q;
        q.push(root);
        TreeNode* cur;
        while (!q.empty()) {
            cur = q.front();
            q.pop();
            cur->val = sum[cur->val];
            if (cur->left != nullptr)
                q.push(cur->left);
            if (cur->right != nullptr)
                q.push(cur->right);
        }

        return root;
    }
private:
    void midOrder(TreeNode* root, vector<int>& vals) {
        stack<TreeNode*> st;
        while (root != nullptr || !st.empty()) {
            if (root == nullptr) {
                root = st.top();
                st.pop();
                vals.push_back(root->val);
                root = root->right;
            } else {
                st.push(root);
                root = root->left;
            }
        }
    }
};
```

## 2. 反向中序遍历
要修改一个节点需要获取比这个节点大的值，比它大的值在它的右子树中，同时还来自于它的各层父节点（如果它是父节点的左孩子的话）。  
如果按照这个思路求解每个节点的比它大的所有值是有些困难的，但是联想到中序遍历得到的有序序列就会比较简单。  
中序左根右遍历BST得到的是由小到大的有序序列，因此反向中序右根左遍历BST得到的是由大到小的有序序列。  
题目需要的比每个节点大的值正好由反向中序遍历提供了。  
时间`O(n)`，空间`O(n)`。  
```cpp
class Solution {
public:
    TreeNode* convertBST(TreeNode* root) {
        TreeNode* keepRoot = root;
        stack<TreeNode*> st;
        int sum = 0;
        while (root != nullptr || !st.empty()) {
            if (root == nullptr) {
                root = st.top();
                st.pop();
                sum += root->val;
                root->val = sum;
                root = root->left;
            } else {
                st.push(root);
                root = root->right;
            }
        }

        return keepRoot;
    }
};
```
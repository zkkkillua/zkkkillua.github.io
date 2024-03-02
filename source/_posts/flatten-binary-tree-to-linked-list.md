---
title: 114.二叉树展开为链表
date: 2020-08-02 18:02:50
categories: leetcode
tags: 
- 树
---
## 1. 前序遍历（递归）
查看题目和示例，发现展开之后的链表的顺序和二叉树的前序遍历的顺序是一致的。  
因此可以首先前序遍历获得顺序，然后逐个修改节点的左右子节点指向。  
时间`O(n)`，空间`O(n)`。  
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
    void flatten(TreeNode* root) {
        vector<TreeNode*> nodes;
        preorderTraversal(root, nodes);
        int n = nodes.size();
        for (int i = 0; i < n - 1; i++) {
            nodes[i]->left = nullptr;
            nodes[i]->right = nodes[i + 1];
        }
    }
private:
    void preorderTraversal(TreeNode* root, vector<TreeNode*>& nodes) {
        if (root != nullptr) {
            nodes.push_back(root);
            preorderTraversal(root->left, nodes);
            preorderTraversal(root->right, nodes);
        }
    }
};
```

## 2. 前序遍历（迭代）
上述方法的问题是需要首先通过前序遍历获得顺序之后，才能继续后面的链接操作。  
考虑是否可以在访问每个节点的过程中直接修改左右子节点的指向。  
借助一个栈保存当前节点的右子节点，调整pre指针和cur指针的位置实现遍历过程中直接修改。  
时间`O(n)`，空间`O(n)`。  
```cpp
class Solution {
public:
    void flatten(TreeNode* root) {
        stack<TreeNode*> s;
        TreeNode* pre = nullptr;
        TreeNode* cur = root;
        while (!s.empty() || cur != nullptr) {
            if (cur == nullptr) {
                cur = s.top();
                s.pop();
            }
            if (pre != nullptr) {
                pre->right = cur;
                pre->left = nullptr;
            }
            if (cur->right != nullptr)
                s.push(cur->right);
            pre = cur;
            cur = pre->left;
        }
    }
};
```

## 3. 根据题目定义和示例直接求解
整个过程实际是把root的展平的左子树移动到右子节点，再把root原来的展平的右子树接到左子树的最右下叶子节点。  
但直接用递归实现的话，由于递归栈，空间还是`O(n)`。  
```cpp
class Solution {
public:
    void flatten(TreeNode* root) {
        if (root == nullptr)
            return;
        flatten(root->left);
        flatten(root->right);
        TreeNode* pre = nullptr;
        TreeNode* cur = root->left;
        while (cur != nullptr) {
            pre = cur;
            cur = cur->right;
        }
        if (pre != nullptr)
            pre->right = root->right;
        if (root->left != nullptr)
            root->right = root->left;
        root->left = nullptr;
    }
};
```
因此可以继续详细化上述过程：把左子树移动到右子节点，原来的右子树接到左子树的最右下叶子节点。  
这样实现了空间`O(1)`的算法。  
```cpp
class Solution {
public:
    void flatten(TreeNode* root) {
        while (root != nullptr) {
            TreeNode* right = root->right;
            if (root->left != nullptr) {
                root->right = root->left;
                root->left = nullptr;
                TreeNode* pre = root->right;
                TreeNode* cur = root->right->right;
                while (cur != nullptr) {
                    pre = cur;
                    cur = cur->right;
                }
                pre->right = right;
            }
            root = root->right;
        }
    }
};
```
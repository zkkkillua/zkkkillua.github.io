---
title: 236. 二叉树的最近公共祖先
date: 2020-09-28 11:05:40
categories: 
- leetcode
tags: 
- 树
---
## 1. 递归
递归到以当前root为根的子树中查找是否包含p或q节点。  
因为包含与否分四种情况：都不包含，只含p，只含q，都包含。  
因此只用简单的true/false是不容易表示的，因此可以考虑返回指针，分别返回：null, &p, &q, root。  
时间`O(n)`，空间`O(n)`。  
```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == nullptr)
            return nullptr;
        
        if (root->val == p->val || root->val == q->val)
            return root;

        TreeNode* leftTree = lowestCommonAncestor(root->left, p, q);
        TreeNode* rightTree = lowestCommonAncestor(root->right, p, q);

        if (leftTree == nullptr)
            return rightTree;
        else if (rightTree == nullptr)
            return leftTree;
        else
            return root;
    }
};
```

## 2. 迭代
使用hash表记录每个节点的parent，然后分别找p和q节点的parent一直到整棵树的root，在此过程中查找最近公共祖先。  
这就相当于在两个数组中查找最接近开始位置的相等值的位置。  
- 一种方法是朴素查找，p每访问一层parent，q遍历所有层的parent，时间复杂度`O(n^2)`。  

- 第二种方法是hash表同时记录该parent的层数，然后p和q从parent的同一层出发公式向上找LCA。  

- 第三种方法是使用另一个hash表记录是否访问，p首先遍历各层的parent并标记为true，q在向上查找过程中访问到为true的节点即为公共祖先。  

时间`O(n)`，空间`O(n)`。  
```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == nullptr)
            return nullptr;

        unordered_map<int, TreeNode*> parent;
        unordered_map<int, bool> vis;
        queue<TreeNode*> que;

        parent[root->val] = nullptr;
        que.push(root);
        while (!que.empty()) {
            root = que.front();
            que.pop();
            if (root->left != nullptr) {
                que.push(root->left);
                parent[root->left->val] = root;
            }
            if (root->right != nullptr) {
                que.push(root->right);
                parent[root->right->val] = root;
            }
        }

        while (p != nullptr) {
            vis[p->val] = true;
            p = parent[p->val];
        }
        while (q != nullptr) {
            if (vis[q->val])
                break;
            q = parent[q->val];
        }

        return q;
    }
};
```
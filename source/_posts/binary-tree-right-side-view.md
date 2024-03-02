---
title: 199.二叉树的右视图
date: 2020-04-22 21:26:07
categories: leetcode
tags: 
- dfs
---
## 1. 层次遍历
层次遍历，只保留最右侧的那个值。  
时间复杂度`O(n)`，空间复杂度`O(n)`。  
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
    vector<int> rightSideView(TreeNode* root) {
        if (root == nullptr)
            return {};
        queue<TreeNode*> q;
        vector<int> ans;
        q.push(root);

        while (!q.empty()) {
            int n = q.size();
            for (int i = 0; i < n; i++) {
                TreeNode* temp = q.front();
                q.pop();
                if (temp->left != nullptr)
                    q.push(temp->left);
                if (temp->right != nullptr)
                    q.push(temp->right);
                if (i == n - 1)
                    ans.push_back(temp->val);
            }
        }

        return ans;
    }
};
```

## 2. DFS
按照“根右左”的顺序访问节点，则优先访问到的就是最右侧的节点。  
这种方法需要记录高度，当某个高度第一次被访问到的时候，储存遇到的第一个节点的值。  
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
    void dfs(vector<int>& ans, TreeNode* root, int height) {
        if (root == nullptr)
            return;
        if (ans.size() == height)
            ans.push_back(root->val);
        dfs(ans, root->right, height + 1);
        dfs(ans, root->left, height + 1);
    }

    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        dfs(ans, root, 0);

        return ans;
    }
};
```
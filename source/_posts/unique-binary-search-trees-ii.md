---
title: 95。不同的二叉搜索树II
date: 2020-07-22 10:09:47
categories: leetcode
tags: 
- dp
---
## 1. 回溯
最开始想到的是回溯，先通过回溯产生1~n的所有排列，然后把排列作为插入顺序，通过插入实现二叉搜索树。  
问题在于不同的序列对应的二叉树可能是相等的，比如2, 1, 3和2, 3, 1对应的是同一棵二叉树，会产生重复。  
暂时没有想到解决重复的方法。  

## 2. dp
参照[96. 不同的二叉搜索树]，题干相同，但96题仅要求返回种数，而不需要返回所有可能的树。  
96题的方法是dp，`g[i]`代表1~i产生的二叉搜索树的种数，则`g[n]`就是遍历i作为根节点，左子树是`g[i-1]`，右子树是`g[n-i]`，求乘积即可。  
参照96题，这道题也可以记录1~i产生的二叉搜索树，最终结果是遍历i作为根节点，左子树是1~i-1可能组成的二叉搜索树，右子树是i+1~n。  
左子树可以直接重用之前建好的节点，右子树可以复制1~n-i对应的二叉搜索树，然后整体加上一个偏移值。  
如果左子树是复用之前的节点，则速度要比递归快一些，因为左子树有重叠。  
```cpp
class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        if (n <= 0)
            return {};
        vector<vector<TreeNode*>> halfTrees(n + 1);    // halfTrees[i]代表1~i产生的二叉树
        halfTrees[0] = {nullptr};
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                vector<TreeNode*> leftChild = halfTrees[j - 1];
                vector<TreeNode*> rightChild = copyTrees(halfTrees[i - j], j);
                for (int ci = 0; ci < leftChild.size(); ci++) {
                    for (int cj = 0; cj < rightChild.size(); cj++) {
                        TreeNode* root = new TreeNode(j);
                        root->left = leftChild[ci];
                        root->right = rightChild[cj];
                        halfTrees[i].push_back(root);
                    }
                }
            }
        }

        return halfTrees[n];
    }
private:
    TreeNode* copyTree(TreeNode* root, int sum) {
        if (root == nullptr)
            return root;
        TreeNode* p = new TreeNode(root->val + sum, copyTree(root->left, sum), copyTree(root->right, sum));

        return p;
    }

    vector<TreeNode*> copyTrees(vector<TreeNode*> trees, int sum) {
        if (trees.size() == 1 && trees[0] == nullptr)
            return trees;
        vector<TreeNode*> ans;
        for (int i = 0; i < trees.size(); i++) 
            ans.push_back(copyTree(trees[i], sum));
        
        return ans;
    }
};
```

## 3. 递归
`gen(begin, end)`产生begin~end的二叉搜索树。  
可以遍历中间的i作为根节点，左子树是`gen(begin, i-1)`，右子树是`gen(i+1, end)`。  
```cpp
class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        if (n <= 0)
            return {};
        vector<TreeNode*> ans = generateTrees(1, n);
        return ans;
    }
private:
    vector<TreeNode*> generateTrees(int begin, int end) {
        if (begin > end)
            return {nullptr};
        
        vector<TreeNode*> ans;
        for (int i = begin; i <= end; i++) {
            vector<TreeNode*> leftChild = generateTrees(begin, i - 1);
            vector<TreeNode*> rightChild = generateTrees(i + 1, end);

            for (int j = 0; j < leftChild.size(); j++) {
                for (int k = 0; k < rightChild.size(); k++) {
                    TreeNode* root = new TreeNode(i);
                    root->left = leftChild[j];
                    root->right = rightChild[k];
                    ans.push_back(root);
                }
            }
        }

        return ans;
    }
};
```
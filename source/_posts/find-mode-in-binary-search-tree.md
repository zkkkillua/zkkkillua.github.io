---
title: 501.二叉搜索树中的众数
date: 2020-09-24 10:22:17
categories: 
- leetcode
tags:
---

## 1. 中序遍历+辅助数组
中序遍历获得有相同值的BST的非严格递增序列，存入辅助数组中，然后统计众数。  
时间`O(n)`，空间`O(n)`。  

## 2. 中序遍历
在中序遍历的过程中，可以直接记录和统计当前数据的出现次数，跟之前出现过的最大次数比较即可，不需要辅助数组。  
时间`O(n)`，空间`O(n)`。  
```cpp
class Solution {
public:
    vector<int> findMode(TreeNode* root) {
        if (root == nullptr)
            return {};
        vector<int> ans;
        stack<TreeNode*> st;
        int maxMode, maxCount = 0;
        int cur, curCount = 0;

        while (root != nullptr || !st.empty()) {
            if (root == nullptr) {
                root = st.top();
                st.pop();
                if (cur == root->val)
                    curCount++;
                else {
                    cur = root->val;
                    curCount = 1;
                }
                if (curCount == maxCount) 
                    ans.push_back(cur);
                else if (curCount > maxCount) {
                    maxCount = curCount;
                    if (maxMode != cur) {
                        maxMode = cur;
                        ans.clear();
                        ans.push_back(maxMode);
                    }
                }
                root = root->right;
            } else {
                st.push(root);
                root = root->left;
            }
        }

        return ans;
    }
};
```
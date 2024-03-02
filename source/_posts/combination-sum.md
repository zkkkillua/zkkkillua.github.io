---
title: 39. 组合总和
date: 2020-09-09 14:00:36
categories: leetcode
tags: 
- 回溯
---
## 前言
这道题目跟“377.组合总和iv”是一样的，都是无重复数组，可重复选择。  
区别是这道题返回的是全部的组合（数组），而377是仅返回组合数目。  
所以该题需要使用递归和回溯，在此过程中记录满足要求的组合到数组中；而由于递归过程中出现了许多重复计算，并且在377中仅要求组合的数目，不需要组合，因此377可以使用记忆化去掉重复计算，利用dp求解。  
  
## 1. 递归和回溯
类似77.组合，递归+回溯不断选择新的元素，判断满足target时记录。  
但时间复杂度可能超级高？  
空间复杂度最坏为`O(target)`。  
```cpp
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sum = 0;
        dfs(candidates, 0, target);

        return ans;
    }

private:
    void dfs(vector<int>& candidates, int begin, int target) {
        if (sum > target)
            return;
        else if (sum == target) {
            ans.push_back(subAns);
            return;
        }

        int n = candidates.size();
        for (int i = begin; i < n; i++) {
            subAns.push_back(candidates[i]);
            sum += candidates[i];
            dfs(candidates, i, target);
            subAns.pop_back();
            sum -= candidates[i];
        }
    }

    vector<vector<int>> ans;
    vector<int> subAns;
    int sum;
};
```
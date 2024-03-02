---
title: 216.组合总和III
date: 2020-09-11 11:06:24
categories: leetcode
tags: 
- 回溯
---
## 1. 递归+回溯
还是基本的递归回溯模板，只是将candidates数组改为了1~9的正整数，并且除了和为target之外还限制了数的个数。  
```cpp
class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        dfs(1, 9, k, n);

        return ans;
    }

private:
    void dfs(int begin, int end, int count, int sum) {
        if (sum == 0 && count == 0) {
            ans.push_back(subAns);
            return;
        } else if (count > 0 && sum > 0) {
            for (int i = begin; i <= end; i++) {
                subAns.push_back(i);
                dfs(i + 1, end, count - 1, sum - i);
                subAns.pop_back();
            }
        }
    }
    vector<int> subAns;
    vector<vector<int>> ans;
};
```
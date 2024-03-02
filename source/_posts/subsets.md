---
title: 78.子集
date: 2020-09-20 15:30:34
categories: 
- leetcode
tags: 
- 回溯
---
## 1. 递归+回溯
类似于求各种组合，选择->递归选择之后的元素->回溯。  
为了避免重复计算，在每次递归时将数组加入答案中即可，不需要每个数组都是从头开始计算。  
时间`O(n*2^n)`，空间`O(n)`递归栈。  
```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        dfs(nums, 0);

        return ans;
    }
private:
    void dfs(vector<int>& nums, int begin) {
        ans.push_back(subAns);

        int n = nums.size();
        for (int i = begin; i < n; i++) {
            subAns.push_back(nums[i]);
            dfs(nums, i + 1);
            subAns.pop_back();
        }
    }
    vector<int> subAns;
    vector<vector<int>> ans;
};
```

## 2. 迭代
首先记录空集，然后在此基础上每次向后追加新元素。  
如：`[] -> [], [1] -> [], [1], [2], [1,2] -> [], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]`  

```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        if (n == 0)
            return {};
            
        vector<int> subAns;
        vector<vector<int>> ans;

        ans.push_back(subAns);
        for (int i = 0; i < n; i++) {
            int curSize = ans.size();
            for (int j = 0; j < curSize; j++) {
                subAns = ans[j];
                subAns.push_back(nums[i]);
                ans.push_back(subAns);
            }
        }

        return ans;
    }
};
```
---
title: 416.分割等和子集
date: 2020-10-11 21:35:05
categories: 
- leetcode
tags: 
- 回溯
- 背包
---
## 1. 递归+回溯
第一反应是“40. 组合总和 II”，有重复数字，不能重复选择。  
首先求出数组总和，然后就变成了找是否存在目标为`sum/2`的组合问题。  
时间复杂度`O(2^n)`（每个元素选或不选），空间复杂度`O(1)`。  
*超时*  
  
“40. 组合总和 II”用dfs是因为它需要记录所有的方案，而这道题目只需要方案数，所以不需要在dfs过程中隐式包含的路径。  
```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int n = nums.size(), sum = 0;
        bool ans = false;
        for (int i = 0; i < n; i++) 
            sum += nums[i];
        
        if (sum % 2 == 0) {
            sort(nums.begin(), nums.end());
            ans = dfs(nums, 0, sum / 2);
        }

        return ans;
    }
private:
    bool dfs(vector<int>& nums, int beg, int target) {
        if (target < 0)
            return false;
        if (target == 0)
            return true;
        
        bool ans = false;
        for (int i = beg; i < nums.size(); ++i) {
            if (nums[i] > target)
                break;
            ans = dfs(nums, i + 1, target - nums[i]);
            if (ans)
                break;
        }

        return ans;
    }
};
```
  
## 2. 背包
01背包问题，需要恰好装满（到达sum/2)。  
时间`O(n*sum)`，空间`O(sum)`。  
```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int n = nums.size(), sum = 0;
        bool ans = false;
        for (int i = 0; i < n; i++)
            sum += nums[i];
        
        if (sum % 2 == 0) {
            int mid = sum / 2;
            vector<bool> dp(mid + 1, false);
            dp[0] = true;
            for (int i = 0; i < n; ++i) {
                for (int j = mid; j >= nums[i]; --j)
                    dp[j] = dp[j] || dp[j - nums[i]];
                if (dp[mid]) {
                    ans = true;
                    break;
                }
            }
        }

        return ans;
    }
};
```
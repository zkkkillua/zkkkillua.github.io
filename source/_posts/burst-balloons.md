---
title: 312.戳气球
date: 2020-07-23 21:56:32
categories: leetcode
tags: 
- dp
---
## 1. dp
因为不知道戳爆哪个气球得到的奖励最高，所以可以遍历i都戳戳试试。  
当戳爆第i个气球时，得到`nums[i - 1] * nums[i] * nums[i + 1]`的奖励，  
**同时把气球分为左右两部分**  

假设首先戳爆`i~j`的气球k，则非常不好计算：  
因为k被戳爆之后，左侧部分最后一个气球的戳爆依赖于右部分第一个气球，右侧部分第一个气球的戳爆依赖于左侧部分最后一个气球。  
所以可以假设最后戳爆气球k，这样左右两部分就不会产生关联。  

可以设`dp[i][j]`是戳爆`nums[i] ~ nums[j]`可得的最大收益。  
`dp[i][j] = max_k(dp[i][k - 1] + dp[k + 1][j] + nums[i - 1] * nums[k] * nums[j + 1])`  
时间`O(n^3)`，因为状态有`O(n^2)`种，每个状态的计算是`O(n)`。空间`O(n^2)`。  
```cpp
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        if (n == 0)
            return 0;
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                for (int k = i; k <= j; k++) {
                    dp[i][j] = max(dp[i][j], dpv(dp, i, k - 1) + dpv(dp, k + 1, j) + mult(nums, i, j, k));
                }
            }
        }

        return dp[0][n - 1];
    }
private:
    int dpv(const vector<vector<int>>& dp, const int& i, const int& j) {
        if (j < i)
            return 0;
        else
            return dp[i][j];
    }

    int mult(const vector<int>& nums, const int& i, const int& j, const int& k) {
        int a = i - 1 >= 0 ? nums[i - 1] : 1;
        int b = j + 1 < nums.size() ? nums[j + 1] : 1;
        return a * b * nums[k];
    }
};
```
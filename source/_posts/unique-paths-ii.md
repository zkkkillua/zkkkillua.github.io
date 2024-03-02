---
title: 63.不同路径II
date: 2020-07-23 16:32:49
categories: leetcode
tags: 
- dp
---
## 1. dp
类似[62. 不同路径]，只是在遇到障碍时清零dp即可。  
```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        vector<int> dp(n, 0);
        dp[0] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (obstacleGrid[i][j] == 1) {
                    dp[j] = 0;
                    continue;
                }
                if (j > 0) 
                    dp[j] += dp[j - 1];
            }
        }

        return dp[n - 1];
    }
};
```
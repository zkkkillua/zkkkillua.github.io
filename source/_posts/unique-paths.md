---
title: 62.不同路径
date: 2020-07-23 16:21:42
categories: leetcode
tags: 
- dp
---
## 1. dp
设`dp[i][j]`为从左上角到`(i, j)`位置的路径条数。  
`dp[i][j] = dp[i][j - 1] + dp[i - 1][j]`  
时间`O(mn)`，空间`O(mn)`但可以优化到`O(n)`。  
```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> dp(n, 1);
        for (int i = 1; i < m; i++) 
            for (int j = 1; j < n; j++)
                dp[j] += dp[j - 1];
        
        return dp[n - 1];
    }
};
```
---
title: 64. 最小路径和
date: 2020-07-23 16:12:05
categories: leetcode
tags: 
- dp
---
## 1. dp
最开始想的是bfs，但是没法实现，因为每次扩展出去的距离是不一样的。  
bfs可以解决的是每次位移距离都是1（这跟bfs的每次扩展过程是相同的），网格中有障碍的情况。  
可以使用dp来解决，`dp[i][j]`代表从左上角到达`grid[i][j]`需要的最小的路径和。  
`dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]`  
时间`O(mn)`，空间`O(mn)`但可以优化到`O(n)`。  
```cpp
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<int> dp(n);
        dp[0] = grid[0][0];

        for (int i = 0; i < m; i++) {
            if (i == 0) {
                for (int j = 1; j < n; j++)
                    dp[j] = dp[j - 1] + grid[i][j];
                continue;
            }
            for (int j = 0; j < n; j++) {
                if (j == 0)
                    dp[j] = dp[j] + grid[i][j];
                else
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j];
            }
        }

        return dp[n - 1];
    }
};
```
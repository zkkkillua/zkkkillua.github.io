---
title: 329.矩阵中的最长递增路径
date: 2020-07-27 17:13:38
categories: leetcode
tags: 
- dfs
- dp
---
## 1. dfs+记忆化搜索
其实就是dp的思想。  
`dp[i][j]`代表`nums[i][j]`开始，能够得到的最长递增路径的长度.  
则`dp[i][j]`依赖于上下左右四个位置中值比当前值大的位置。  

这样存在的问题是依赖位置的dp值不一定是已经求得的。  

一种方法是先从大到小排序，按这个顺序求解。  

另一种方法是递归求依赖但还未求解的位置的值。  
```cpp
class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        rows = matrix.size();
        if (rows == 0)
            return 0;
        cols = matrix[0].size();
        vector<vector<int>> dp(rows, vector<int>(cols, -1));
        int ans = 0;

        for (int i = 0; i < rows; i++) 
            for (int j = 0; j < cols; j++) 
                ans = max(ans, dfs(matrix, dp, i, j));

        return ans;
    }

private:
    int dfs(const vector<vector<int>>& matrix, vector<vector<int>>& dp, int x, int y) {
        if (x < 0 || x >= rows || y < 0 || y >= cols)
            return 0;
        if (dp[x][y] != -1)
            return dp[x][y];
        
        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k], ny = y + dy[k];
            if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && matrix[nx][ny] > matrix[x][y])
                dp[x][y] = max(dp[x][y], dfs(matrix, dp, nx, ny) + 1);
        }
        if (dp[x][y] == -1)
            dp[x][y] = 1;
        
        return dp[x][y];
    }

    int rows, cols;
    const int dx[4] = {-1, 1, 0, 0};
    const int dy[4] = {0, 0, -1, 1};
};
```
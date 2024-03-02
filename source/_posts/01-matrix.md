---
title: 542. 01矩阵
date: 2020-04-15 12:06:21
categories: leetcode
tags: 
- bfs
- dp
---
## 1. 超级源点+BFS
建一个超级源点0，BFS计算从0到1的距离。  
时间复杂度`O(mn)`，空间复杂度`O(mn)`。  
```cpp
class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> dis(m, vector<int>(n, 0));
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        queue<pair<int, int> > q;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    q.push(make_pair(i, j));
                    visited[i][j] = true;
                }
            }
        }

        int mi[4] = {-1, 1, 0, 0};
        int mj[4] = {0, 0, -1, 1};
        while (!q.empty()) {
            pair<int, int> loc = q.front();
            q.pop();
            for (int k = 0; k < 4; k++) {
                int i = loc.first + mi[k], j = loc.second + mj[k];
                if (i >= 0 && i < m && j >= 0 && j < n && !visited[i][j]) {
                    dis[i][j] = dis[loc.first][loc.second] + 1;
                    q.push(make_pair(i, j));
                    visited[i][j] = true;
                }
            }
        }

        return dis;
    }
};
```

## 2. dp
`dp[i][j]`代表`matrix[i][j]`到最近的0的距离。  
转移方程（仅针对1）为，遍历上下左右四个位置(ni, nj)：
dp[i][j] = min(dp[i][j], dp[ni][nj] + 1), 当matrix[ni][nj] == 1时；  
dp[i][j] = 1, 当matrix[ni][nj] == 0时。  

由于遍历的是上下左右四个位置，而dp[i][j]的计算是逐行逐列进行的，所以左、上的dp[ni][nj]已经计算得到了，而右、下的dp[ni][nj]还没有计算。  
可以选择更新两次，第一次只依赖左上部分元素转移，第二次只依赖右下部份元素转移。  

时间复杂度`O(mn)`，空间复杂度`O(mn)`。  
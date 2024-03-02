---
title: 200.岛屿数量
date: 2020-04-20 12:07:06
categories: leetcode
tags: 
- bfs
---
## 1. BFS
遍历与BFS。时间复杂度`O(mn)`，空间复杂度`O(mn)`(visited数组)。  
```cpp
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        if (m == 0)
            return 0;

        int n = grid[0].size();
        if (n == 0)
            return 0;
            
        vector<vector<bool> > visited(m, vector<bool>(n, false));
        int mvi[4] = {-1, 1, 0, 0};
        int mvj[4] = {0, 0, -1, 1};
        queue<pair<int, int> > q;
        int ans = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j] && grid[i][j] == '1') {
                    q.push(make_pair(i, j));
                    visited[i][j] = true;
                    while (!q.empty()) {
                        pair<int, int> loc = q.front();
                        q.pop();
                        int loci = loc.first, locj = loc.second;
                        for (int k = 0; k < 4; k++) {
                            int curi = loci + mvi[k], curj = locj + mvj[k];
                            if (curi >= 0 && curi < m && curj >= 0 && curj < n && grid[curi][curj] == '1' && !visited[curi][curj]) {
                                q.push(make_pair(curi, curj));
                                visited[curi][curj] = true;
                            }
                        }
                    }
                    ans++;
                }
            }
        }

        return ans;
    }
};
```
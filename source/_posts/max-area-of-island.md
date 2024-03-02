---
title: 695.Max Area of Island
date: 2020-03-15 16:47:02
categories: leetcode
tags: 
- bfs
---
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-area-of-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
_______________________________


## 框架
```cpp
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {

    }
};
```

## 1. bfs
遍历每个格子，对1的格子做bfs。最终遍历mn个格子，`O(mn)`。  
```cpp
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int res = 0;
        queue<pair<int, int> > q;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    int xmov[4] = {0, -1, 0, 1};
                    int ymov[4] = {-1, 0, 1, 0};
                    int tempMax = 1;
                    q.push(make_pair(i, j));
                    //push而非push_back，因为stack/queue/priority_queue都是容器适配器
                    //分别默认是由底层容器deque/deque/vector实现的。
                    grid[i][j] = 0;

                    while (!q.empty()) {
                        pair<int, int> qtop = q.front();    //front & back, 没有迭代器
                        q.pop();
                        int xtop = qtop.first, ytop = qtop.second;
                        
                        for (int imov = 0; imov < 4; imov++) {
                            int x = xtop + xmov[imov];
                            int y = ytop + ymov[imov];
                            if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == 1) {
                                tempMax++;
                                q.push(make_pair(x, y));
                                grid[x][y] = 0;
                            }
                        }
                    }
                    res = res >= tempMax ? res : tempMax;
                }
            }
        }

        return res;
    }
};
```

---
title: 994. Rotting Oranges
date: 2020-03-17 17:04:14
categories: leetcode
tags: 
- bfs
---
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotting-oranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
__________________________

## 框架
```cpp
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {

    }
};
```

## 1. 朴素
每次遍历grid，用queue储存2的位置，然后遍历queue，把2周围的1都变成2，而不能入队（新的烂橘子不具备传染能力）  
当两次遍历grid得到的剩余1的个数相等时表示结束。  
`O(mnk)`，m, n, k分别为grid的行、列、时间。  
```cpp
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size(), time = 0;
        int last = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == 1)
                    last++;
        int movi[4] = {0, -1, 0, 1};
        int movj[4] = {-1, 0, 1, 0};
        queue<pair<int, int> > q;

        while (true) {
            for (int i = 0; i < m; i++)
                for (int j = 0; j < n; j++)
                    if (grid[i][j] == 2)
                        q.push(make_pair(i, j));
            
            int cur = 0;
            while (!q.empty()) {
                pair<int, int> temp = q.front();
                q.pop();
                int loci = temp.first, locj = temp.second;
                for (int i = 0; i < 4; i++)
                    if (loci + movi[i] >= 0 && loci + movi[i] < m && locj + movj[i] >= 0 && locj + movj[i] < n && grid[loci + movi[i]][locj + movj[i]] == 1)
                        grid[loci + movi[i]][locj + movj[i]] = 2;
            }

            for (int i = 0; i < m; i++)
                for (int j = 0; j < n; j++)
                    if (grid[i][j] == 1)
                        cur++;
            if (cur != last) {
                time++;
                last = cur;
            } else
                break;
        }

        return last == 0 ? time : -1;
    }
};
```

## 2. BFS+超级原点
一个烂橘子传染一次之后其实就失效了，其他部分的传染不会跟它有关。  
所以每个橘子给一个时间属性，用BFS从最开始的烂橘子出发，找到所有相邻的橘子，时间每次++就代表腐烂时间。  
由于最开始有多个烂橘子，因此可以想象有一个超级原点，然后把这些初始的烂橘子都放到queue中。  
这样就相当于复杂度是`O(mn)`。  
```cpp
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int> > timeRecord(grid);
        int leftFresh = 0;
        queue<pair<int, int> > q;
        int maxTime = 0;
        int movi[4] = {0, -1, 0, 1};
        int movj[4] = {-1, 0, 1, 0};

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1)
                    leftFresh++;
                else if (grid[i][j] == 2)
                    q.push(make_pair(i, j));
                timeRecord[i][j] = 0;
            }

        while (!q.empty()) {
            pair<int, int> cur = q.front();
            q.pop();
            int curi = cur.first, curj = cur.second;
            
            for (int i = 0; i < 4; i++) {
                int aroundi = curi + movi[i], aroundj = curj + movj[i];
                if (aroundi >= 0 && aroundi < m && aroundj >= 0 && aroundj < n && grid[aroundi][aroundj] == 1) {
                    grid[aroundi][aroundj] = 2;
                    timeRecord[aroundi][aroundj] = timeRecord[curi][curj] + 1;
                    q.push(make_pair(aroundi, aroundj));
                    leftFresh--;
                    maxTime = timeRecord[aroundi][aroundj] > maxTime ? timeRecord[aroundi][aroundj] : maxTime;
                }
            }
        }

        return leftFresh == 0 ? maxTime : -1;
    }
};
```
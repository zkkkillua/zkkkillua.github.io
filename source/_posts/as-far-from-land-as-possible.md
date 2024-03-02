---
title: 1162. As Far from Land as Possible
date: 2020-03-29 15:47:08
categories: leetcode
tags: 
- bfs
---
## 框架
```cpp
class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {

    }
};
```

## 1. 朴素
统计每个0和1的位置，储存到vector中，对每个0直接求到所有1的曼哈顿距离的最小值。  
时间`O(n^2logn)`，空间`O(n)`.  
*超时了*  
```cpp
class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
        int n = grid.size();
        bool hasZero = false, hasOne = false;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (hasZero && hasOne)
                    break;
                if (grid[i][j] == 0 && !hasZero)
                    hasZero = true;
                if (grid[i][j] == 1 && !hasOne)
                    hasOne = true;
            }
        }
        if (!hasZero || !hasOne)
            return -1;

        vector<pair<int, int> > zeros;
        vector<pair<int, int> > ones;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0)
                    zeros.push_back(make_pair(i, j));
                else
                    ones.push_back(make_pair(i, j));
            }
        }

        int ans = 0;
        for (int i = 0; i < zeros.size(); i++) {
            int curAns = 2 * n;
            for (int j = 0; j < ones.size(); j++) {
                int dis = abs(zeros[i].first - ones[j].first) + abs(zeros[i].second - ones[j].second);
                curAns = curAns <= dis ? curAns : dis;
                if (curAns == 1)
                    break;
            }
            ans = ans >= curAns ? ans : curAns;
        }

        return ans;
    }
};
```

## 2. 超级源点+BFS
题目要求找每块海洋0到最近陆地1的距离最大，可以反过来找每块陆地1到所有海洋0的距离。  
通过超级源点可以把所有陆地都加到queue中，每次把每层的所有陆地1取出来向外扩展一圈。  
当海洋0被第一次访问时，得到的一定是该块海洋到最近陆地1的距离，之后的再次访问都不会对结果造成影响。  
可以新建一个grid记录每个海洋到最近陆地的距离，不过更省空间的方法是：每轮向外扩展是将该层的所有节点都向外扩展一次，这样只需要一个distance记录当前扩展的宽度就可以了。  
时间复杂度因为要访问到所有的节点，因此是`O(n^2)`，空间由于需要queue暂存节点，最坏也是`O(n^2)`。  
```cpp
class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
        int n = grid.size();
        queue<pair<int, int> > q;
        for (int i = 0; i < n; i++) 
            for (int j = 0; j < n; j++) 
                if (grid[i][j] == 1) 
                    q.push(make_pair(i, j));
                
        if (q.size() == 0 || q.size() == n * n)
            return -1;
        
        int distance = -1;
        int di[4] = {-1, 1, 0, 0};
        int dj[4] = {0, 0, -1, 1};
        while (!q.empty()) {
            distance++;
            int qsize = q.size();
            for (int k = 0; k < qsize; k++) {
                pair<int, int> cur = q.front();
                q.pop();
                for (int mv = 0; mv < 4; mv++) {
                    int i = cur.first + di[mv];
                    int j = cur.second + dj[mv];
                    if (i >= 0 && i < n && j >= 0 && j < n && grid[i][j] == 0) {
                        q.push(make_pair(i, j));
                        grid[i][j] = -1;
                    }
                }
            }
        }

        return distance;
    }
};
```
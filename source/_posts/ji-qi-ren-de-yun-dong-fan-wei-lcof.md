---
title: 面试题13. 机器人的运动范围
date: 2020-04-08 12:17:07
categories: leetcode
tags: 
- BFS
---
## 框架
```cpp
class Solution {
public:
    int movingCount(int m, int n, int k) {

    }
};
```

## 1. BFS
BFS到相邻节点，判断要求是否超过k。  
时间`O(mn)`，空间由于需要一个网格记录是否访问过，也是`O(mn)`.  
```cpp
class Solution {
public:
    int movingCount(int m, int n, int k) {
        int id[2] = {0, 1};
        int jd[2] = {1, 0};
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        queue<pair<int, int>> q;
        q.push(make_pair(0, 0));
        visited[0][0] = true;
        int ans = 1;

        while (!q.empty()) {
            pair<int, int> cur = q.front();
            q.pop();
            int i = cur.first, j = cur.second;
            for (int mv = 0; mv < 2; mv++) {
                if (i + id[mv] < m && j + jd[mv] < n && !visited[i + id[mv]][j + jd[mv]]) {
                    int sum = 0;
                    int loci = i + id[mv], locj = j + jd[mv];
                    while (loci > 0) {
                        sum += loci % 10;
                        loci /= 10;
                    }
                    while (locj > 0) {
                        sum += locj % 10;
                        locj /= 10;
                    }
                    if (sum <= k) {
                        q.push(make_pair(i + id[mv], j + jd[mv]));
                        ans++;
                    }
                    visited[i + id[mv]][j + jd[mv]] = true;
                }
            }
        }

        return ans;
    }
};
```
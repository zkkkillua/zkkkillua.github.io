---
title: 892.Surface Area of 3D Shapes
date: 2020-03-25 11:14:24
categories: leetcode
tags:
---
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

 

Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46


Note:

1 <= N <= 50
0 <= grid[i][j] <= 50

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surface-area-of-3d-shapes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
_____________________________________

## 框架
```cpp
class Solution {
public:
    int surfaceArea(vector<vector<int>>& grid) {

    }
};
```

## 1. 遍历前后左右四个位置
```cpp
class Solution {
public:
    int surfaceArea(vector<vector<int>>& grid) {
        int n = grid.size();
        int movi[4] = {-1, 1, 0, 0};
        int movj[4] = {0, 0, -1, 1};
        int ans = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0)
                    continue;
                
                ans += 2;
                for (int k = 0; k < 4; k++) {
                    int curi = i + movi[k];
                    int curj = j + movj[k];
                    if (curi < 0 || curi >= n || curj < 0 || curj >= n)
                        ans += grid[i][j];
                    else {
                        if (grid[i][j] > grid[curi][curj])
                            ans += grid[i][j] - grid[curi][curj];
                    }
                }
            }
        }

        return ans;
    }
};
```
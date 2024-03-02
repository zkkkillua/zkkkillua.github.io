---
title: 836.Rectangle Overlap
date: 2020-03-18 11:27:16
categories: leetcode
tags:
---
A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Notes:

Both rectangles rec1 and rec2 are lists of 4 integers.
All coordinates in rectangles will be between -10^9 and 10^9.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rectangle-overlap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

---

## 框架

```cpp
class Solution {
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {

    }
};
```

## 1. 画图分析

两个矩形相交得到的小矩形的：
左边界是二者左边界中最大的，
右边界是二者右边界中最小的，
下边界是二者下边界中最大的，
上边界是二者上边界中最小的。

```cpp
class Solution {
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        if (max(rec1[0], rec2[0]) < min(rec1[2], rec2[2]) && max(rec1[1], rec2[1]) < min(rec1[3], rec2[3]))
            return true;
        else
            return false;
    }
};
```

## 2. 投影取反

这个是看题解知道的，妙啊。
把两个矩形投影到x, y轴，如果相交，那么它们在x, y轴的投影都是重叠的，就变成了判断线段是否重叠的问题。
不过实际上，重叠的情况很多，不重叠的更好判断，所以判断不重叠然后取反就可以了。
![projection](rectangle-overlap/projection.jpg)

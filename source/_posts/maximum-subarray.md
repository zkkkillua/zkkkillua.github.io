---
title: 53. 最大子序和
date: 2020-05-03 22:39:05
categories: leetcode
tags: 
- 滑动窗口
---
```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
    }
};
```

## 1. 滑动窗口
当窗口内的值为正时，右边界一直向右移动（因为左侧总是可以作为正数部分）  
当窗口内的值为负时，左边界跳过右边界（因为左侧已经是负数了）  
时间`O(n)`，空间`O(1)`。  
```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        if (n == 0)
            return 0;

        int loc = 0, ans = nums[0], cur = 0;
        while (loc < n) {
            if (cur >= 0) {
                cur += nums[loc++];
                ans = ans >= cur ? ans : cur;
            }
            else
                cur = 0;
        }

        return ans;
    }
};
```

## 2. 分治
https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/  
很奇妙。  
维护了区间的：整个区间的和、以左端点为起点的最大子段和、以右端点为终点的最大子段和、整个区间最优的最大子段和。  
这样，在分治合并的时候，求一个区间的上述四种属性可以这样求：  
1. 整个区间的和：左右子区间的整个区间的和之和。
2. 以左端点为起点的最大子段和：可能只是左子区间的以左端点为起点的最大字段和，也有可能是整个左子区间+右子区间以左端点为起点的部分和。  
3. 以右端点为终点的最大子段和：跟2正好相对。  
4. 整个区间的最大子段和：可能是左或右子区间的最大子段和，也可能是跨越左右子区间的（左子区间中以右端点为终点的部分+右子区间中以左端点为起点的部分）  

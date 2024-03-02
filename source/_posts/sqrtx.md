---
title: 69.x的平方根
date: 2020-05-09 22:57:03
categories: leetcode
tags: 
- 二分
---
## 1. 二分
时间复杂度：`O(logn)`，空间复杂度`O(1)`。  
```cpp
class Solution {
public:
    int mySqrt(int x) {
        if (x < 0)
            return -1;

        int left = 0, right = x;
        int ans = 0;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            long long midv = (long long)mid * mid;
            if (midv == x) {
                ans = mid;
                break;
            } else if (midv < x) {
                ans = mid;
                left = mid + 1;
            } else 
                right = mid - 1;
        }

        return ans;
    }
};
```

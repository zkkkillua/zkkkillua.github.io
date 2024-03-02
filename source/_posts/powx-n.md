---
title: 50.Pow(x,n)
date: 2020-05-11 23:57:52
categories: leetcode
tags:
---
## 1. 快速幂
时间`O(logn)`，空间`O(1)`。  
```cpp
class Solution {
public:
    double myPow(double x, int n) {
        long long N = n;
        bool isNegative = x < 0 && N % 2 == 1;
        if (isNegative)
            x = -x;
        if (N < 0) {
            // n = -n;     // n == INT32_MIN时不能直接取负，会溢出
            N = -N;
            x = 1 / x;
        }
        double ans = 1;
        while (N > 0) {
            if (N & 1)
                ans *= x;
            x *= x;
            N >>= 1;
        }

        if (isNegative)
            ans = -ans;
        return ans;
    }
};
```
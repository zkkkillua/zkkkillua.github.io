---
title: 977.有序数组的平方
date: 2020-10-16 17:39:59
categories: 
- leetcode
tags:
---
## 1. 双指针
首先找到正数和负数的分界点，然后二者根据各自指向的值的平方大小向左向右移动。  
时间`O(n)`，空间`O(1)`。  
```cpp
class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        int n = A.size();
        vector<int> res(n);
        int neg, pos, sep, count = 0;

        for (sep = 0; sep < n; ++sep)
            if (A[sep] >= 0)
                break;
        neg = sep - 1;
        pos = sep;
        while (count < n) {
            int val;
            if (neg >= 0 && pos < n) {
                if (-A[neg] <= A[pos]) 
                    val = A[neg--];
                else
                    val = A[pos++];
            } else if (neg >= 0)
                val = A[neg--];
            else 
                val = A[pos++];
            res[count++] = val * val;
        }

        return res;
    }
};
```
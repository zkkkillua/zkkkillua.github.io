---
title: 852.山脉数组的峰顶索引
date: 2020-07-18 22:56:24
categories: leetcode
tags: 
- 二分
---
## 1. 朴素
直接`O(n)`扫描一遍，记录最大值索引。  
```cpp
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        int n = A.size();
        int ans = 0;
        for (int i = 0; i < n; i++)
            if (A[i] > A[ans])
                ans = i;
        
        return ans;
    }
};
```

## 2. 二分
二分根据mid判断是递增一侧还是递减一侧，复杂度`O(logn)`。  
```cpp
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        int l = 0, r = A.size() - 1;
        int ans = 0;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (mid == 0) {
                ans = A[ans] > A[r] ? ans : r;
                break;
            }
            ans = A[ans] > A[mid] ? ans : mid;
            if (A[mid] > A[mid - 1] && A[mid] > A[mid + 1])
                break;
            else if (A[mid] >= A[mid - 1])
                l = mid + 1;
            else if (A[mid] <= A[mid - 1])
                r = mid - 1;
        }

        return ans;
    }
};
```
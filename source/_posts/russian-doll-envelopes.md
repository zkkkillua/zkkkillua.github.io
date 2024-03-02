---
title: 354. 俄罗斯套娃信封问题
date: 2021-03-04 19:38:11
categories: 
- leetcode
tags: 
- dp
- 二分
---
**参考[最长递增子序列](https://zkkkillua.github.io/longest-increasing-subsequence/)**  


## 1. dp
首先将信封从小到大排列，之后设置动态规划数组，`dp[i]`代表以`envelopes[i]`为结尾的信封序列最长的长度。  
则每次`dp[i]`都由左侧比它小的信封中最长的长度+1得到。  
时间`O(n^2)`，空间`O(n)`。  
```cpp
class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        int n = envelopes.size();
        if (n == 0)
            return 0;
        sort(envelopes.begin(), envelopes.end());

        vector<int> lens(n, 1);
        int maxLength = 1;
        for (int i = 1; i < n; i++) {
            int maxBefore = 0;
            for (int j = i; j >= 0; j--) {
                if (envelopes[j][0] < envelopes[i][0] && envelopes[j][1] < envelopes[i][1] && lens[j] > maxBefore) {
                    maxBefore = lens[j];
                    if (lens[j] == maxLength)
                        break;
                }
            }
            lens[i] += maxBefore;
            maxLength = max(maxLength, lens[i]);
        }

        return maxLength;
    }
};
```

## 2. dp+二分
将信封按照第一维递增，第一维相等时第二维递减排序，可以转换为只考虑第二维。  
因为第一维必是递增的，第一维相等时由于第二维递减，故不会在递增过程中重复取第一维相同的元素。  

考虑修改方法1中`dp[i]`的定义为长度为`i`的递增子序列的最小的结尾元素。  
假设当前长度为`len`，则当遇到比`dp[len]`更大的元素时，`dp[++len] = val`；当遇到更小的元素时，则到其左侧找到第一个比`val`大的`dp[i]`，修改为`val`，代表长度为`i`的递增子序列如今可以有更小的结尾元素了，从而可以使得之后更长的递增序列也可能跟在`val`之后，用更小的值实现相同的递增长度。  
查找第一个比`val`大的`dp[i]`可以使用二分，因为根据定义，`dp`数组必是单调递增的，同时也代表了`dp[i-1]`的序列加上`val`之后可以得到`dp[i]`的序列。  
时间`O(nlogn)`，空间`O(n)`。  
```cpp
class Solution {
public:
    static bool cmp(vector<int>& a, vector<int>& b) {
        bool res = a[0] < b[0];
        if (a[0] == b[0])
            res = a[1] > b[1];
        return res;
    }

    int maxEnvelopes(vector<vector<int>>& envelopes) {
        int n = envelopes.size();
        if (n == 0)
            return 0;
        
        sort(envelopes.begin(), envelopes.end(), cmp);

        vector<int> tail(n + 1);
        int maxLength = 0;
        for (int i = 0; i < n; i++) {
            if (maxLength == 0 || envelopes[i][1] > tail[maxLength])
                tail[++maxLength] = envelopes[i][1];
            else {
                int left = 1, right = maxLength, mid = (right - left) / 2 + left;
                while (left < right) {
                    if (tail[mid] >= envelopes[i][1])
                        right = mid;
                    else
                        left = mid + 1;
                    mid = (right - left) / 2 + left;
                }
                tail[mid] = envelopes[i][1];
            }
        }

        return maxLength;
    }
};
```
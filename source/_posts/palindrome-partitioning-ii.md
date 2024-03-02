---
title: 132. 分割回文串 II
date: 2021-03-08 10:32:24
categories: 
- leetcode
tags: 
- dp
---
## 1. dp
设`dp[i]`是以`s[i]`为结尾的子串的最少分割次数，则  
`dp[i] = min(dp[j-1]+1)`，`j`是`i`左侧的位置，`s[j~i]`是`s[0~i]`最后一个回文串。  
从后遍历所有的回文串，找到分割最短的。  
使用预处理之后，以`O(1)`的时间判断`s[i][j]`的回文性。  
时间`O(n^2)`，空间`O(n^2)`。  
```cpp
class Solution {
public:
    int minCut(string s) {
        int n = s.length();
        vector<vector<bool>> palindromic(n, vector<bool>(n));
        vector<int> dp(n, INT_MAX);

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (j - i < 2)
                    palindromic[i][j] = s[i] == s[j];
                else
                    palindromic[i][j] = palindromic[i + 1][j - 1] && s[i] == s[j];
            }
        }

        for (int i = 0; i < n; i++) {
            if (palindromic[0][i]) {
                dp[i] = 0;
                continue;
            }
            for (int j = i; j > 0; j--) {
                if (palindromic[j][i])
                    dp[i] = min(dp[i], dp[j - 1] + 1);
            }
        }

        return dp[n - 1];
    }
};
```
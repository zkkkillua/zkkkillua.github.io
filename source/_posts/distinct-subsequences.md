---
title: 115. 不同的子序列
date: 2021-03-17 15:47:53
categories: 
- leetcode
tags: 
- dp
---
## 1. dp
设`dp[i][j]`代表s的前i个字符和t的前j个字符满足题目的匹配要求的个数，则  
`dp[i][j] = dp[i-1][j-1] + dp[i-1][j]`，当`s[i-1] == t[j-1]`时；  
`dp[i][j] = dp[i-1][j]`，当`s[i-1] != t[j-1]`时。  
原因是要满足题目要求，t的字符必须全部匹配，故t[0~j-1]必选。  
对于s[i-1]，如果可匹配则可选可不选；如果不匹配，则不选。  
初始化dp[i][0] = 1, dp[0][j>0] = 0.  
时间`O(mn)`，空间`O(mn)`。  
```cpp
class Solution {
public:
    int numDistinct(string s, string t) {
        int ns = s.length(), nt = t.length();
        if (ns < nt)
            return 0;
        
        vector<vector<long long>> dp(ns + 1, vector<long long>(nt + 1, 0));
        for (int i = 0; i <= ns; i++)
            dp[i][0] = 1;
        
        for (int i = 1; i <= ns; i++) {
            for (int j = 1; j <= i && j <= nt; j++) {     // j可以超过i就停止，因为s短则比不可能匹配t
                if (s[i - 1] == t[j - 1])
                    dp[i][j] = dp[i - 1][j - 1];
                dp[i][j] += dp[i - 1][j];
            }
        }

        return dp[ns][nt];
    }
};
```
  
## 2. 优化空间
方法1中更新dp[i][j]只用到了dp[i-1][j-1]和dp[i-1][j]，因此可以在空间上进行优化。  
空间上只保留一行，同时j逆序更新。  
时间`O(mn)`，空间`O(n)`。  
```cpp
class Solution {
public:
    int numDistinct(string s, string t) {
        int ns = s.length(), nt = t.length();
        if (ns < nt)
            return 0;
        
        vector<long long> dp(nt + 1, 0);
        dp[0] = 1;
        
        for (int i = 1; i <= ns; i++) {
            for (int j = nt; j >= 1; j--) {
                if (s[i - 1] == t[j - 1])
                    dp[j] += dp[j - 1];
            }
        }

        return dp[nt];
    }
};
```
---
title: 72.Edit Distance
date: 2020-04-06 17:45:41
categories: leetcode
tags: 
- dp
---
## 框架
```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        
    }
};
```

## 1. dp
~~设`dp[i][j]`代表`word1[0~i]与word2[0~j]`部分需要的最少的操作数。~~  
设`dp[i][j]`代表`word1`的前i个字符和`word2`的前j个字符部分需要的最少操作数。（这样要简单得多）  
状态转移方程为：  
`dp[i][j] = dp[i - 1][j - 1]`, 当`word1[i - 1] == word2[j - 1]`时。  
`dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1`, 当`word1[i - 1] != word2[j - 1]`时。  
上述情况需要由三种状态转移而来，分别是：修改，删除word1[i-1]，添加word2[j-1]。  
```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        int n1 = word1.length(), n2 = word2.length();
        if (n1 == 0 || n2 == 0)
            return n1 + n2;

        int **dp = new int*[n1 + 1];
        for (int i = 0; i < n1 + 1; i++)
            dp[i] = new int[n2 + 1]{0};
        
        for (int i = 0; i <= n1; i++)
            dp[i][0] = i;
        for (int i = 0; i <= n2; i++)
            dp[0][i] = i;
        
        for (int i = 1; i <= n1; i++) {
            for (int j = 1; j <= n2; j++) {
                if (word1[i - 1] == word2[j - 1])
                    dp[i][j] = dp[i - 1][j - 1];
                else {
                    int temp = min(dp[i - 1][j], dp[i][j - 1]);
                    dp[i][j] = min(temp, dp[i - 1][j - 1]) + 1;
                }
            }
        }

        int ans = dp[n1][n2];
        for (int i = 0; i < n1 + 1; i++)
            delete []dp[i];
        delete []dp;
        return ans;
    }
};
```
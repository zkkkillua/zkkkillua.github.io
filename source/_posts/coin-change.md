---
title: 322. 零钱兑换
date: 2020-04-09 15:13:42
categories: 
- leetcode
tags: 
- dp
- 背包
---
## 框架
```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {

    }
};
```

## 1. 完全背包
背包容量：`amount`  
物品价值：`coins`  
物品体积：`coins`  
恰好达到价值`amount`  
`dp[i][j]`原本记录前i种物品装入容量为j的背包能达到的最大价值。但是此处由于容量就代表了价值，所以`dp[i][j]`此处可以记录前i种金额装入容量为j的背包（达到j的价值）需要的最少的钱的张数。  
```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int maxVal = 0x3f3f3f3f;
        int n = coins.size();
        vector<int> dp(amount + 1, maxVal);
        dp[0] = 0;

        for (int i = 0; i < n; i++) {
            for (int j = coins[i]; j <= amount; j++) {
                dp[j] = min(dp[j], dp[j - coins[i]] + 1);
            }
        }

        if (dp[amount] >= maxVal)
            return -1;
        else
            return dp[amount];
    }
};
```

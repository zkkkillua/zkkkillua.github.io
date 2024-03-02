---
title: 983.最低票价
date: 2020-05-07 16:54:45
categories: leetcode
tags: 
- dp
---
## 1. 动态规划（从前往后）
`dp[i]`代表从开始到第`days[i]`天(包括这一天)花费的钱。  

如果求解`dp[i]`是遍历到i时再去看前1天、前7天和前30天花的钱+再买票的钱是没法计算的，因为前面的那些天已经买票了，即30天前的那一天可能已经花钱买了30天的票，如果再+票钱的话，就多余了。  
所以就需要在`dp[i]`这天买票的时候，就将之后的在票范围内的`dp[j]`更新掉。  

遍历到每一天`days[i]`，我们都假设这一天没有旅游，需要买票（加上上次旅游花的钱即`dp[i-1]`），并把买票之后可以访问到的`dp[j]`更新。  
这样就可以得到每一个`days[j]`之前的天数花费一定的票费到达`days[j]`这一天。

如果是访问到`days[i]`这天发现已经通过之前的票旅游过了，那么这就是从开始到`days[i]`天花费的最少的钱。  
而如果访问到`days[i]`这天，发现之前旅游买票还没有能长到这天的（即`dp[i] == INT32_MAX`时），就根据旅游到前一次花费的最少的钱`dp[i-1]`来更新`dp[i]`。  

时间复杂度：因为要算后面最多30天的dp，所以`O(30*n) = O(n)`.  
空间复杂度：`O(n)`.  
```cpp
class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int n = days.size();
        if (n == 0)
            return 0;
        
        vector<int> dp(n, INT32_MAX);
        int duration[3] = {1, 7, 30};
        for (int i = 0; i < n; i++) {
            int last = i == 0 ? 0 : dp[i - 1];
            dp[i] = min(dp[i], last + min({costs[0], costs[1], costs[2]}));
            for (int k = 1; k < 3; k++) {
                for (int j = i + 1; j < n && days[j] - days[i] < duration[k]; j++)
                    dp[j] = min(dp[j], last + costs[k]);
            }
        }

        return dp[n - 1];
    }
};
```

## 2. 动态规划（从后往前）
`dp[i]`代表从第`days[i]`天到最后一天旅游需要花的最少的费用。  

在`days[i]`天：  
1. 可能买1天的票到达`days[i+1]`天
2. 可能买7天的票到达`days[j7]`天
3. 可能买30天的票到达`days[j30]`天
`days[j7], days[j30]`分别代表在`days[i]`天买7, 30天的票可以到达的最远的一天。  
因为`days[i] >= days[i+1]`必成立，所以可以贪心一下找到最后一天。  
`dp[i] = min(dp[i + 1] + costs[0/1/2], dp[j7] + costs[2], dp[j30] + costs[3])`  

时间复杂度：因为要算后面最多30天的dp，所以`O(30*n) = O(n)`.  
空间复杂度：`O(n)`.  
```cpp
class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int n = days.size();
        if (n == 0)
            return 0;

        vector<int> dp(n, INT32_MAX);
        int duration[3] = {1, 7, 30};
        for (int i = n - 1; i >= 0; i--) {
            int next = i == n - 1 ? 0 : dp[i + 1];
            dp[i] = next + min({costs[0], costs[1], costs[2]});
            for (int k = 1; k < 3; k++) 
                for (int j = i + 1; j < n && days[j] - days[i] < duration[k]; j++)
                    dp[i] = min(dp[i], dp[j] + costs[k]);
        }
    }
};
```

## 3. 总结
正序遍历和逆序遍历的代码几乎是完全一样的，但是思想上却有很大的差距。  
正序遍历是根据之前的买上票之后把之后可以到达的更新掉，  
逆序遍历是根据之后花的最少的钱加上这一天花的可以到达之后那一天的票钱。  

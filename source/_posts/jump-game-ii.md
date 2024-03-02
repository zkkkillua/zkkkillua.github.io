---
title: 45.跳跃游戏II
date: 2020-05-04 11:46:24
categories: leetcode
tags: 
- dp
---
## 1. 朴素dp
`dp[i]`记录从开始到`nums[i]`节点需要的最少的跳数，则状态转移方程：  
`dp[i] = min(dp[j] + 1), if (j < i && j + nums[j] >= i)`  
时间`O(n^2)`，空间`O(n)`。  
*超时。*  
```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        if (n < 2)
            return 0;
        
        int* dp = new int[n];
        for (int i = 1; i < n; i++)
            dp[i] = INT32_MAX;
        dp[0] = 0;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (j + nums[j] >= i)
                    dp[i] = dp[i] <= dp[j] + 1 ? dp[i] : dp[j] + 1;
            }
        }

        int ans = dp[n - 1];
        delete []dp;
        return ans;
    }
};
```

## 2. 优化方法1的记录方式
可以在访问到i节点的时候，将其可以访问到的右侧的节点的`dp[j]`更新。  
而由于定义的`dp[i]`数组一定是随着i的增加而增大的，所以之后的`dp[j]`只需要更新第一次即可。  
由于只需要更新一次dp数组，所以时间复杂度是`O(n)`，空间复杂度也是`O(n)`.  

还可以想到，i节点更新完它可以访问到的j节点的`dp[j]`时，`dp[i]`的作用就完成了，后续不会再使用。  
同时，由于一次更新的好多j节点的`dp[j]`的值都是`dp[i]+1`，所以可以只用一个变量来记录这个值。  
这些等待下次被访问的条数相同的节点可以存到队列中，类似BFS，一段一段地向右前进。  
这样，空间复杂度就变成了最差是`O(n)`.  

由于每次跳数+1得到的是下一个连续的段，所以可以不用队列储存这一个段的元素，而是使用左右两个索引来记录。  
这样的空间复杂度就优化到了`O(1)`.  
```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        if (n < 2)
            return 0;
        
        int left = 0, right = 0;
        int ans = 0;
        while (left < n) {
            int nextRight = right;
            while (left <= right) {
                nextRight = max(nextRight, left + nums[left]);
                left++;
            }
            ans++;
            right = nextRight;
            if (right >= n - 1)
                break;
        }

        return ans;
    }
};
```
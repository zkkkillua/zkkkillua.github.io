---
title: 面试题 17.16. 按摩师
date: 2020-03-24 17:11:27
categories: leetcode
tags: 
- dp
---
A popular masseuse receives a sequence of back-to-back appointment requests and is debating which ones to accept. She needs a break between appointments and therefore she cannot accept any adjacent requests. Given a sequence of back-to-back appoint­ ment requests, find the optimal (highest total booked minutes) set the masseuse can honor. Return the number of minutes.

Note: This problem is slightly different from the original one in the book.

 

Example 1:

Input:  [1,2,3,1]
Output:  4
Explanation:  Accept request 1 and 3, total minutes = 1 + 3 = 4
Example 2:

Input:  [2,7,9,3,1]
Output:  12
Explanation:  Accept request 1, 3 and 5, total minutes = 2 + 9 + 1 = 12
Example 3:

Input:  [2,1,4,5,3,1,1,3]
Output:  12
Explanation:  Accept request 1, 3, 5 and 8, total minutes = 2 + 4 + 3 + 3 = 12

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-masseuse-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
_____________________________

## 框架
```cpp
class Solution {
public:
    int massage(vector<int>& nums) {

    }
};
```

## 1. 动态规划
设`dp[i]`代表从头到`nums[i]`服务的最大值，则`dp[i] = max(dp[i-1], dp[i-2]+nums[i])`.  
初始化`dp[0] = nums[0]; dp[1] = max(dp[0], dp[1])`.  
遍历一次后`dp[nums.size()-1]`即为结果，时间`O(n)`，空间`O(n)`。  
```cpp
class Solution {
public:
    int massage(vector<int>& nums) {
        int len = nums.size();
        if (len == 0)
            return 0;
        else if (len == 1)
            return nums[0];
        
        int *dp = new int[len];
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);

        for (int i = 2; i < len; i++)
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]);
        
        int ans = dp[len - 1];
        delete []dp;
        return ans;
    }
};
```

实际上，由于`dp[i]`只依赖于`dp[i-1]`与`dp[i-2]`，因此可以将数组换成变量，空间降为`O(1)`。  
```cpp
class Solution {
public:
    int massage(vector<int>& nums) {
        int len = nums.size();
        if (len == 0)
            return 0;
        
        int bbefore = 0, before = 0, cur = 0;
        for (int i = 0; i < len; i++) {
            cur = max(bbefore + nums[i], before);
            bbefore = before;
            before = cur;
        }

        return before;
    }
};
```
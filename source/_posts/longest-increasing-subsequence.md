---
title: 300.Longest Increasing Subsequence
date: 2020-03-14 18:34:48
categories: leetcode
tags: 
- dp
- 二分
---
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
________________________

## 框架
```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {

    }
};
```

## 1. 朴素dp`O(n^2)`
设`dp[i]`为以`a[i]`为结尾的最长上升子序列的长度。  
`dp[i]=max(dp[j]) + 1, j<i且a[j]到a[i]满足递增条件`，需要遍历之前所有的`dp[j]`。  

## 2. dp+二分查找`O(nlogn)`
设`dp[i]`为长度为`i`的上升子序列的**最小的**末尾元素（即最小的最大值），如1,2,4和1,2,3，`dp[3]=3`。  
遍历序列`a`，对于每个元素`a[i]`，有：  
- `a[i]>dp[last]`
  `dp[++last]=a[i]`  
- `a[i]<dp[last]`
  `dp[1]~dp[last]`之间总能找到一个位置`loc`，使得`dp[loc-1]<a[i]<dp[loc]`，那么可以用`a[i]`替换`dp[loc]`，代表可以用更小的结尾元素获得同样的长度。  
  在方法1中，查找是`O(n)`的，所以结果是`O(n^2)`。  
  此处，由于`dp`序列必是非递减的，可以利用二分查找，从而达到`O(nlogn)`的时间复杂度。  
  
```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        int *dp = new int[n + 1];
        for (int i = 0; i <= n; i++)
            dp[i] = 0;
        
        int resLen = 0;
        for (int i = 0; i < n; i++) {
            if (resLen == 0 || nums[i] > dp[resLen])
                dp[++resLen] = nums[i];
            else {
                int left = 1, right = resLen, mid = (left + right) / 2;
                while (left < right) {
                    if (dp[mid] >= nums[i])
                        right = mid;
                    else
                        left = mid + 1;
                    mid = (left + right) / 2;
                }
                dp[mid] = nums[i];
            }
        }

        delete []dp;
        return resLen;
    }
};
```
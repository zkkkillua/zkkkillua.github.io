---
title: 152.乘积最大子数组
date: 2020-07-23 11:06:26
categories: leetcode
tags: 
- dp
---
## 1. dp
最直接想到的是`dp[i]`代表以`nums[i]`为结尾的乘积最大值，`dp[i+1]`依赖`dp[i]`。  
但实际上这并不满足“最优子结构”，比如可能`nums[i]`为负，将`dp[i-1]`的正最大值变成了负值。  

如果不用dp的话，又很难想到方法使得`dp[i+1]`依赖于`dp[i]`。  
所以可以根据正负考虑转移关系。  
- `nums[i] > 0`时，`dp[i]`肯定依赖于为非负的最大值`dp[i-1]`  
- `nums[i] < 0`时，`dp[i]`依赖于i-1的最小值  
所以需要两个dp数组，分别记录以`nums[i]`为结尾的乘积最大值和最小值。  
  

设`dpMax[i]`和`dpMin[i]`分别代表以`nums[i]`为结尾的乘积的最大值和最小值。  
`dpMax[i] = max(dpMax[i - 1] * nums[i], dpMin[i - 1] * nums[i], nums[i])`  
`dpMin[i] = min(dpMax[i - 1] * nums[i], dpMin[i - 1] * nums[i], nums[i])`  
时间`O(n)`,空间`O(n)`但可以优化到`O(1)`。  
```cpp
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        int dpMax = nums[0], dpMin = nums[0], ans = nums[0];
        for (int i = 1; i < n; i++) {
            int tempMax = dpMax;
            dpMax = max(tempMax * nums[i], max(dpMin * nums[i], nums[i]));
            dpMin = min(tempMax * nums[i], min(dpMin * nums[i], nums[i]));
            ans = max(ans, dpMax);
        }

        return ans;
    }
};
```
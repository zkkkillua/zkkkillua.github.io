---
title: 41. 缺失的第一个正数
date: 2020-07-30 18:33:51
categories: leetcode
tags:
---
## 1. 辅助数组
`bool`类型的`1~n`的数组记录数据的出现情况，n为数据的个数。  
时间`O(n)`，空间`O(n)`。  

## 2. 原地重排
题目要求空间是`O(1)`的，单纯使用额外变量又没法记录得到最小值，同时又不能使用额外的空间，因此考虑原地重排。  
数据和位置的对应关系如下：  
```cpp
[3,4,-1,1]
 0,1, 2,3
```
遍历每个数据，如果不满足`i + 1 == nums[i]`，则将当前的`nums[i]`数据与`nums[nums[i] - 1]`数据交换。  
并将交换到`i`位置的数据也交换到其应该在的位置，直到当前位置满足上述条件或者交换过来的数据越界（负数或过大的正数）。  
因为所有数据至多交换n次，所以时间复杂度`O(n)`，空间复杂度`O(1)`。  
```cpp
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            while (i + 1 != nums[i] && nums[i] > 0 && nums[i] <= n && nums[nums[i] - 1] != nums[i]) {
                int temp = nums[nums[i] - 1];
                nums[nums[i] - 1] = nums[i];
                nums[i] = temp;
            }
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (i + 1 != nums[i]) {
                ans = i + 1;
                break;
            }
        }
        if (ans == 0)
            ans = n + 1;

        return ans;
    }
};
```

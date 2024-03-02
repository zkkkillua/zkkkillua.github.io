---
title: 面试题 08.03. 魔术索引
date: 2020-07-31 21:00:07
categories: leetcode
tags:
---
## 1. 顺序遍历
逐个判断，时间`O(n)`，空间`O(1)`。  
```cpp
class Solution {
public:
    int findMagicIndex(vector<int>& nums) {
        int n = nums.size();
        int ans = -1;
        for (int i = 0; i < n; i++) {
            if (i == nums[i]) {
                ans = i;
                break;
            }
        }

        return ans;
    }
};
```
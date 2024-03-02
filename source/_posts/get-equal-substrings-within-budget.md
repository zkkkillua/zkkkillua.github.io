---
title: 1208. 尽可能使字符串相等
date: 2021-02-05 15:34:29
categories: 
- leetcode
tags: 
- 双指针
- 滑动窗口
---
## 1. 滑动窗口
滑动窗口从左侧开始在满足cost的情况下向右滑动，记录最大窗口大小。  
当cost不足以支持窗口继续向右扩展时，左侧窗口向右收缩1次，然后右侧窗口继续向右扩展。  
时间`O(n)`，空间`O(1)`。  
```cpp
class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int n = s.length();
        int left = 0, right = 0, maxDist = 0;

        while (right < n) {
            int cost = abs(s[right] - t[right]);
            if (cost <= maxCost) {
                maxCost -= cost;
                right++;
                maxDist = max(maxDist, right - left);
            } else if (left < right) {
                maxCost += abs(s[left] - t[left]);
                left++;
            } else if (left == right) {
                left++;
                right++;
            }
        }

        return maxDist;
    }
};
```
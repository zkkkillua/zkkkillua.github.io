---
title: 978. 最长湍流子数组
date: 2021-02-08 22:04:29
categories: 
- leetcode
tags: 
- 滑动窗口
---
## 1. 滑动窗口
题目中要求的是“子数组”，但实际上是要求连续的“子串”。  
因此可以使用滑动窗口，固定左侧，右侧在满足“湍流”条件的情况下向右移动，直到不满足条件，记录此时子数组的长度。  
取长度的最大值，然后重新开始窗口的滑动。  
由于当前窗口内的子数组满足“湍流”条件，因此该子数组的任意子数组也满足“湍流”条件，故调整窗口左侧到右侧位置，以窗口最后一个元素作为下一个窗口新开始的元素。  
时间`O(n)`，空间`O(1)`。  
```cpp
class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        int n = arr.size();
        if (n <= 1)
            return n;

        int len = 0, maxLen = 0;
        int left = 0, right = 1;
        bool greater = arr[1] > arr[0];

        while (right < n) {
            if ((greater && arr[right] > arr[right - 1]) || (!greater && arr[right] < arr[right - 1])) {
                right++;
                greater = !greater;
            }
            else {
                len = right - left;
                maxLen = max(maxLen, len);
                while (right < n && arr[right] == arr[right - 1])
                    right++;
                left = right - 1;
                if (right < n)
                    greater = arr[right] > arr[left];
            }
        }
        maxLen = max(maxLen, right - left);

        return maxLen;
    }
};
```
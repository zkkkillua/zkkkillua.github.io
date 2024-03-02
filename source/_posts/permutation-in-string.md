---
title: 567. 字符串的排列
date: 2021-02-10 21:27:45
categories: 
- leetcode
tags: 
- 滑动窗口
---

## 1. 滑动窗口
要求是字符串的任一排列，因此不需要实际遍历各种排列，只需要统计该字符串各字符的个数即可。  
窗口右边界向右滑动，直到不可再滑动。如果此时还不满足条件，则左边界向右滑动1个位置，然后继续判断右边界。当左右边界重叠时右边界还不能向右滑动，证明字符串中不存在该字符，左右边界同时向右滑动1个位置。  
时间`O(n)`，空间`O(26)`。  
```cpp
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int len1 = s1.length(), len2 = s2.length();
        if (len1 > len2)
            return false;

        int left = 0, right = 0;
        bool res = false;
        int freq[26];
        for (int i = 0; i < 26; i++)
            freq[i] = 0;
        for (int i = 0; i < len1; i++)
            freq[s1[i] - 'a']++;

        while (right < len2) {
            if (freq[s2[right] - 'a'] > 0) {
                freq[s2[right] - 'a']--;
                right++;
                len1--;
                if (len1 == 0) {
                    res = true;
                    break;
                }
            } else {
                if (left == right) {
                    left++;
                    right++;
                } else {
                    freq[s2[left] - 'a']++;
                    left++;
                    len1++;
                }
            }
        }

        return res;
    }
};
```
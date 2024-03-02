---
title: 3.无重复字符的最长子串
date: 2020-05-02 10:46:51
categories: leetcode
tags: 
- 滑动窗口
---
## 1. 滑动窗口
因为只知道是字符，所以用hash表（unordered_map)来判重。  
hash表中记录字符位置，当遇到重复时，跳过记录的该字符的位置到达下一个位置。  
时间复杂度`O(n)`，空间复杂度`O(字符数)`（hash表占用）  
```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int len = s.length();
        if (len < 2)
            return len;

        unordered_map<char, int> loc;
        int ans = 0;
        int left = 0, right = 0;
        while (right < len) {
            if (loc.count(s[right]) == 1 && loc[s[right]] >= left) {
                ans = ans >= right - left ? ans : right - left;
                left = loc[s[right]] + 1;
            }
            loc[s[right]] = right;
            right++;
        }
        ans = ans >= right - left ? ans : right - left;

        return ans;
    }
};
```
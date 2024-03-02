---
title: 392. 判断子序列
date: 2020-07-27 16:27:44
categories: leetcode
tags: 
- 双指针
---
## 1. 双指针遍历
遍历s和t，时间`O(len(t))`，空间`O(1)`。  
如果短字符串s有无限多个，则可以预先处理t，得到每个位置开始下一个给定字符的最近位置，这样就可以直接跳转到下一个需要的位置了。  
```cpp
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int n1 = s.length(), n2 = t.length();
        if (n1 == 0)
            return true;
        int i1 = 0, i2 = 0;
        bool ans = false;
        while (i2 < n2) {
            if (s[i1] == t[i2])
                i1++;
            if (i1 >= n1) {
                ans = true;
                break;
            }
            i2++;
        }

        return ans;
    }
};
```

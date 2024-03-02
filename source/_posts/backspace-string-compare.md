---
title: 844.比较含退格的字符串
date: 2020-10-19 16:12:31
categories: 
- leetcode
tags:
---
## 1. 模拟
直接在原有字符串上进行修改，当遇到`#`时，把其左侧的第一个非`#`修改为`#`，表示已删除。  
为了更快的找到左侧第一个非`#`字符，而不是每次都要--遍历，可以直接逆序修改。  
时间`O(n)`，空间`O(1)`。  
```cpp
class Solution {
public:
    bool backspaceCompare(string S, string T) {
        int sLen = S.length(), tLen = T.length();
        int sCount = 0, tCount = 0;
        bool ans = true;

        for (int i = sLen - 1; i >= 0; i--) {
            if (sCount > 0 && S[i] != '#') {
                S[i] = '#';
                sCount--;
            } else if (S[i] == '#')
                sCount++;
        }
        for (int i = tLen - 1; i >= 0; i--) {
            if (tCount > 0 && T[i] != '#') {
                T[i] = '#';
                tCount--;
            } else if (T[i] == '#')
                tCount++;
        }

        int sidx = 0, tidx = 0;
        while (sidx < sLen || tidx < tLen) {
            while (sidx < sLen && S[sidx] == '#')
                sidx++;
            while (tidx < tLen && T[tidx] == '#')
                tidx++;
            if ((sidx == sLen && tidx < tLen) || (sidx < sLen && tidx == tLen)) {
                ans = false;
                break;
            } else if (sidx < sLen && tidx < tLen) {
                if (S[sidx++] != T[tidx++]) {
                    ans = false;
                    break;
                }
            }
        }

        return ans;
    }
};
```
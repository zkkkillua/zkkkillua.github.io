---
title: 763.划分字母区间
date: 2020-10-22 15:39:12
categories: 
- leetcode
tags:
---
## 1. 朴素
首先找到第一个字符最后一次出现的位置，得到一个子串。  
然后遍历这个子串，找其中每一个字符的最后一次出现的位置，得到这个子串最终的结尾。  
对右侧剩余部分做同样的处理。  
时间`O(n^2)`，空间`O(1)`。  
```cpp
class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<int> ans;
        int n = S.length();

        for (int i = 0; i < n;) {
            int lastIdx = lastLocation(S, i);       // 获取开始字符的最后出现位置
            for (int j = i + 1; j < lastIdx; j++)
                // 这里可以适当剪枝，已经访问过的字符之后不需要再重复访问了，因为其最后出现的位置还是不变的。
                lastIdx = max(lastIdx, lastLocation(S, j));
            ans.push_back(lastIdx - i + 1);
            i = lastIdx + 1;
        }

        return ans;
    }
private:
    int lastLocation(string S, int k) {
        int n = S.length();
        for (int i = k + 1; i < n; i++)
            if (S[k] == S[i])
                k = i;
        
        return k;
    }
};
```
  
## 2. 记忆化
上述方法的问题是在查找每个元素出现的最后一个位置上花费了太多的时间，导致时间复杂度是`O(n^2)`的。  
可以使用一个`bool`数组记录已经访问过最后一个位置的元素，之后再遇到就不需要再次访问了，不过这样最差是`O(26n)`的。  
更好的方法是首先遍历一次字符串，使用一个大小为26的数组记录每个字符最后出现的位置，在需要最后一个位置时直接查表。  
时间`O(n)`，空间`O(26) = O(1)`。  
```cpp
class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<int> ans, loc(26, 0);
        int n = S.length();
        for (int i = 0; i < n; i++)
            loc[S[i] - 'a'] = i;

        for (int i = 0; i < n;) {
            int lastIdx = loc[S[i] - 'a'];       // 获取开始字符的最后出现位置
            for (int j = i + 1; j < lastIdx; j++)
                // 这里可以适当剪枝，已经访问过的字符之后不需要再重复访问了，因为其最后出现的位置还是不变的。
                lastIdx = max(lastIdx, loc[S[j] - 'a']);
            ans.push_back(lastIdx - i + 1);
            i = lastIdx + 1;
        }

        return ans;
    }
};
```
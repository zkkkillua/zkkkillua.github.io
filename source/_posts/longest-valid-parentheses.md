---
title: 32.最长有效括号
date: 2020-07-28 22:09:17
categories: leetcode
tags:
---
## 1. 朴素
**错误！！**  
```cpp
输入:
"()(()"
输出
4
预期结果
2
```
题目要求的是子串，而不是任意匹配即可。  
求从每一个'('的位置开始，最长的有效括号子串的长度。  
时间`O(n^2)`，空间`O(1)`。  
```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.length();
        int ans = 0;

        for (int i = 0; i < n; i++) {
            if (s[i] == ')')
                continue;
            int temp = 0, llen = 1;
            for (int j = i + 1; j < n; j++) {
                if (s[j] == '(')
                    llen++;
                else {
                    if (llen > 0) {
                        llen--;
                        temp++;
                    } else
                        break;
                }
                ans = ans >= temp ? ans : temp;
            }
        }

        return ans * 2;     // 返回的是子串的长度
    }
};
```

## 2. 修改后的朴素
根据1中的错误可知，需要在左括号个数清零时才能累计个数++。  
```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.length();
        int ans = 0;

        for (int i = 0; i < n; i++) {
            if (s[i] == ')')
                continue;
            int cur = 0, temp = 0, llen = 1;
            for (int j = i + 1; j < n; j++) {
                if (s[j] == '(')
                    llen++;
                else {
                    if (llen > 0) {
                        llen--;
                        temp++;
                        if (llen == 0) {
                            cur += temp;
                            temp = 0;
                        }
                    } else
                        break;
                }
                ans = ans >= cur ? ans : cur;
            }
        }

        return ans * 2;     // 返回的是子串的长度
    }
};
```

## 3. 继续优化上述算法
已经知道了需要在左括号数目清零时才++个数，所以可以不需要再在每个左括号处都作为起始来计算长度了。  
时间`O(n)`，空间`O(1)`.  
```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.length();
        int ans = 0;
        int cur = 0, temp = 0, llen = 0;

        for (int i = 0; i < n; i++) {
            if (s[i] == '(')
                llen++;
            else {
                if (llen > 0) {
                    llen--;
                    temp++;
                    if (llen == 0) {
                        cur += temp;
                        temp = 0;
                    }
                } else {
                    if (cur != 0) {
                        ans = ans >= cur ? ans : cur;
                        cur = 0;
                    }
                }
            }
        }

        return max(ans * 2, cur * 2);     // 返回的是子串的长度
    }
};
```
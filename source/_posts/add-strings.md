---
title: 415. 字符串相加
date: 2020-08-03 16:06:05
categories: leetcode
tags:
---
## 1. 模拟
直接在string上逐位模拟加法的过程。  
需要特别注意的是仍有剩余部分的字符串的处理过程。  
时间`O(len)`，空间`O(1)`.  
```cpp
class Solution {
public:
    string addStrings(string num1, string num2) {
        int n1 = num1.length(), n2 = num2.length();
        int i1 = n1 - 1, i2 = n2 - 1, c = 0;
        string sum = "";
        while (i1 >= 0 || i2 >= 0 || c != 0) {
            if (i1 >= 0)
                c += num1[i1--] - '0';
            if (i2 >= 0)
                c += num2[i2--] - '0';
            sum = to_string(c % 10) + sum;
            c /= 10;
        }

        return sum;
    }
};
```
---
title: 343.整数拆分
date: 2020-07-30 22:46:42
categories: leetcode
tags:
---
## 1. 数学
分析将一个数拆成以下部分：  
拆1：没用  
拆2：可以  
拆3：可以  
拆4：可以，跟2一样  
拆5+：对半拆分后的乘积要比原来的值大  
综上，尽可能拆出3，不要剩余1.  
时间`O(1)`，空间`O(1)`。  
```cpp
class Solution {
public:
    int integerBreak(int n) {
        if (n <= 3)
            return n - 1;

        int n3 = n / 3;
        int n2 = 0;
        n %= 3;
        if (n == 1) {
            n3--;
            n2 = 2;
        } else if (n == 2)
            n2 = 1;

        return pow(3, n3) * pow(2, n2);
    }
};
```
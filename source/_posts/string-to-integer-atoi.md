---
title: 8.字符串转换整数 (atoi)
date: 2020-04-03 11:36:29
categories: leetcode
tags:
---
## 框架
```cpp
class Solution {
public:
    int myAtoi(string str) {
        
    }
};
```

## 1. 直接模拟
```cpp
class Solution {
public:
    int myAtoi(string str) {
        int n = str.length();
        int flag = 1;
        long long ans = 0;
        //判断是否溢出的时候可以比较int ans和INT_MAX / 10的关系，这样就不会ans * 10溢出了。
        bool hasNumber = false;

        for (int i = 0; i < n; i++) {
            if (str[i] != ' ' && str[i] != '+' && str[i] != '-' && !(str[i] >= '0' && str[i] <= '9') && !hasNumber)    //数字前有其他字符
                return 0;
            else if (!(str[i] >= '0' && str[i] <= '9') && hasNumber)    //数字后有其他字符
                return flag * ans;
            else if (str[i] == '-' || str[i] == '+') {   //数字符号
                if (i + 1 < n && (str[i + 1] >= '0' && str[i + 1] <= '9')) {
                    hasNumber = true;
                    if (str[i] == '-')
                        flag = -1;
                } else
                    return 0;
            } else if (str[i] >= '0' && str[i] <= '9') {      //是数字
                hasNumber = true;
                ans = ans * 10 + (str[i] - '0');
                if (flag == 1 && ans >= pow(2, 31) - 1)
                    return pow(2, 31) - 1;
                else if (flag == -1 && ans >= pow(2, 31))
                    return -pow(2, 31);
            }
        }

        return flag * ans;
    }
};
```

## 2. 自动机
我看到这个题解直接傻了，太nb了。  
没想到自动机还可以用来解题啊……  
https://leetcode-cn.com/problems/string-to-integer-atoi/solution/zi-fu-chuan-zhuan-huan-zheng-shu-atoi-by-leetcode-/
---
title: 224. 基本计算器
date: 2021-03-10 15:03:54
categories: 
- leetcode
tags: 
- 栈
---
## 1. 辅助栈
一个栈存操作数，一个栈存操作符。  
为了避免`-1+2`和`1+(-2+3)`等情况，还要判断操作符的上一位，看是否需要在操作数栈中添加0.  
时间`O(n)`，空间`O(n)`。  
```cpp
class Solution {
public:
    int calculate(string s) {
        int n = s.length();
        char last = ' ';
        stack<int> nums;
        stack<char> ops;

        for (int i = 0; i < n; i++) {
            if (s[i] == ' ')
                continue;
            else if (s[i] >= '0' && s[i] <= '9') {
                int num = 0;
                while (i < n && s[i] >= '0' && s[i] <= '9') {
                    num = num * 10 + (s[i++] - '0');
                }
                i--;
                nums.push(num);
                last = 'n';
            } else {
                if (s[i] != '(' && last != 'n' && last != ')')
                    nums.push(0);
                while (s[i] != '(' && !ops.empty() && ops.top() != '(') {
                    char op = ops.top();
                    ops.pop();
                    int b = nums.top();
                    nums.pop();
                    int a = nums.top();
                    nums.pop();
                    if (op == '+')
                        nums.push(a + b);
                    else if (op == '-')
                        nums.push(a - b);
                }
                if (s[i] != ')')
                    ops.push(s[i]);
                else
                    ops.pop();
                last = s[i];
            }
        }

        while (!ops.empty()) {
            char op = ops.top();
            ops.pop();
            int b = nums.top();
            nums.pop();
            int a = nums.top();
            nums.pop();
            if (op == '+')
                nums.push(a + b);
            else if (op == '-')
                nums.push(a - b);
        }

        return nums.top();
    }
};
```

## 2. 去括号
算式中只有加减法，因此可以全部看作是加法，将减法看作是负数。  
还是使用辅助栈，不过栈只存正负号，代表当前括号外部是正号还是负号。  
时间`O(n)`，空间`O(n)`。  
```cpp
class Solution {
public:
    int calculate(string s) {
        int n = s.length();
        stack<int> signs;
        signs.push(1);
        int sign = 1;
        int res = 0;

        for (int i = 0; i < n; i++) {
            if (s[i] == ' ')
                continue;
            else if (s[i] >= '0' && s[i] <= '9') {
                int num = 0;
                while (i < n && s[i] >= '0' && s[i] <= '9')
                    num = num * 10 + (s[i++] - '0');
                i--;
                res += sign * num;
            } else {
                if (s[i] == '(')
                    signs.push(sign);
                else if (s[i] == ')')
                    signs.pop();
                else if (s[i] == '+')
                    sign = signs.top();
                else if (s[i] == '-')
                    sign = -signs.top();
            }
        }

        return res;
    }
};
```
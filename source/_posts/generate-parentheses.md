---
title: 22.Generate Parentheses
date: 2020-04-09 14:35:21
categories: leetcode
tags:
---
## 框架
```cpp
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        
    }
};
```

## 1. 递归
```cpp
class Solution {
public:
    void recursion(string s, int total, int cur) {
        if (total == n) {
            while (cur > 0) {
                s += ')';
                cur--;
            }
            vec.push_back(s);
            return;
        }
        
        recursion(vec, s + '(', total + 1, cur + 1, n);
        if (cur > 0)
            recursion(vec, s + ')', total, cur - 1, n);
    }

    vector<string> generateParenthesis(int n) {
        vec.clear();
        this->n = n;

        recursion(ans, "(", 1, 1);

        return ans;
    }

private:
    vector<string> vec;
    int n;
};
```

---
title: 680.验证回文字符串II
date: 2020-05-20 00:13:25
categories: leetcode
tags: 
- 双指针
---
## 1. 朴素
首先判断不删除字符的情况下，s本身是不是回文串。  
之后遍历判断删除每个字符，剩下的部分是否是回文串。  
时间`O(n^2)`，空间`O(1)`，超时。  
```cpp
class Solution {
public:
    bool isPalindromic(const string& s) {
        int n = s.length();
        for (int i = 0; i < n / 2; i++) {
            if (s[i] != s[n - i - 1])
                return false;
        }
        return true;
    }
    bool validPalindrome(string s) {
        if (isPalindromic(s))
            return true;
        
        for (int i = 0; i < s.length(); i++) {
            if (isPalindromic(s.erase(i)))
                return true;
        }

        return false;
    }
};
```

## 2. 双指针+贪心
初始双指针指在s的左右两侧。  
1. 判断s是否是回文串，若是则返回true，否则继续。  
2. 若s不是回文串，则将s的开头和结尾的相等的部分删除，直到开头和结尾的字符不相等。  
3. 当开头和结尾不相等时，则`s[1:-1]`和`s[0:-2]`之中必须有一个是回文串，否则不可能满足删除至多一个字符得到回文串的要求。  

这样，最多只需要执行3次`isPalindromic()`函数即可实现。  
时间`O(n)`，空间`O(1)`。  
```cpp
class Solution {
public:
    bool isPalindromic(const string& s) {
        int n = s.length();
        for (int i = 0; i < n / 2; i++) {
            if (s[i] != s[n - i - 1])
                return false;
        }
        return true;
    }
    bool validPalindrome(string s) {
        if (isPalindromic(s))
            return true;
        
        int i, n = s.length();
        for (i = 0; i < n / 2; i++) {
            if (s[i] != s[n - i - 1])
                break;
        }

        return isPalindromic(s.substr(i, n - 2 * i - 1)) || isPalindromic(s.substr(i + 1, n - 2 * i - 1));
    }
};
```
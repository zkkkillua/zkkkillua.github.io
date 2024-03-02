---
title: 151.Reverse Words in a String
date: 2020-04-10 14:18:22
categories: leetcode
tags:
---
## 框架
```cpp
class Solution {
public:
    string reverseWords(string s) {

    }
};
```

## 1. 借助额外空间
主要学会string的`find_first(last)_of()`函数和`find_first(last)_not_of()`函数的使用。  
分别是找到第一个（最后一个）参数的位置和找到第一个（最后一个）不是参数的位置。  
而`find()`和`find_first_of()`的区别是：  
`s.find("abc")`必须找到`s`中子串`abc`的位置，而`s.find_first_of("abc")`只需要找到`s`中a或b或c中任意一个字符的第一个位置。  
`s.substr(起始位置, 截取长度（默认到结尾）)`  
`s.erase(迭代器开始, 迭代器结束（不含）（默认到结尾）)`  
`s.erase(起始位置, 删除长度（默认到结尾）)`  
```cpp
class Solution {
public:
    string reverseWords(string s) {
        s.erase(0, s.find_first_not_of(' '));   // 删除左侧空格
        s.erase(s.find_last_not_of(' ') + 1);   // 删除右侧空格

        string rev = "";
        while (!s.empty()) {
            int loc = s.find_last_of(' ');
            rev += s.substr(loc + 1) + ' ';
            if (loc != -1) {
                s = s.substr(0, loc);
                int space_loc = s.find_last_not_of(' ');
                if (space_loc == -1)
                    s = "";
                else
                    s = s.substr(0, space_loc + 1);
            }
            else {
                s = "";
                rev.erase(rev.length() - 1);
            }
        }

        return rev;
    }
};
```

## 2. 原地重排
先把字符串整体反转，然后把字符串中每个单词反转。  
```cpp
class Solution {
public:
    string reverseWords(string s) {
        s.erase(0, s.find_first_not_of(' '));
        s.erase(s.find_last_not_of(' ') + 1);
        reverse(s.begin(), s.end());

        int cur = 0;
        while (!s.empty()) {
            int loc = s.find_first_of(' ', cur);
            if (loc == -1) {
                int len = s.length();
                for (int i = 0; i <= (len - 1 - cur) / 2; i++)
                    swap(s[cur + i], s[len - 1 - i]);
                break;
            }
            for (int i = 0; i <= (loc - 1 - cur) / 2; i++) 
                swap(s[cur + i], s[loc - 1 - i]);
            cur = loc + 1;
            s = s.erase(cur, s.find_first_not_of(' ', cur) - cur);
        }

        return s;
    }
};
```
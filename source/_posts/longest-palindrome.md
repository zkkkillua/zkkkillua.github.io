---
title: 409.Longest Palindrome
date: 2020-03-19 23:19:18
categories: leetcode
tags:
---
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
______________________________

## 框架
```cpp
class Solution {
public:
    int longestPalindrome(string s) {

    }
};
```

## 1. 统计次数
回文串中所有的同一类的字符必为偶数个，再加上可能有的最中间的那个字符。  
每个字符遍历一次，`O(n)`。
```cpp
class Solution {
public:
    int longestPalindrome(string s) {
        int count[52];
        for (int i = 0; i < 52; i++)
            count[i] = 0;
        int ans = 0;

        int lenS = s.length();
        for (int i = 0; i < lenS; i++) {
            if (s[i] >= 'a' && s[i] <= 'z')
                count[s[i] - 'a']++;
            else
                count[s[i] - 'A' + 26]++;
        }

        for (int i = 0; i < 52; i++) {
            if (count[i] % 2 == 0)
                ans += count[i];
            else
                ans += count[i] - 1;
        }
        if (ans < lenS)
            ans++;
        
        return ans;
    }
};
```
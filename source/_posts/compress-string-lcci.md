---
title: 面试题 01.06. Compress String LCCI
date: 2020-03-16 14:19:02
categories: leetcode
tags:
---
Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

Example 1:

Input: "aabcccccaaa"
Output: "a2b1c5a3"
Example 2:

Input: "abbccd"
Output: "abbccd"
Explanation: 
The compressed string is "a1b2c2d1", which is longer than the original string.


Note:

0 <= S.length <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/compress-string-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
________________________

## 框架
```cpp
class Solution {
public:
    string compressString(string S) {

    }
};
```

## 1. 直接模拟
```cpp
class Solution {
public:
    string compressString(string S) {
        if (S.size() == 0)
            return S;

        char cur = S[0];
        int len = 1;
        int sLen = S.size();
        string res = "";
        
        for (int i = 1; i < sLen; i++) {
            if (S[i] == cur)
                len++;
            else {
                //res = res + cur + to_string(len);     //报错，超出内存限制
                //上边这条语句相当于建立了一个新的string对象，其由res+cur+to_string(len)组成，然后赋值给res
                //而下边这条语句是相当于建立了cur+to_string(len)，然后再直接添加到res后面。
                res += cur + to_string(len);
                cur = S[i];
                len = 1;
            }
        }
        res = res + cur + to_string(len);
        res = res.size() < S.size() ? res : S;

        return res;
    }
};
```
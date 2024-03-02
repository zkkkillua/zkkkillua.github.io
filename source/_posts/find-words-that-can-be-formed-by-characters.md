---
title: 1160.Find Words That Can Be Formed by Characters
date: 2020-03-17 10:54:28
categories: leetcode
tags:
---
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
________________________________

## 框架
```cpp
class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {

    }
};
```

## 1. 统计次数
既然字母的次序是不好匹配的，那只需要统计次数就可以了。
一共就26个字母，用hash表`unordered_map`可以，不过用数组`int a[26]`会更省空间。
遍历每个字符串，统计字母次数就可以了，复杂度是`O(n)`，n是所有字符串的长度之和。

P.S.  
我之前的想法是，朴素的话就是挨个对比，对word的每个字符都得扫描一遍chars。  
然后优化一下就是先排好序，再比较就不用每个字符都去扫描chars了。
不过实际上这类问题统计次数就可以解决的问题，再去排个序就更麻烦了，而且复杂度也要高。  

```cpp
class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        int count[26];
        int charsCount[26];
        int res = 0;
        for (int i = 0; i < 26; i++)
            charsCount[i] = 0;
        for (string::iterator iter = chars.begin(); iter != chars.end(); ++iter)
            charsCount[(*iter) - 'a']++;
        
        for (vector<string>::iterator iterw = words.begin(); iterw != words.end(); ++iterw) {
            for (int i = 0; i < 26; i++)
                count[i] = 0;
            for (string::iterator iters = iterw->begin(); iters != iterw->end(); ++iters)
                count[*iters - 'a']++;
            
            bool flag = true;
            for (int i = 0; i < 26; i++)
                if (count[i] > charsCount[i]) {
                    flag = false;
                    break;
                }
            if (flag)
                res += iterw->length();
        }

        return res;
    }
};
```
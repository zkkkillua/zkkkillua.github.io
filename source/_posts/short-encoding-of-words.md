---
title: 820.Short Encoding of Words
date: 2020-03-29 11:16:41
categories: leetcode
tags:
---
Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#" and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the given words?

Example:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].


Note:

1 <= words.length <= 2000.
1 <= words[i].length <= 7.
Each word has only lowercase letters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/short-encoding-of-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
________________________________

## 框架
```cpp
class Solution {
public:
    int minimumLengthEncoding(vector<string>& words) {

    }
};
```

## 1. 朴素
分析可知，如果A和B能够被简化表示，则A或B一定是完全地是对方的结尾部分。  
即time和me，而不能是time和mesh。所以可以从它们的结尾逆序进行比较。  
遍历每两个单词，从结尾比较看能否完全被包含。  
时间`O(n^2 * wordLen)`，空间记录一下是不是已经被包含了，`O(n)`  
*超时了*  
```cpp
class Solution {
public:
    int minimumLengthEncoding(vector<string>& words) {
        int ans = 0;
        int n = words.size();
        vector<bool> contained(n);
        vector<bool> encoded(n);
        for (int i = 0; i < n; i++){
            contained[i] = false;
            encoded[i] = false;
        }
        
        for (int i = 0; i < n; i++) {
            if (contained[i])
                continue;
            for (int j = 0; j < n; j++) {
                if (i != j && !contained[j]) {
                    int ilen = words[i].length(), jlen = words[j].length();
                    if (jlen > ilen)
                        continue;
                    
                    bool isContained = true;
                    while (jlen > 0) {
                        if (words[i][--ilen] != words[j][--jlen]) {
                            isContained = false;
                            break;
                        }
                    }
                   
                    if (isContained) {
                        contained[j] = true;
                        if (encoded[i] && encoded[j])
                            ans--;
                        if (!encoded[i] && !encoded[j]) {
                            encoded[i] = true;
                            ans++;
                        }
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (encoded[i] && !contained[i])
                ans += words[i].length();
            else if (!encoded[i] && !contained[i])
                ans += words[i].length() + 1;
        }

        return ans;
    }
};
```

## 2. 排序
如果把每个字符串都反转，再从小到大排序，就可以发现如果二者是包含关系的话，则二者一定相邻并且左侧的被右侧的包含。  
不过以下代码不反转字符串，而是重新写sort的compare函数。  
时间`O(nlogn)`，空间`O(1)`.  
```cpp
class Solution {
public:
    //这里需要用static，因为非静态成员函数的参数中会隐含地让this指针作为第一个参数
    //而sort的compare函数的参数要求是两个参数，所以加static避免它隐含加上第一个参数this。
    static bool cmp (string& a, string& b) {
        int aLen = a.length(), bLen = b.length();
        for (int i = 1; i <= min(aLen, bLen); i++) 
            if (a[aLen - i] != b[bLen - i])
                return a[aLen - i] < b[bLen - i];
        return aLen <= bLen;
    }

    int minimumLengthEncoding(vector<string>& words) {
        int n = words.size();
        int ans = 0;
        sort (words.begin(), words.end(), cmp);

        for (int i = 0; i < n - 1; i++) {
            int iLen = words[i].length(), jLen = words[i + 1].length();
            if (iLen > jLen) {
                ans += iLen + 1;
                continue;
            }
            
            for (int k = 1; k <= iLen; k++) {
                if (words[i][iLen - k] != words[i + 1][jLen - k]) {
                    ans += iLen + 1;
                    break;
                }
            }
        }
        ans += words[n - 1].length() + 1;

        return ans;
    }
};
```

## 3. 字典树Trie
为了方便管理子节点，字典树（如果是全小写字母）会开一个26的数组记录子节点。  
可以有两个方法统计长度：  
1. 用hash表记录每个单词的结尾在Trie中的位置和在数组中位置的映射关系，当该Trie结点没有子节点时可以根据映射关系获取该单词的长度，加到结果中。  
2. 插入的时候先插长的，这样如果后续插入中需要开辟新的结点，则说明该单词是新的而不是后缀，直接加上它的长度。不过这种方法需要先根据单词长度由长到短进行排序。  

https://leetcode-cn.com/problems/short-encoding-of-words/solution/99-java-trie-tu-xie-gong-lue-bao-jiao-bao-hui-by-s/
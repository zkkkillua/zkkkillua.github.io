---
title: 136.只出现一次的数字
date: 2020-05-14 23:36:35
categories: leetcode
tags: 
- 位运算
---
## 1. hash表
直接hash表记录次数，但是空间占用有点多。  
时间`O(n)`，空间`O(n)`.  
```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int, int> hashTable;
        for (int i = 0; i < nums.size(); i++)
            hashTable[nums[i]]++;
        
        int ans;
        for (unordered_map<int, int>::iterator it = hashTable.begin(); it != hashTable.end(); ++it)
            if (it->second == 1) {
                ans = it->first;
                break;
            }

        return ans;
    }
};
```

## 2.　位运算异或
偶数个相同的数据异或之后变成0，而任何数异或0还是它本身。  
时间`O(n)`，空间`O(1)`。  
```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < nums.size(); i++)
            ans ^= nums[i];
        return ans;
    }
};
```
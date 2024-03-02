---
title: 697. 数组的度
date: 2021-02-20 00:40:27
categories: 
- leetcode
tags: 
- hash表
---
## 1. hash表
首先使用hash表记录每个数据出现的频数，就可以得知最大的频数及其对应的数据。  
此时如果有该数据的第一次和最后一次出现的位置，则可以获得这段区间的长度，比较频数最大的数据的区间的最小值即可。  
数据的记录可以用hash表，key是元素值，为保证数据的一致性，value是一个数组，储存频数、首位置和末位置。也可以用3个数组直接储存，因为已经给定了0~49999的范围。  
时间`O(n)`，空间`O(n)`。  
```cpp
class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, vector<int>> mp;     // key, [freq, first, last]
        int maxFreq = 0, minLen = 0;

        for (int i = 0; i < n; i++) {
            if (mp.count(nums[i]) == 0)
                // mp[nums[i]].emplace_back(1, i, i);       // 此时数组还不存在
                mp[nums[i]] = {1, i, i};
            else {
                mp[nums[i]][0]++;
                mp[nums[i]][2] = i;
            }
            if (maxFreq == mp[nums[i]][0])
                minLen = min(minLen, mp[nums[i]][2] - mp[nums[i]][1] + 1);
            else if (maxFreq < mp[nums[i]][0]) {
                maxFreq = mp[nums[i]][0];
                minLen = mp[nums[i]][2] - mp[nums[i]][1] + 1;
            }
        }

        return minLen;
    }
};
```
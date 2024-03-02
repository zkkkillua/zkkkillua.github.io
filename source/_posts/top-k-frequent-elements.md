---
title: 347.前K个高频元素
date: 2020-09-07 13:06:20
categories: leetcode
tags: 
- 堆
---
## 1.小根堆
首先遍历一次数组，统计得到每个数字的出现次数。  
然后遍历第二次，通过小根堆筛选出k个高频元素。  
时间`O(nlogk)`，空间`O(n)`记录次数。  
记录数字出现次数使用hash表`unordered_map`.  
*`map`的实现依赖于红黑树，内部是有序的，实现了对数级别的查找。*  
*`map`与hash表没有关系。hash表用更大的空间实现了更快的查找：`O(1)`。*  
*hash表可以使用`unordered_map`，由hash函数实现，所以查找插入和删除都是`O(1)`的。*  
*也正因为如此，`unordered_map`的内部元素是无序的，而`map`内部是有序的。*  
*至于`hash-map`，它与`unordered_map`功能相同，但是不属于STL，是历史原因，使用`unordered_map`即可。*  
```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counter;
        priority_queue<pair<int, int>> q;
        vector<int> ans;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            if (counter.count(nums[i]) == 0) 
                counter[nums[i]] = 1;
            else
                counter[nums[i]]++;
        }

        for (auto iter = counter.begin(); iter != counter.end(); ++iter) {
            if (q.size() < k)
                q.push(make_pair(-iter->second, iter->first));
            else if (iter->second > -q.top().first) {
                q.pop();
                q.push(make_pair(-iter->second, iter->first));
            }
        }

        while (!q.empty()) {
            ans.push_back(q.top().second);
            q.pop();
        }

        return ans;
    }
};
```
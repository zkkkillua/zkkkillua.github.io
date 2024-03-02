---
title: 496. 下一个更大元素 I
date: 2021-03-06 10:35:36
categories: 
- leetcode
tags: 
- 单调栈
---
## 1. 单调栈+hash表
使用一个单调递减栈遍历`nums2`，当元素比栈顶小时入栈；当比栈顶大时代表该元素是栈顶及随后一部分比该元素小的元素的“下一个更大元素”，故弹出较小的元素，将该元素作为他们的“下一个更大元素”，将该元素入栈。  
这样求得的是所有元素的“下一个更大元素”，需要hash表记录一下，最后只取`nums1`中对应的。  
时间`O(m + n)`，空间`O(m + n)`。  
```cpp
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size(), n2 = nums2.size();
        stack<int> st;
        unordered_map<int, int> nextGreater;
        vector<int> res;

        for (int i = 0; i < n2; i++) {
            while (!st.empty() && nums2[i] > st.top()) {
                nextGreater[st.top()] = nums2[i];
                st.pop();
            }
            st.push(nums2[i]);
        }
        while (!st.empty()) {
            nextGreater[st.top()] = -1;
            st.pop();
        }

        for (int i = 0; i < n1; i++)
            res.push_back(nextGreater[nums1[i]]);
        
        return res;
    }
};
```
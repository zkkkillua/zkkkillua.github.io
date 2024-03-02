---
title: 503. 下一个更大元素 II
date: 2021-03-06 10:35:57
categories: 
- leetcode
tags: 
- 单调栈
---
## 1. 单调栈
- 使用单调递减栈  
- 数组中的最大值的“下一个更大元素”不存在，是-1  
- 获得所有元素的“下一个最大元素”最多需要2次遍历  
- 数组最大值一共有x个，当数组的最后一个元素是最大值时结束；否则当单调栈中只有x+1个元素且栈顶元素是最大值时代表栈中全是最大值，结束  

```cpp
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        if (n == 0)
            return {};
        stack<int> st;
        vector<int> res(n, -1);

        int maxValue = nums[0], maxValueFreq = 0;
        for (int i = 1; i < n; i++)
            if (nums[i] > maxValue)
                maxValue = nums[i];
        for (int i = 0; i < n; i++)
            if (nums[i] == maxValue)
                maxValueFreq++;

        for (int i = 0; i < n; i++) {
            while (!st.empty() && nums[i] > nums[st.top()]) {
                if (res[st.top()] == -1)
                    res[st.top()] = nums[i];
                st.pop();
            }
            st.push(i);
            if (i == n - 1) {
                if (nums[i] == maxValue)
                    break;
                else
                    i = -1;
            }
            if (st.size() == maxValueFreq + 1 && nums[st.top()] == maxValue)
                break;
        }

        return res;
    }
};
```
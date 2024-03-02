---
title: 739. 每日温度
date: 2020-07-30 17:34:12
categories: leetcode
tags: 
- 栈
- 单调栈
---
## 1. 单调栈
使用一个辅助的单调递减栈，栈内存放数据的索引。  
当当前元素大于栈顶元素时，弹出栈顶元素，并同时可以得到弹出的栈顶元素距离右侧第一个大于它的元素的位置。  
当当前元素小于等于栈顶元素时，入栈。  
时间`O(n)`，空间`O(n)`。  
```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        stack<int> s;
        int n = T.size();
        vector<int> ans(n, 0);
        
        for (int i = 0; i < n; i++) {
            if (s.empty() || T[i] <= T[s.top()])
                s.push(i);
            else {
                int topIndex = s.top();
                while (!s.empty() && T[i] > T[topIndex]) {
                    s.pop();
                    ans[topIndex] = i - topIndex;
                    if (s.empty()) 
                        break;
                    topIndex = s.top();
                }
                s.push(i);
            }
        }

        return ans;
    }
};
```
---
title: 1438. 绝对差不超过限制的最长连续子数组
date: 2021-02-21 15:55:58
categories: 
- leetcode
tags: 
- 滑动窗口
- 堆
- 单调队列
---
## 1. 朴素
滑动窗口，记录窗口内部的最大值和最小值。  
但是每次移动窗口之后，如果最大值或者最小值被移除了，则需要重新遍历窗口内部的元素获取。  
时间`O(n^2)`，空间`O(1)`。  

## 2. 堆
使用大根堆和小根堆保存当前窗口内部的数据，从而能够直接获得最大值和最小值。  
不过问题在于，如果移动窗口移除的是非最大值或最小值，则堆是无法直接删除非堆顶的元素的，需要使用hash表记录，每次删除时对照hash表，延迟删除。  
时间`O(nlogn)`，空间`O(n)`。  
```cpp
class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        int n = nums.size();
        int left = 0, right = 0;
        int res = 0;
        priority_queue<int> bigHeap;
        priority_queue<int, vector<int>, greater<int>> smallHeap;
        unordered_map<int, int> bigDel, smallDel;

        while (right < n) {
            if (bigHeap.empty() || (!bigHeap.empty() && bigHeap.top() - nums[right] <= limit && nums[right] - smallHeap.top() <= limit)) {
                bigHeap.push(nums[right]);
                smallHeap.push(nums[right]);
                right++;
            } else {
                res = max(res, right - left);
                bigDel[nums[left]]++;
                smallDel[nums[left]]++;
                left++;
            }

            while (!bigHeap.empty() && bigDel[bigHeap.top()] > 0) {
                bigDel[bigHeap.top()]--;
                bigHeap.pop();
            }
            while (!smallHeap.empty() && smallDel[smallHeap.top()] > 0) {
                smallDel[smallHeap.top()]--;
                smallHeap.pop();
            }
        }
        res = max(res, right - left);

        return res;
    }
};
```

## 3. 单调队列
对滑动窗口而言，堆，即优先队列，可以获取最大值和最小值，但是不便于维护。因为当窗口滑过，非堆顶的元素无法及时删除，还需要额外使用数组记录延迟删除。  
动态维护滑动窗口内部的最值更方便的手段是使用单调队列/栈。  

维护窗口内的最小值，可以使用单调递增队列；维护窗口内的最大值，可以使用单调递减队列。  
此处使用双端队列作为单调队列，因为右窗口右移添加和移除元素是在队尾，左窗口右移移除元素是在队首，所以需要双端队列。  
时间`O(n)`，空间`O(n)`。  
```cpp
class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        int n = nums.size();
        int left = 0, right = 0, res = 0;
        deque<int> greaterQ, smallerQ;

        while (right < n) {
            if (greaterQ.empty() || (!greaterQ.empty() && nums[right] - greaterQ.front() <= limit && smallerQ.front() - nums[right] <= limit)) {
                while (!greaterQ.empty() && nums[right] < greaterQ.back())
                    greaterQ.pop_back();
                greaterQ.push_back(nums[right]);
                while (!smallerQ.empty() && nums[right] > smallerQ.back())
                    smallerQ.pop_back();
                smallerQ.push_back(nums[right]);
                right++;
            } else {
                res = max(res, right - left);
                if (nums[left] == greaterQ.front())
                    greaterQ.pop_front();
                if (nums[left] == smallerQ.front())
                    smallerQ.pop_front();
                left++;
            }
        }
        res = max(res, right - left);

        return res;
    }
};
```